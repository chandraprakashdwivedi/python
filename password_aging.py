import paramiko
from openpyxl.compat import range
li = ['10.88.238.39']
for i in range(0,len(li)):
    try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if li[i]!="10.88.238.39":
            ssh.connect(li[i], username='hexmon' ,password='session#123')
        else:
            ssh.connect(li[i], username='hexmon' , password='session#123')
            stdin,stdout,stderr = ssh.exec_command('echo -e "session#123 \n hetd#123 \n hetd#123" | passwd --stdin hexmon')
            print('password changed',li[i])
    except:
        print("Error in changing password:",li[i])
        
