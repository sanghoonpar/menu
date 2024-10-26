import os, run_service, requests, menu_choose
from flask import Flask, request, render_template
from dotenv import load_dotenv
from flask_lucide import Lucide
load_dotenv()

n = None
h = '.html'
def o(a): return os.environ.get(a)
def a(b): return request.args.get(b)
a_t, crd, ad, Id, dat, f_l, food, weat = n, n, n, n, [n,'?','?','?','?'], n, n, n

app = Flask(__name__, template_folder = 'templates')
lucide = Lucide(app)

@app.route('/')
def inintial():
    if a_t != n: key = 0
    else: key = 1

    if crd != n: key1 = 0
    else: key1 = 1
    return render_template('home' + h, c_b_u = o('c_b_u'), key = key, key1 = key1, a = a_t)

@app.route('/kakaocallback')
def kakaocallback():
    global a_t, Id
    a_t = run_service.g_t(a('code'), o('k_cli_id'), o('k_red_uri'))
    Id = requests.get('https://kapi.kakao.com/v2/user/me', headers = {'Authorization': f'Bearer {a_t}', 'Content-Type': 'application/x-www-form-urlencoded',}).json()['properties']['nickname']
    return render_template('kakaocallback' + h, nick_name = Id)

@app.route('/logout')
def logout():
    global a_t, crd, ad, Id, dat, f_l, food, weat
    a_t, crd, ad, Id, dat, f_l, food, weat = n, n, n, n, [n,'?','?','?','?'], n, n, n
    return render_template('lo' + h)

@app.route('/map')
def map(): return render_template('map' + h, java_key = o('k_java_key'))

@app.route('/manual')
def manual(): return render_template('manual' + h)


@app.route('/roulette')
def gatcha(): 
    global f_l, ad, weat
    ad = run_service.g_a(a('lat') + ', ' + a('lon'))
    crd = a('lat') + ', ' + (a('lon'))
    weat = run_service.weat(crd, o('ser_key1'), o('ser_key2'))
    f_l = menu_choose.m_c(weat)
    return render_template('roulette' + h, f_l = f_l)

@app.route('/service', methods = ['Get', 'Post'])
def service():
    global ad, a_t, crd, dat, food, weat
    food = a('food')
    dat = run_service.s_c(ad, a_t, food, weat)
    if ad != n and a_t != n:
        if dat[0] == 2: return render_template('success' + h, rec = dat[1], ad = ad, wea = dat[2], dust = str(dat[3]) + '㎍/㎥', temp = str(dat[4]) + '°C', id = Id)
        else: return render_template('fail' + h)
    else: return render_template('try_again' + h)

if __name__ == '__main__':

    with open('cert.pem', 'w') as certfile: certfile.write(o('cert_str'))
    with open('private_key.pem', 'w') as keyfile: keyfile.write(o('pri_key_str'))
    app.run(port = 5051, ssl_context = ('cert.pem', 'private_key.pem'))