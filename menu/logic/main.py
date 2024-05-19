import webbrowser, os, run_service, requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
load_dotenv()

access_token, crd, address, allergy = None, None, None, None

#Flask 인스턴스 생성 및 템플릿 폴더 설정
app = Flask(__name__, template_folder = 'templates')

@app.route('/', methods = ['GET', 'POST'])
def inintial():
    return render_template('home.html')

@app.route('/main')
def login():
    global crd, address
    if request.method == 'GET':
        if request.args.get('lat') != None and request.args.get('lon') != None:
            address = run_service.get_address(request.args.get('lat') + ', ' + request.args.get('lon'))
            crd = request.args.get('lat') + ', ' + request.args.get('lon')
            
            if access_token != None:
                return service()
    
    elif request.method == 'POST':
        webbrowser.open(os.environ.get('call_back_url'))
    
    if access_token != None:
        key = 0
    else:
        key = 1

    return render_template('main.html', call_back_url = os.environ.get('call_back_url'), key = key)

@app.route('/kakaocallback')
def kakaocallback():
    global access_token
    #URL에서 'code' 파라미터 추출
    access_token = run_service.get_token(request.args.get('code'), os.environ.get('k_client_id'), os.environ.get('k_redirect_uri'))

    if address != None:
        return service()

    #액세스 토큰 요청
    return render_template('kakaocallback.html', nick_name = requests.get('https://kapi.kakao.com/v2/user/me', headers = {'Authorization': f"Bearer {access_token}"}).json()['properties']['nickname'])
@app.route('/logout')
def logout():
    global access_token
    access_token = None
    return login()

@app.route('/map')
def map():
    return render_template('map.html', java_key = os.environ.get('k_java_key'))

@app.route('/allergy', methods = ['GET', 'POST'])
def allergy():
    global allergy
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        allergy = request.form.getlist('allergy')
        print('allergy :', allergy)

    return render_template('allergy.html')

def service():
    #함수호출
    if run_service.serve_code(address, access_token, crd) == 2:
        return render_template('success.html')
    else:
        return render_template('fail.html')

#서버 실행
if __name__ == '__main__':
    app.run(port = 5051, ssl_context = ('ssl/self_signed_certificate.pem', 'ssl/private_key.pem'))