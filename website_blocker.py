import time
from datetime import datetime as dt

#hosts_path=r"C:\Windows\System32\drivers\etc\hosts" # 'r' variable makes this path considered as a row
hosts_path="hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() <dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("working hours")
        with open(hosts_path,'r+') as file:
            content=file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines() 
            file.seek(0)    #when the file was readed the pointer is in the last line so thats why this operation is applied
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()  #when the file content is verified with for loop the pointer is before the website_list so thats why that part is truncated
        print("Fun Hours")
    time.sleep(5)
