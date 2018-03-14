import hpilo,sys
import getpass

host=input('host: ')

USERNAME=input('Username: ')
PASSWORD=getpass.getpass(prompt="Password: ")

try:
    ilo=hpilo.Ilo(host, USERNAME, PASSWORD,delayed=False)
    health=ilo.get_embedded_health()
    print(' \n------------------------------------\n')
    print("BIOS: "+ health['health_at_a_glance']['bios_hardware']['status'])
    print("FANS: "+ health['health_at_a_glance']['fans']['status'])
    print("MEMORY: "+ health['health_at_a_glance']['memory']['status'])
    print("NETWORK: "+ health['health_at_a_glance']['network']['status'])
    print("PROCESSOR: "+ health['health_at_a_glance']['processor']['status'])
    print("STORAGE: "+ health['health_at_a_glance']['storage']['status'])
    print("TEMPREATURE: "+ health['health_at_a_glance']['temperature']['status'])
    print(' \n------------------------------------\n')

    try:
        print('Fan 1 speed: '+str(health['fans']['Fan 1']["speed"][0])+'%')
        print('Fan 2 speed: '+str(health['fans']['Fan 2']["speed"][0])+'%')
        print('Fan 3 speed: '+str(health['fans']['Fan 3']["speed"][0])+'%')
        print('Fan 4 speed: '+str(health['fans']['Fan 4']["speed"][0])+'%')
        print('Fan 5 speed: '+str(health['fans']['Fan 5']["speed"][0])+'%')
        print('Fan 6 speed: '+str(health['fans']['Fan 6']["speed"][0])+'%')
        print(' \n------------------------------------\n')
    except:
        pass
        #need to write code for FAN status for Gen8

    print('Power Supply1: '+health["power_supplies"]["Power Supply 1"]['status'])
    print('Power Supply2: '+health["power_supplies"]["Power Supply 2"]['status'])
    try:
        print('Smart Storage Battery: '+health["power_supplies"]["Battery 1"]["status"])
    except:
        pass
    print(' \n------------------------------------\n')

    print('Processor1: '+health["processors"]["Proc 1"]["status"])
    print('Processor1: '+health["processors"]["Proc 2"]["status"])
    print(' \n------------------------------------\n')

    print('NIC1 status: '+health["nic_information"]["NIC Port 1"]["status"])
    print('NIC2 status: '+health["nic_information"]["NIC Port 2"]["status"])
    print('NIC3 status: '+health["nic_information"]["NIC Port 3"]["status"])
    print('NIC4 status: '+health["nic_information"]["NIC Port 4"]["status"])
    print(' \n------------------------------------\n')


    print('Storage -->Cache Module Status: '+health["storage"]["Controller on System Board"]["cache_module_status"])
    print('Logical Drive status: '+health["storage"]["Controller on System Board"]["logical_drives"][0]['status'])

    for i in range(22):
            print('Physical Drives' ,i+1)
            print(health["storage"]["Controller on System Board"]["logical_drives"][0]['physical_drives'][i]['status'])
    
 
except:
   pass

finally:
    sys.exit("Enter correct host/password")
    
