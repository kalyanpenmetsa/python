import requests
import json
import getpass

BASE_URL='https://www.instagram.com/'
LOGIN_URL= BASE_URL + 'accounts/login/ajax/'
USERNAME= 'ven1376'
PASSWD= getpass.getpass("Enter IG password: ")
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
session = requests.Session()
session.headers = {'user-agent': USER_AGENT}
session.headers.update({'Referer': BASE_URL})

req = session.get(BASE_URL)
session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})
login_data = {'username': USERNAME, 'password': PASSWD}
login = session.post(LOGIN_URL, data=login_data, allow_redirects=True)
session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
cookies = login.cookies
login_text = json.loads(login.text)

print(login.text)

