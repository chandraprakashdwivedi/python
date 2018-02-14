import paramiko
import xlsxwriter
import time
import re
workbook = xlsxwriter.Workbook('UCDevice_DC.xlsx')
worksheet = workbook.add_worksheet()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.88.238.4', username='monitor', password='Pkl@4321')
stdin, stdout, stderr = ssh.exec_command('sh proc')

u=stdout.readlines()
str1 = ''.join(u)

a='five minutes:'
aa='PID'
aaa=str1[(str1.index(a)+len(a)):str1.index(aa)]
print(aaa.strip())
worksheet.write('A1',aaa.strip())
ssh.close()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.88.238.5', username='monitor', password='Pkl@4321')
stdin, stdout, stderr = ssh.exec_command('sh proc')
u=stdout.readlines()
str1 = ''.join(u)

a='five minutes:'
aa='PID'
aaa=str1[(str1.index(a)+len(a)):str1.index(aa)]
print(aaa.strip())
worksheet.write('A2',aaa.strip())
ssh.close()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.88.238.132', username='monitor', password='Pkl@4321')
stdin, stdout, stderr = ssh.exec_command('sh proc')

u=stdout.readlines()
str1 = ''.join(u)

a='five minutes:'
aa='PID'
aaa=str1[(str1.index(a)+len(a)):str1.index(aa)]
print(aaa.strip())
worksheet.write('A3',aaa.strip())
ssh.close()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.88.238.133', username='monitor', password='Pkl@4321')
stdin, stdout, stderr = ssh.exec_command('sh proc')

u=stdout.readlines()
str1 = ''.join(u)

a='five minutes:'
aa='PID'
aaa=str1[(str1.index(a)+len(a)):str1.index(aa)]
print(aaa.strip())
worksheet.write('A4',aaa.strip())
ssh.close()


device = "10.88.238.16"
conn_pre = paramiko.SSHClient()
conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn_pre.connect(device, username="array", password="acer")
time.sleep(1)
conn = conn_pre.invoke_shell()
time.sleep(1)

output = []
commands = ["enable\n", "\n", "sh statistics cpu\n","sh statistic slb virtual http WebPrortal_80\n"]
for command in commands:
   conn.send(command + "\r")
   time.sleep(1)
   output.append(conn.recv(100000))
str1=''.join(str(x) for x in output)

str2=re.sub(r"\W", "", str1)
str2=str2.replace("rn","")

a='Utilization'
b='rSDCHETDWEBSLBSECrrSDCHETDWEBSLBSECbshstatisticslbvir'
c='CurrentConnectionCount'
d='TotalConnectionCount'
e='TotalPacketsIn'
f='TotalPacketsOut'
g='AverageBandwidth'
Utilization=str2[(str2.index(a)+len(a)):str2.index(b)]
Packetin=str2[(str2.index(e)+len(e)):str2.index(f)]
Packetout=str2[(str2.index(f)+len(f)):str2.index(g)]
Current=str2[(str2.index(c)+len(c)):str2.index(d)]

print(int(Utilization.strip()))
print(int(Packetin.strip()))
print(int(Packetout.strip()))
print(int(Current.strip()))

worksheet.write_number('A6',int(Utilization.strip()))
worksheet.write_number('B6',int(Packetin.strip()))
worksheet.write_number('C6',int(Packetout.strip()))
worksheet.write_number('D6',int(Current.strip()))

device = "10.88.238.61"
conn_pre = paramiko.SSHClient()
conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn_pre.connect(device, username="array", password="acer")
time.sleep(1)
conn = conn_pre.invoke_shell()
time.sleep(1)

output = []
commands = ["enable\n", "\n", "sh statistics cpu\n","sh statistic slb virtual http PSRM_6520\n","\n"]
for command in commands:
   conn.send(command + "\r")
   time.sleep(1)
   output.append(conn.recv(1000000))
   
str1=''.join(str(x) for x in output)

str2=re.sub(r"\W", "", str1)
str2=str2.replace("rn","")
print(str2)

a='Utilization'
b='rSDCHETDAPPSLBPRIrrSDCHETDAPPSLBPRIbshstatisticslbvir'
c='CurrentConnectionCount'
d='TotalConnectionCount'
e='TotalPacketsIn'
f='TotalPacketsOut'
g='MSSchosenbysy'
Utilization=str2[(str2.index(a)+len(a)):str2.index(b)]
Packetin=str2[(str2.index(e)+len(e)):str2.index(f)]
Packetout=str2[(str2.index(f)+len(f)):str2.index(g)]
Current=str2[(str2.index(c)+len(c)):str2.index(d)]

print(int(Utilization.strip()))
print(int(Packetin.strip()))
print(int(Packetout.strip()))
print(int(Current.strip()))



worksheet.write_number('A7',int(Utilization.strip()))
worksheet.write_number('B7',int(Packetin.strip()))
worksheet.write_number('C7',int(Packetout.strip()))
worksheet.write_number('D7',int(Current.strip()))


workbook.close()





