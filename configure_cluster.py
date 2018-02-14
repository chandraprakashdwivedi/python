#Script used to crerate cluster nodes
import paramiko
from openpyxl.compat import range
li=['192.168.2.11']
for i in range(0,len(li)):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(li[i], username='root', password='redhat')
    stdin,stdout,stderr = ssh.exec_command('echo -e "redhat" |pcs cluster auth --stdin clusternode1 clusternode2 -u hacluster')
    stdin,stdout,stderr = ssh.exec_command('pcs cluster setup --name mycluster clusternode1 clusternode2')
    stdin,stdout,stderr = ssh.exec_command('pcs resource create virtip ipaddr ip=192.168.2.100 cidr_netmask=24 op monitor interval=30s')
    stdin,stdout,stderr = ssh.exec_command('pcs resource create httpd apache configfile="/etc/httpd/conf/httpd.conf" op monitor interval=30s')
    stdin,stdout,stderr = ssh.exec_command('pcs constraint colocation add httpd with virtip INFINITY')
    stdin,stdout,stderr = ssh.exec_command('pcs property set stonith-enabled=false ')
    stdin,stdout,stderr = ssh.exec_command('pcs property set no-qouram-policy=ignore')
    stdin,stdout,stderr = ssh.exec_command('pcs property set default-resource-stickiness="INFINITY"')
    stdin,stdout,stderr = ssh.exec_command('systemctl start pcsd && systemctl enable pcsd')
    stdin,stdout,stderr = ssh.exec_command('')
    stdin,stdout,stderr = ssh.exec_command('')
    
    print("----------------------["+li[i]+"]--------------------------")
print ("task completed")
