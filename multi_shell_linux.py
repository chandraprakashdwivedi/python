import paramiko ,time


device = "192.168.2.4"

conn_pre = paramiko.SSHClient()

conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

conn_pre.connect(device, username="root", password="redhat")

conn = conn_pre.invoke_shell()

output=[]

commands = [ "ssh root@192.168.2.5\n"]

for command in commands:

   conn.send(command + "\r")

    
commands1 = ['\n', 'user1' , 'abc@123']

for command in commands1:

   conn.send(command + "\r")
   time.sleep(1)

 
commands2 = ['nc -vz google.com 80']

for command in commands2:

   conn.send(command + "\r")

   time.sleep(1)

   output.append(conn.recv(100000))

str1=''.join(str(x) for x in output)
a='80 port [tcp/http]'
c=str1[(str1.index(a)+len(a)):]
if "succeeded!" in c:
   print("CDN working")



