import paramiko
from openpyxl.compat import range

li=['10.89.252.86','10.89.252.87','10.89.252.88','10.89.252.89','10.89.252.90','10.89.252.6']

for i in range(0,len(li)):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if li[i]!="10.88.238.39" or li[i]!="10.88.238.40":
              ssh.connect(li[i], username='hexmon', password='hetd@123')    
        else:
             ssh.connect(li[i], username='hexmon', password='hetd@123')
        sftp = ssh.open_sftp()
        sftp.put('filesystem', '/home/hexmon/filesystem')
        sftp.close()
        ssh.close()
    except:
        print("error in IPs  " + li[i])


