#Script used to create cluster nodes
import paramiko
from openpyxl.compat import range
li=['192.168.2.11']
for i in range(0,len(li)):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(li[i], username='root', password='redhat')
    stdin,stdout,stderr = ssh.exec_command('echo "clusternode1.example.com" > /etc/hostname')  #set cluster hostname manually
    stdin,stdout,stderr = ssh.exec_command('echo "192.168.2.11  clusternode1.example.com clusternode1" >> /etc/hosts')  #set hosts manualy
    stdin,stdout,stderr = ssh.exec_command('echo "192.168.2.12  clusternode2.example.com clusternode2" >> /etc/hosts')
    stdin,stdout,stderr = ssh.exec_command('echo "192.168.2.22  clusterstorage.example.com clusterstorage" >> /etc/hosts')
    stdin,stdout,stderr = ssh.exec_command('systemctl stop firewalld && systemctl disable firewalld;sed -ie "s/enforcing/disabled/g" /etc/selinux/config')
    stdin,stdout,stderr = ssh.exec_command('echo -e "[yum] \nname=yum server \nbaseurl=ftp://192.168.2.22/pub/Pacakages \nenabled=1 \ngpgcheck=0" > /etc/yum.repos.d/yum.repo')
    stdin,stdout,stderr = ssh.exec_command('echo -e "\n\n[addons] \nname=yum addon \nbaseurl=ftp://192.168.2.22/pub/addons/HighAvailability \nenabled=1 \ngpgcheck=0" > /etc/yum.repos.d/yum.repo')
    stdin,stdout,stderr = ssh.exec_command('yum install http* -y;systemctl start httpd && systemctl enable httpd')
    stdin,stdout,stderr = ssh.exec_command('echo "Test page from cluster node1" > /var/www/html/index.html') 
    stdin,stdout,stderr = ssh.exec_command('mount -t nfs 192.168.2.22:/shared    /var/www/html')
    stdin,stdout,stderr = ssh.exec_command('echo "192.168.2.22:/shared  /var/www  nfs 0 0 " >> /etc/fstab')
    stdin,stdout,stderr = ssh.exec_command('systemctl stop NetworkManager && systemctl disable NetworkManager;systemctl enable network')
    stdin,stdout,stderr = ssh.exec_command('yum install pacemaker pcs fence-agents all -y')
    stdin,stdout,stderr = ssh.exec_command('echo -e "redhat \n redhat" | passwd --stdin hacluster')

    print("----------------------["+li[i]+"]--------------------------")
print ("task completed")
