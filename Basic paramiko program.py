import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.89.217.207', username='hexmon', password='hetd#123')
stdin,stdout,stderr = ssh.exec_command('uptime')
a=stdout.readlines()
output=''.join(a)  #this is done to fetch the output inside the qoutes''
print (output)

             
