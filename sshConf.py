#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

## Çalıştırmadan önce ssh_config dosyasının yedeğini almayı unutmayınız! ##
## Script i yetkili kullanıcı ile çalıştırınız! ##

# Birden fazla aynı komutları değiştirmemek için 
a = False
b = False
c = False
d = False

with open("/etc/ssh/sshd_config", "a+") as file:
    icerik = file.readlines()
    for i in range(len(icerik)):
	# standart portu değitirme
        if(icerik[i].find("Port") != -1 and a==False):
            a=True
            icerik[i] = "Port 2222\n"
	# şifre ile ssh bağlantısını engelleme
        elif(icerik[i].find("PasswordAuthentication") != -1 and b==False): 
            b=True
            icerik[i] = "PasswordAuthentication no\n"
	# port yönlendrimelerini kapatma
        elif(icerik[i].find("X11Forwarding") != -1 and c==False):
            c=True
            icerik[i] = "X11Forwarding no\n"
	# root erişiminin kapatılması
        elif(icerik[i].find("PermitRootLogin") != -1 and d==False):
            d=True
            icerik[i] = "PermitRootLogin no\n"
	
        elif(icerik[i].find("AllowUsers") != -1):
            icerik[i] = "AllowUsers " + os.getenv("SUDO_USER")+"\n"  
            
    
    
    
    file.seek(0)
    file.writelines(icerik)
print("OK")    

#  eski ssh sürümünü (1) kaldırma
#  debian eski ssh sürümünü(protocol 1) desteklemiyor 
#  hangi kullanıcıların ssh kullanacağını belirleme

