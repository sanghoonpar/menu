import os, run_service, requests, menu_choose
from flask import Flask, request, render_template
from dotenv import load_dotenv
from flask_lucide import Lucide
load_dotenv()

n = None
h = ".html"
def fetch_env(a): return os.environ.get(a)
def fetch_url(b): return request.args.get(b)
access_token, coordinate, address, Id, result, food_list, food, data = n, n, n, n, [n,"?","?","?","?"], n, n, n

app = Flask(__name__, template_folder = "templates")
lucide = Lucide(app)

@app.route("/")
def inintial():
    return render_template("home" + h, 
                           call_back_url = fetch_env("c_b_u"), 
                           access_token = access_token)

@app.route("/kakaocallback")
def kakaocallback():
    global access_token, Id
    access_token = run_service.get_access_token(fetch_url("code"), fetch_env("k_cli_id"), fetch_env("k_red_uri"))
    Id = requests.get("https://kapi.kakao.com/v2/user/me", 
                      headers = {"Authorization": f"Bearer {access_token}", 
                                 "Content-Type": "application/x-www-form-urlencoded"}).json()["properties"]["nickname"]
    return render_template("kakaocallback" + h, 
                           nick_name = Id)

@app.route("/logout")
def logout():
    global access_token, coordinate, address, Id, result, food_list, food, data
    access_token, coordinate, address, Id, result, food_list, food, data = n, n, n, n, [n,"?","?","?","?"], n, n, n
    return render_template("logout" + h)

@app.route("/map")
def map(): return render_template("map" + h, 
                                  java_key = fetch_env("k_java_key"))

@app.route("/manual")
def manual(): return render_template("manual" + h)

@app.route("/roulette")
def gatcha(): 
    global food_list, address, data
    address = run_service.get_address(fetch_url("lat") + ", " + fetch_url("lon"))
    coordinate = fetch_url("lat") + ", " + (fetch_url("lon"))
    data = run_service.select_menu(coordinate, fetch_env("ser_key1"), fetch_env("ser_key2"))
    food_list = menu_choose.menu_choose(data)
    return render_template("roulette" + h, 
                           food_list = food_list)

@app.route("/service", methods = ["Get", "Post"])
def service():
    global address, access_token, coordinate, result, food, data
    food = fetch_url("food")
    result = run_service.run_service(address, access_token, food, data)
    if address != n and access_token != n:
        if result[0] == 2: return render_template("success" + h, 
                                               record = result[1], 
                                               address = address, 
                                               weather_data = result[2], 
                                               dust = str(result[3]) + "㎍/㎥", 
                                               temp = str(result[4]) + "°C", 
                                               id = Id)
        else: return render_template("fail" + h)
    else: return render_template("try_again" + h)

if __name__ == "__main__":

    with open("cert.pem", "w") as certfile: certfile.write(fetch_env("cert_str"))
    with open("private_key.pem", "w") as keyfile: keyfile.write(fetch_env("pri_key_str"))
    app.run(port = 5051, ssl_context = ("cert.pem", "private_key.pem"))