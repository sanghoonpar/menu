import os, run_service, requests, menu_choose
from flask import Flask, request, render_template
from dotenv import load_dotenv
from flask_lucide import Lucide
load_dotenv()

n = None
h = ".html"
def get_env(key): return os.environ.get(key)
def get_args(key): return request.args.get(key)
a_t, crd, address, Id, result, food_list, food, data = n, n, n, n, [n,"?","?","?","?"], n, n, n

app = Flask(__name__, template_folder = "templates")
lucide = Lucide(app)

@app.route("/")
def inintial(): return render_template("home" + h, call_back_url = get_env("c_b_u"), access_token = a_t)

@app.route("/kakaocallback")
def kakaocallback():
    global a_t, Id
    a_t = run_service.get_access_token(get_args("code"), get_env("k_cli_id"), get_env("k_red_uri"))
    Id = requests.get("https://kapi.kakao.com/v2/user/me", headers = {"Authorization": f"Bearer {a_t}", "Content-Type": "application/x-www-form-urlencoded"}).json()["properties"]["nickname"]
    return render_template("kakaocallback" + h, nick_name = Id)

@app.route("/logout")
def logout():
    global a_t, crd, address, Id, result, food_list, food, data
    a_t, crd, address, Id, result, food_list, food, data = n, n, n, n, [n,"?","?","?","?"], n, n, n
    return render_template("logout" + h)

@app.route("/map")
def map(): return render_template("map" + h, java_key = get_env("k_java_key"))

@app.route("/manual")
def manual(): return render_template("manual" + h)

@app.route("/roulette")
def gatcha(): 
    global food_list, address, data
    address = run_service.get_address(get_args("lat") + ", " + get_args("lon"))
    crd = get_args("lat") + ", " + (get_args("lon"))
    data = run_service.select_menu(crd, get_env("ser_key1"), get_env("ser_key2"))
    food_list = menu_choose.menu_choose(data)
    return render_template("roulette" + h, food_list = food_list)

@app.route("/service", methods = ["Get", "Post"])
def service():
    global address, a_t, crd, data
    food = get_args("food")
    result = run_service.run_service(address, a_t, food, data)
    if address != n and a_t != n:
        if result[0] == 2: return render_template("success" + h, record = result[1], address = address, weather_data = result[2], dust = str(result[3]) + "㎍/㎥", temp = str(result[4]) + "°C", id = Id)
        else: return render_template("fail" + h)
    else: return render_template("try_again" + h)

if __name__ == "__main__":

    with open("cert.pem", "w") as certfile: certfile.write(get_env("cert_str"))
    with open("private_key.pem", "w") as keyfile: keyfile.write(get_env("pri_key_str"))
    app.run(port = 5051, ssl_context = ("cert.pem", "private_key.pem"))