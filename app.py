import webbrowser, os, run_service, requests
from flask import Flask, render_template, request, session, url_for, redirect, flash, make_response
from dotenv import load_dotenv
load_dotenv()

access_token, crd, address = None, None, None

app = Flask(__name__, template_folder = 'templates')
app.secret_key = os.environ.get('sec_key')

@app.route('/')
def inintial(): 

    if session.get('user'):
        return render_template('home.html', user = session.get('user'))
    if request.cookies.get('user_id'):
        if get_user_from_db(request.cookies.get('user_id')):
            session['user'] = get_user_from_db(request.cookies.get('user_id'))
            return render_template('home.html', user = get_user_from_db(request.cookies.get('user_id')))
    return render_template('home.html', user = None)

@app.route('/login')
def login(): return redirect(os.environ.get('c_b_u2'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('user_id', '', expires = 0)
    return resp

@app.route('/main')
def login():
    global crd, address

    if request.method == 'GET':
        if request.args.get('lat') != None and request.args.get('lon') != None:
            address = run_service.get_address(request.args.get('lat') + ', ' + request.args.get('lon'))
            crd = request.args.get('lat') + ', ' + request.args.get('lon')

    elif request.method == 'POST': webbrowser.open(os.environ.get('c_b_u'))

    if access_token != None: key = 0
    else: key = 1

    return render_template('main.html', c_b_u = os.environ.get('c_b_u'), key = key)

@app.route('/kakaocallback')
def kakaocallback():
    global access_token

    access_token = run_service.get_token(request.args.get('code'), os.environ.get('k_cli_id'), os.environ.get('k_red_uri'))
    
    user_info = requests.get('https://kapi.kakao.com/v2/user/me', headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/x-www-form-urlencoded',}).json()
    user_infor = {'id': user_info['id'], 'nickname': user_info['properties']['nickname'],}
    user_inform = save_user_to_db(user_infor)

    session['user'] = user_infor
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('user_id', str(user_info['id']), max_age = 30 * 24 * 60 * 60)
    return render_template('kakaocallback.html', nick_name = user_info['properties']['nickname'], resp = resp)

@app.route('/k_logout')
def logout():
    global access_token
    
    access_token = None
    return login()

@app.route('/map')
def map(): return render_template('map.html', java_key = os.environ.get('k_java_key'))

@app.route('/manual')
def manual(): return render_template('manual.html')

@app.route('/service')
def service():
    
    global address, access_token, crd
    if address != None and access_token != None:    
        if run_service.serve_code(address, access_token, crd) == 1: return render_template('success.html')
        else: return render_template('fail.html')
    else: return render_template('try_again.html')

def save_user_to_db(user):
    user_inform = {}
    user_inform[user['id']] = user['id'], user['nickname']
    return user_inform

def get_user_from_db(user_id, user_inform):
    nick = user_inform[user_id]['nickname']
    return {'id': user_id, 'nickname': nick}

if __name__ == '__main__':
    with open('cert.pem', 'w') as certfile: certfile.write(os.environ.get('cert_str'))
    with open('private_key.pem', 'w') as keyfile: keyfile.write(os.environ.get('pri_key_str'))

    app.run(port = 5051, ssl_context = ('cert.pem', 'private_key.pem'))