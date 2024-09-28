<<<<<<< HEAD
import os, run_service, requests, menu_choose
=======
import os, run_service, requests
>>>>>>> origin/main
from flask import Flask, request, render_template
from dotenv import load_dotenv
from flask_lucide import Lucide
load_dotenv()

n = None
h = '.html'
a_t, crd, ad, Id, dat, food = n, n, n, n, [n,'?','?','?','?'], n

app = Flask(__name__, template_folder = 'templates')
lucide = Lucide(app)
user = {}

@app.route('/')
def inintial():
    
    if a_t != n: key = 0
    else: key = 1

    if crd != n: key1 = 0
    else: key1 = 1
    return render_template('home.html', c_b_u = os.environ.get('c_b_u'), key = key, key1 = key1, a = a_t)
<<<<<<< HEAD
=======

@app.route('/main')
def login(): return render_template('main' + h)
>>>>>>> origin/main

@app.route('/kakaocallback')
def kakaocallback():
    global a_t, Id

    a_t = run_service.g_t(request.args.get('code'), os.environ.get('k_cli_id'), os.environ.get('k_red_uri'))
    
    user_info = requests.get('https://kapi.kakao.com/v2/user/me', headers = {'Authorization': f'Bearer {a_t}', 'Content-Type': 'application/x-www-form-urlencoded',}).json()

    Id = user_info['properties']['nickname']
    return render_template('kakaocallback' + h, nick_name = Id)

@app.route('/logout')
def logout():
    global a_t, crd, ad, Id, dat, food

<<<<<<< HEAD
    a_t, crd, ad, Id, dat = n, n, n, n, [n,'?','?','?','?']
=======
<<<<<<< HEAD
    a_t, crd, ad, Id, dat = n, n, n, n, [n,'?','?','?','?']
=======
    a_t, crd, ad, Id, dat, alle = n, n, n, n, [n,'?','?','?','?'], n
>>>>>>> origin/main
>>>>>>> 9981c73c5a82b5eba295c67f006e6e4fa3185d73
    return render_template('lo' + h)

@app.route('/map')
def map(): return render_template('map' + h, java_key = os.environ.get('k_java_key'))

@app.route('/manual')
def manual(): return render_template('manual' + h)

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 9981c73c5a82b5eba295c67f006e6e4fa3185d73
@app.route('/choose')
def choose():

    global ad, crd, f_l, weat
    ad = run_service.g_a(request.args.get('lat') + ', ' + request.args.get('lon'))
    crd = request.args.get('lat') + ', ' + request.args.get('lon')
    weat = run_service.weat(crd, os.environ.get('ser_key'))
    f_l = menu_choose.m_c(weat)
    print(f_l)
    return render_template('choose' + h)

@app.route('/select_menu')
def select(): return render_template('select_menu' + h, f_l = f_l)

@app.route('/roulette')
def gacha(): return render_template('roulette' + h, f_l = f_l)
=======
@app.route('/choose', methods = ['Get', 'Post'])
def choose():

    global ad, crd, weat
    if request.method == 'GET':
        if request.args.get('lat') != n and request.args.get('lon') != n:
            ad = run_service.g_a(request.args.get('lat') + ', ' + request.args.get('lon'))
            crd = request.args.get('lat') + ', ' + request.args.get('lon')
    weat = run_service.weat(crd, os.environ.get('ser_key'))
    return render_template('choose' + h)

@app.route('/select_menu')
def select(): return render_template('select_menu' + h)

@app.route('/roulette')
def gacha(): return render_template('roulette' + h)
>>>>>>> origin/main

@app.route('/service', methods = ['Get', 'Post'])
def service():
    
    global ad, a_t, crd, dat, food, weat

    food = request.args.get('food')
<<<<<<< HEAD
    dat = run_service.s_c(ad, a_t, food, weat)
=======
    dat = run_service.s_c1(ad, a_t, food, weat)

>>>>>>> origin/main
    if ad != n and a_t != n:
        if dat[0] == 2: return render_template('success' + h, rec = dat[1], ad = ad, wea = dat[2], dust = str(dat[3]) + '㎍/㎥', temp = str(dat[4]) + '°C', id = Id)
        else: return render_template('fail' + h)
    else: return render_template('try_again' + h)

if __name__ == '__main__':
<<<<<<< HEAD
    #app.debug = True
=======
    app.debug = True
>>>>>>> 9981c73c5a82b5eba295c67f006e6e4fa3185d73
    with open('cert.pem', 'w') as certfile: certfile.write(os.environ.get('cert_str'))
    with open('private_key.pem', 'w') as keyfile: keyfile.write(os.environ.get('pri_key_str'))
    app.run(port = 5051, ssl_context = ('cert.pem', 'private_key.pem'))