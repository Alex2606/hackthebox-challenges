import requests
import hashlib
from bs4 import BeautifulSoup

url = 'http://docker.hackthebox.eu:32675/'
session = requests.session()
get_req = session.get(url).text
source = BeautifulSoup(get_req, 'html.parser')
initial_md5 = source.find('h3').text
encrypted_md5 = hashlib.md5(word.encode()).hexdigest()
data = {'hash': encrypted_md5}
post_req = session.post(url, data = data).text
source = BeautifulSoup(post_req, 'html.parser')
flag = source.find('p').text
print(flag)

