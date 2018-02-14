import paramiko
from openpyxl.compat import range
li=['10.89.217.207','10.89.217.208','10.89.217.209']
for i in range(0,len(li)):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(li[i], username='hexmon', password='hetd#123')
    stdin,stdout,stderr = ssh.exec_command('uptime;df-h')
    a=stdout.readlines()
    output=''.join(a)  #this is done to fetch the output inside the qoutes''
    print("----------------------["+li[i]+"]--------------------------")
    print (output)
