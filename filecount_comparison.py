---
create a Bash script which update the file count 
---
import paramiko
from openpyxl.compat import range

li=['10.88.238.71']

for i in range(0,len(li)):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(li[i], username='hexmon', password='wipro@123')
        stdin, stdout, stderr = ssh.exec_command('ls /home/hexmon | wc -l ')
        a,b,c = ssh.exec_command('ls /home/hexmon | wc -l >> output.txt')
        u=stdout.readlines()
        output = ''.join(u)
        with open("output.txt","a+") as file:
    
        print(output)
    except:
        print("error in IPs  " + li[i])


