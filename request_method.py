import requests
from bs4 import BeautifulSoup
import datetime
import smtplib
import getpass

USERNAME=input('Username: ')
PASSWORD=getpass.getpass(prompt="Password: ")
    

try:
    login_data =  {'username':USERNAME, 'password':PASSWORD}
    url='https://google.com'
    s = requests.Session()
    data=s.get(url)
    header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    cookie=data.cookies.get_dict()
    
    status=s.post(url,data=login_data,headers=header,cookies=cookie)
    #response=s.get(url,allow_redirects=False, stream=True)
    #con=response.content
    #soup=BeautifulSoup(con,"html.parser")
    print(status)
    
except :
    print('exception')
    


