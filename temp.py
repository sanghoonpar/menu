from flask import Flask, redirect, url_for, request, session, render_template, flash, make_response
import requests
import os

app = Flask(__name__)
app.secret_key = 'tkdgns5568?'

@app.route('/')
def home():
    user = session.get('user')
    if user: return render_template('home.html', user=user)
    user_id = request.cookies.get('user_id')
    if user_id:
        user = get_user_from_db(user_id)
        if user:
            session['user'] = user
            return render_template('home.html', user = user)
    return render_template('home.html', user = None)

@app.route('/login')
def login(): return redirect(f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={os.environ.get('k_cli_id')}&redirect_uri={os.environ.get('k_red_uri')}")

@app.route('/logout')
def logout():
    session.pop('user', None)
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('user_id', '', expires = 0)
    return resp

@app.route('/oauth')
def oauth():

    user_info = requests.get('https://kapi.kakao.com/v2/user/me', headers = {'Authorization': f'Bearer {requests.post('https://kauth.kakao.com/oauth/token', data = {'grant_type': 'authorization_code', 'client_id': os.environ.get('k_cli_id'), 'redirect_uri': os.environ.get('k_red_uri'), 'code': request.args.get('code'),}, headers = {'Content-Type': 'application/x-www-form-urlencoded',}).json().get('access_token')}','Content-Type': 'application/x-www-form-urlencoded',}).json()

    user_id = user_info['id']
    user_data = {'id': user_id, 'nickname': user_info['properties']['nickname'],}

    save_user_to_db(user_data)

    session['user'] = user_data
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('user_id', str(user_id), max_age = 30 * 24 * 60 * 60)
    return resp

def save_user_to_db(user):
    # 여기에 사용자 정보를 데이터베이스에 저장하는 코드를 추가하세요.
    pass

def get_user_from_db(user_id):
    # 여기에 사용자 정보를 데이터베이스에서 가져오는 코드를 추가하세요.
    # 예시로 임시 사용자 데이터 반환
    return {'id': user_id, 'nickname': 'TempUser'}

if __name__ == '__main__':
    app.run(debug=True)
