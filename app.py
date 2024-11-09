import os, run_service, requests, menu_choose
from flask import Flask, request, render_template
from dotenv import load_dotenv
from flask_lucide import Lucide
load_dotenv()

n = None
h = ".html"
def fetch_env(a): return os.environ.get(a)
def fetch_url(b): return request.args.get(b)
a_t, crd, ad, Id, dat, f_l, food, weat = n, n, n, n, [n,"?","?","?","?"], n, n, n

app = Flask(__name__, template_folder = "templates")
lucide = Lucide(app)

@app.route("/")
def inintial():
    if a_t != n: key = 0
    else: key = 1

    if crd != n: key1 = 0
    else: key1 = 1
    return render_template("home" + h, 
                           c_b_u = fetch_env("c_b_u"), 
                           key = key, 
                           key1 = key1, 
                           a = a_t)

@app.route("/kakaocallback")
def kakaocallback():
    global a_t, Id
    a_t = run_service.get_access_token(fetch_url("code"), fetch_env("k_cli_id"), fetch_env("k_red_uri"))
    Id = requests.get("https://kapi.kakao.com/v2/user/me", 
                      headers = {"Authorization": f"Bearer {a_t}", 
                                 "Content-Type": "application/x-www-form-urlencoded"}).json()["properties"]["nickname"]
    return render_template("kakaocallback" + h, 
                           nick_name = Id)

@app.route("/logout")
def logout():
    global a_t, crd, ad, Id, dat, f_l, food, weat
    a_t, crd, ad, Id, dat, f_l, food, weat = n, n, n, n, [n,"?","?","?","?"], n, n, n
    return render_template("lo" + h)

@app.route("/map")
def map(): return render_template("map" + h, 
                                  java_key = fetch_env("k_java_key"))

@app.route("/manual")
def manual(): return render_template("manual" + h)

@app.route("/roulette")
def gatcha(): 
    global f_l, ad, weat
    ad = run_service.get_address(fetch_url("lat") + ", " + fetch_url("lon"))
    crd = fetch_url("lat") + ", " + (fetch_url("lon"))
    weat = run_service.select_menu(crd, fetch_env("ser_key1"), fetch_env("ser_key2"))
    f_l = menu_choose.menu_choose(weat)
    return render_template("roulette" + h, 
                           f_l = f_l)

@app.route("/service", methods = ["Get", "Post"])
def service():
    global ad, a_t, crd, dat, food, weat
    food = fetch_url("food")
    dat = run_service.run_service(ad, a_t, food, weat)
    if ad != n and a_t != n:
        if dat[0] == 2: return render_template("success" + h, 
                                               rec = dat[1], 
                                               ad = ad, 
                                               wea = dat[2], 
                                               dust = str(dat[3]) + "㎍/㎥", 
                                               temp = str(dat[4]) + "°C", 
                                               id = Id)
        else: return render_template("fail" + h)
    else: return render_template("try_again" + h)

if __name__ == "__main__":

    with open("cert.pem", "w") as certfile: certfile.write(fetch_env("cert_str"))
    with open("private_key.pem", "w") as keyfile: keyfile.write(fetch_env("pri_key_str"))
    app.run(port = 5051, ssl_context = ("cert.pem", "private_key.pem"))