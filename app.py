import os, run_service, requests
from flask import Flask, request, render_template#, session, url_for, redirect
from dotenv import load_dotenv
from flask_lucide import Lucide
load_dotenv()

n = None
h = '.html'
a_t, crd, ad, alle, Id, dat, food = n, n, n, n, n, [n,'?','?','?','?'], n

app = Flask(__name__, template_folder = 'templates')
lucide = Lucide(app)
app.secret_key = os.environ.get('sec_key')
user = {}

@app.route('/')
def inintial():
    
    if a_t != n: key = 0
    else: key = 1

    if crd != n: key1 = 0
    else: key1 = 1
    
    return render_template('home.html', c_b_u = os.environ.get('c_b_u'), key = key, key1 = key1)

# @app.route('/make_cookie', methods=['POST'])
# def make_cookie(): 
#     username = request.form['username']
#     password = request.form['password']    
#     if username in user and user[username]['password'] == password:
#        session['username'] = username

#     if 'username' in session: 
#        username = session['username']
#        return render_template('home.html', user = f'로그인 완료 {username}님')
    
#     return render_template('home.html', user = '로그인 실패')

@app.route('/main')
def login(): return render_template('main' + h)

@app.route('/kakaocallback')
def kakaocallback():
    global a_t, Id

    a_t = run_service.g_t(request.args.get('code'), os.environ.get('k_cli_id'), os.environ.get('k_red_uri'))
    
    user_info = requests.get('https://kapi.kakao.com/v2/user/me', headers = {'Authorization': f'Bearer {a_t}', 'Content-Type': 'application/x-www-form-urlencoded',}).json()
    # session['username'] = username

    # if 'username' in session: 
    #    username = session['username']
    #    return render_template('main.html', user = f'로그인 완료 {username}님')
    Id = user_info['properties']['nickname']
    return render_template('kakaocallback' + h, nick_name = Id)

@app.route('/logout')
def logout():
    global a_t, crd, ad, Id, dat, alle, food

    a_t, crd, ad, Id, dat, alle = n, n, n, n, [n,'?','?','?','?'], n
    return render_template('lo' + h)
    #session.pop('user', None)
    #return redirect(url_for('index')), login()

@app.route('/map')
def map(): return render_template('map' + h, java_key = os.environ.get('k_java_key'))

@app.route('/user')
def user(): return render_template('user' + h, alle = alle, id = Id, rec = dat[1], ad = ad, wea = dat[2], dust = str(dat[3]) + '㎍/㎥', temp = str(dat[4]) + '°C')

@app.route('/alle')
def al(): return render_template('alle' + h)

@app.route('/manual')
def manual(): return render_template('manual' + h)

@app.route('/select_menu', methods = ['Get', 'Post'])
def select():

    global ad, crd
    if request.method == 'GET':
        if request.args.get('lat') != n and request.args.get('lon') != n:
            ad = run_service.g_a(request.args.get('lat') + ', ' + request.args.get('lon'))
            crd = request.args.get('lat') + ', ' + request.args.get('lon')
    return render_template('roulette' + h)

@app.route('/service', methods = ['Get', 'Post'])
def service():
    
    global ad, a_t, crd, alle, dat, food

    food = request.args.get('food')
    dat = run_service.serve_code1(ad, a_t, food, crd)

    if ad != n and a_t != n:
        if dat[0] == 2: return render_template('success' + h)
        else: return render_template('fail' + h)
    else: return render_template('try_again' + h)

if __name__ == '__main__':
    with open('cert.pem', 'w') as certfile: certfile.write(os.environ.get('cert_str'))
    with open('private_key.pem', 'w') as keyfile: keyfile.write(os.environ.get('pri_key_str'))
    app.run(port = 5051, ssl_context = ('cert.pem', 'private_key.pem'))