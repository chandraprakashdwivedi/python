import paramiko ,time

device = "10.24.104.5"
conn_pre = paramiko.SSHClient()
conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn_pre.connect(device, username="admin", password="pasword")
conn = conn_pre.invoke_shell()

output=[]

commands = ["shell\n", "ts_menu"]
for command in commands:
   conn.send(command + "\r")
   time.sleep(1)
   output.append(conn.recv(100000))
str1=''.join(str(x) for x in output)

commands1 = [input('1-8: '),input('option pass: '),input('enter'),input('enter'),input('enter'),input('your user name'),input('your password')]
for command in commands1:
   conn.send(command + "\r")
   time.sleep(3)
   output.append(conn.recv(100000))
str2=''.join(str(x) for x in output)

print(str1)
print(str2)
