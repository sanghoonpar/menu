from flask import Flask, redirect, url_for, request, session, render_template, make_response
import requests
import os

app = Flask(__name__)
app.secret_key = ''

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





c_b_u=https://kauth.kakao.com/oauth/authorize?client_id=173db76aadad12c9dbea268521497443&response_type=code&redirect_uri=https://capitalist-alyssa-menurecommendation-931bf3ba.koyeb.app/kakaocallback
cert_str=-----BEGIN CERTIFICATE-----
MIIDpzCCAo+gAwIBAgIUAh6tctPZ0I7yQeCpQ0nw1LtLm6swDQYJKoZIhvcNAQEL
BQAwfDELMAkGA1UEBhMCS1IxDTALBgNVBAgMBG1lZ2ExDjAMBgNVBAcMBXNlb3Vs
MQ0wCwYDVQQKDARtZWdhMQwwCgYDVQQLDANkZXYxDDAKBgNVBAMMA3BzaDEjMCEG
CSqGSIb3DQEJARYUcGFya2NzMTFzaEBnbWFpbC5jb20wHhcNMjQwMzMwMDYwNzEw
WhcNMjQwNDI5MDYwNzEwWjB8MQswCQYDVQQGEwJLUjENMAsGA1UECAwEbWVnYTEO
MAwGA1UEBwwFc2VvdWwxDTALBgNVBAoMBG1lZ2ExDDAKBgNVBAsMA2RldjEMMAoG
A1UEAwwDcHNoMSMwIQYJKoZIhvcNAQkBFhRwYXJrY3MxMXNoQGdtYWlsLmNvbTCC
ASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAOEb1ZNfhbDVvOrXyOOJxLHU
q4cZA3feuO+H4PZ9OfW7PX8z4uwsaQ5oz8JGNF+3OVCss0O06fRLVTE2418eREXO
sNVZjubu8yEbnCHGEPRzPI80MGpCVIGjhxZjlgB0FNik83o39+1bGXKppz4rmw3c
SXdUNmzEu++Jr5cmOjd1m7n10fHiDcBEvte8q4xeYYT7U3ZhxDiGD82raUQ9HuAN
3aQFvrGWrRwlFQx2WPFNcv2JDo7KgA8c0P4S9gqHZIEpgcGEr8QO5Ds10d3/rjE2
miO79GARnEaKZuRcKCqhQBFLsrHkBMG53ZL9ADQtXFyr8cArGC7s0whYmJwWb3UC
AwEAAaMhMB8wHQYDVR0OBBYEFFh3Rg+n92DOTzR4JeUsyoeW7NvpMA0GCSqGSIb3
DQEBCwUAA4IBAQBZU1HuxtG1yiRMTeM5dZKWx2lP39iFJ/xYkwOXPyXkdAdJFgnN
jIoxm00Ro9gQwV9lal5wTJSVdg1rQ27ntxe+TqZVqIW+lAIV/FYy41IqPYpDWqIB
ar3t4vv/k5zQRiyF2sURJymjcyTVUo+nTVXL96jLrxi4eO9PZ+fgHkk/WwUckhsT
ZP1FKSLrIfEKlUgxCDzwDLDm6YPr0joF3WrTc/f7YMjBfLRKFtQe5SGV9wIAXpv2
8Oej5v9ez5EaX1CjuQkkRO5GpPAyFMG/ogECLV7LS+1qjJguDiWj6pUmqf4VUT8H
V4iFFVbRu4gk7P8rtOXD2XaXYfIbP7gf/nL8
-----END CERTIFICATE-----
k_cli_id=173db76aadad12c9dbea268521497443
k_java_key=048fa658b64039a2161416b741dcd27c
k_red_uri=https://capitalist-alyssa-menurecommendation-931bf3ba.koyeb.app/kakaocallback
n_cli_id=1IdrYpXU82R5qOzxvLgY
n_cli_secret=KDxHRPJGEM
pri_key_str=-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDhG9WTX4Ww1bzq
18jjicSx1KuHGQN33rjvh+D2fTn1uz1/M+LsLGkOaM/CRjRftzlQrLNDtOn0S1Ux
NuNfHkRFzrDVWY7m7vMhG5whxhD0czyPNDBqQlSBo4cWY5YAdBTYpPN6N/ftWxly
qac+K5sN3El3VDZsxLvvia+XJjo3dZu59dHx4g3ARL7XvKuMXmGE+1N2YcQ4hg/N
q2lEPR7gDd2kBb6xlq0cJRUMdljxTXL9iQ6OyoAPHND+EvYKh2SBKYHBhK/EDuQ7
NdHd/64xNpoju/RgEZxGimbkXCgqoUARS7Kx5ATBud2S/QA0LVxcq/HAKxgu7NMI
WJicFm91AgMBAAECggEAHSgWRzLZpZhhkkdlwTcAb4oct3Bhdx61dGz0keiRX8cj
RX0KeM2dw9yGgGLIeNdKCK19wJjHrrktLSUvWQwaCrKlS9UAQeAURKcHV4aIfqkI
YIIBfVnfCTWNkzRN4vwmERN4Z82lAqzIhIX93/sU57wvFdImBHuM3g9G23x7kOAg
GtffK3A0WpwbXillfNFeX4ktb/8+zNkzy7tIkZ1TLvO3rpW+3NPqXr3wsw9qsa+L
Ip/p/zjueq76+PRH6do+iK69pETcTeSIH0WE+wHy2mi8NHyf1cy2tLNzpWpWQl/M
y5tQ+B7iGA+bmfeHfndEjWGQVip2i4zNvxzBknE9BwKBgQD1CdgJfydnxXeL9M2/
2vZ15oVx0kWE+q2PW+r3TSvu4l9VmQo0T6+7Prg73eba93GckuoPTNSCvt4dhLVs
M3yR+NChRNbYWg0gWXopqCRNIDSYXo+Rk+eMH5NczYguNRHGq3JYSnHRf5PPkNWm
GKHXmwAmivoQ7z0h28pPjjd9JwKBgQDrLcHUWfUtVh9du8eW7Rvimr/cY2KB29iD
MNVSIszTCMSadelbSa0vdXWr5iGplQBws7lC7dnkDWKGTHeGIGIDjq/vP9G6UZGD
1MaU9+2/9tuYwHVvYDnKYhnYzJfw1HWy3ho8nARIAlPI/RFtj1h1s/Xmz5f/e4pR
G1mu9/tIAwKBgAwSsRc+sZVWUF6P8Dc8tZn3gqmp/4zewQBoOfp3TevWMXZJNQyA
xJrIK1GfzEkLmghp4KhiU7Ihb1Yq/LlZDBExHi5j8uX0AeOPJQq6Yxd9t7muJwq4
K9dmkt8mrUgBi1+rgNXCzTrSO1klvLETU54I4AgGHu4Iq41og95JlohPAoGBAKdA
k2iB0Wu8o/H1aaxcVEiD5Y7G33ea8g/a2trfBOvQgIGY+ayCaTgnQNhPggEohneg
WVDP9vXIzxjTqO0qeootH9H2gSEQgXxQBipLaDntRZ8MwHfE51SXD+qvFh+f+VSL
v/z6t9C+VvfJgmt4VmDe6zKK0H5RTb0Axnc4xOwhAoGAcf4cJOUVQwO2CaKgU62s
n8yDdTboaRz5l+UxsvjLQ/wR3W3T1tNyksVjvWv1t4HoxYRN2815BLisrmn90lY+
dop8x+l/SdI9ORyYRSncU6doyEqc+eOj5DIs+ZrC4ZARkitgbjI1heTGyyVUgv4o
A3+/YPUjMuNhN0Yu5DupFIQ=
-----END PRIVATE KEY-----
ser_key=9v0QBhawFaMJQYwaCRCBfo%2Fw12RUXAH2TKoDjmpVOd6%2F9AZDCma4CNhQCRc99JRPzaiJPKw8jEhA%2BhntEWS0Rw%3D%3D