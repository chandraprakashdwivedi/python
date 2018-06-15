#!/usr/bin/env python
# -*- coding: utf-8 -*-

from netmiko import ConnectHandler
import time

store = raw_input("Enter the number of store whose Post Work you want : ")
fqdn_wlc = store + "-
usrn = raw_input("Enter the username : ")
paswd_wlc = raw_input("Enter the password for " + store + "-wlc :")
device_wlc = ConnectHandler(device_type='cisco_wlc', ip=fqdn_wlc , username=usrn , password=paswd_wlc)
commands_of_wlc = [ "config paging disable\n" ,
                   "show sysinfo\n" ,
                   "show version\n" ,
                   "show license all\n" ,
                   "show inventory\n" ,
                   "show ap summary\n" ,
                   "show mobility summary\n" ,
                   "show client summary\n" ,
                   ]

for command in commands_of_wlc:
  try:
       device_wlc.find_prompt()
       output = device_wlc.send_command_expect(command)
       time.sleep(3)
       print (output)
  except:
          print("error")
device_wlc.disconnect()
