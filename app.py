import webbrowser, os, run_service, requests
from flask import Flask, render_template, request, session, url_for, redirect
from dotenv import load_dotenv
load_dotenv()

access_token, crd, address = None, None, None

app = Flask(__name__, template_folder = 'templates')
app.secret_key = os.environ.get('sec_key')
user = {}

@app.route('/')
def inintial(): return render_template('home.html')

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
def login():
    global crd, address

    if request.method == 'GET':
        if request.args.get('lat') != None and request.args.get('lon') != None:
            address = run_service.get_address(request.args.get('lat') + ', ' + request.args.get('lon'))
            crd = request.args.get('lat') + ', ' + request.args.get('lon')

    elif request.method == 'POST': webbrowser.open(os.environ.get('c_b_u'))
    
    if access_token != None: key = 0
    else: key = 1

    if crd != None: key1 = 0
    else: key1 = 1

    return render_template('main.html', c_b_u = os.environ.get('c_b_u'), key = key, key1 = key1)

@app.route('/kakaocallback')
def kakaocallback():
    global access_token

    access_token = run_service.get_token(request.args.get('code'), os.environ.get('k_cli_id'), os.environ.get('k_red_uri'))
    
    user_info = requests.get('https://kapi.kakao.com/v2/user/me', headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/x-www-form-urlencoded',}).json()

    # session['username'] = username

    # if 'username' in session: 
    #    username = session['username']
    #    return render_template('main.html', user = f'로그인 완료 {username}님')
    


    return render_template('kakaocallback.html', nick_name = user_info['properties']['nickname'])

@app.route('/k_logout')
def logout():
    global access_token, crd, address

    access_token, crd, address = None, None, None
    return render_template('home.html')
   # session.pop('user', None)
    #return redirect(url_for('index')), login()

@app.route('/map')
def map(): return render_template('map.html', java_key = os.environ.get('k_java_key'))

@app.route('/manual')
def manual(): return render_template('manual.html')

@app.route('/service')
def service():
    
    global address, access_token, crd
    if address != None and access_token != None:
        if run_service.serve_code(address, access_token, crd) == 2: return render_template('success.html')
        else: return render_template('fail.html')
    else: return render_template('try_again.html')

if __name__ == '__main__':
    with open('cert.pem', 'w') as certfile: certfile.write(os.environ.get('cert_str'))
    with open('private_key.pem', 'w') as keyfile: keyfile.write(os.environ.get('pri_key_str'))

    app.run(port = 5051, ssl_context = ('cert.pem', 'private_key.pem'))