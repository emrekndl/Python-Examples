import requests
from bs4 import BeautifulSoup
import subprocess
import os

class fifa():
    def __init__(self):
        self.url="http://www.futbolingo.com/mac-sonuclari"
        self.headersP = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}
        self.resp = requests.get(self.url,headers=self.headersP)
        print(self.resp.ok)
        self.cont = self.resp.content
        self.soup = BeautifulSoup(self.cont,'lxml')
        self.d1 = []
        self.d2 = []
        self.d3 = []
        self.d4 = []
        self.d5 = []
        self.ff1 = self.soup.find_all("div",attrs={"class":"ital"}) #ev
        self.ff2 = self.soup.find_all("div",attrs={"class":"isc"})  #skor
        self.ff3 = self.soup.find_all("div",attrs={"class":"itar"}) #rakip
        self.ff4 = self.soup.find_all("div",attrs={"class":"isd"})  #saat
        self.ff5 = self.soup.find_all("div",attrs={"class":"imin"}) #sonuc
        self.ff6 = self.soup.find("h1") #tarih

        for self.f1 in self.ff1:
            self.d1.append(self.f1.text.strip())
            #print(self.f1.text)
        for self.f2 in self.ff2:
            if self.f2.text.strip() != '-' and self.f2.find("a") :
                self.d2.append(self.f2.text.strip())

        for self.f3 in self.ff3:
            self.d3.append(self.f3.text.strip())
            #print(self.f3.text)

        for self.f5 in self.ff5:
            #if self.f5.text.strip() == "MS" :
            self.d5.append(self.f5.text.strip())

        for self.f4 in self.ff4:
            self.d4.append(self.f4.text.strip())





        #self.d4 = list(zip(self.d1,self.d3))
        self.sendmessage(str(self.ff6.text).upper())
        for self.i in range(0,9):
            self.sendmessage(self.d5[self.i]+" "+"".join(self.d1[self.i])+" * "+self.d2[self.i]+" * "+"".join(self.d3[self.i])+" "+self.d4[self.i])


    def sendmessage(self,message):
        os.system("notify-send -u normal '"+message+"'")
        #subprocess.Popen(['notify-send', message])
        return

i = fifa()
