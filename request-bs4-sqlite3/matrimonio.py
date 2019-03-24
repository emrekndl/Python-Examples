import requests
from bs4 import BeautifulSoup
#import pandas as pd
import os
import sqlite3

"""
#düğün yeri
---adı--- adresi---kapasite---ortamları---hizmetleri---konum----konaklama---hakkında---dahafazla---inceleme---yorumlar--resimler-harita
"""
class dugunYeri():
    def __init__(self,l=0,a=0):
            ##Wedding Location

            self.l=l
            self.t=0

            self.headersP = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}
            while(self.l < 233):
                self.oldL=self.l
                if self.l==1:
                    self.l=2

                self.urlWedding ="https://www.matrimonio.com/location-matrimoni--"+str(self.l) #--2 3 4 ....
                if self.l==0:
                    print("Sayfa:1")
                else:
                    print("Sayfa:",self.l)
                self.l+=1
                self.respWedding = requests.get(self.urlWedding,headers=self.headersP)
                self.contWedding = self.respWedding.content
                self.soupWedding = BeautifulSoup(self.contWedding,"html.parser") #self.resp.status_code == 200:
                self.soupWedding.prettify()
                self.weddingLocations = self.soupWedding.find_all("div",attrs={"class":"directory-item-content"})
                #print(self.weddingLocations)
                self.a=a

                print(len(self.weddingLocations))
                while(self.a < len(self.weddingLocations)):

                    self.dy= []
                    print("Link:",self.a)
                    self.oldA=self.a
                    self.weddingLocation = self.weddingLocations[self.a]
                    self.a+=1
                    self.weddingLocation = self.weddingLocation.find("a",{"href":True})
                    #print(self.weddingLocation['href'])
                    self.wedding = self.weddingLocation['href']

                    self.url = self.wedding  # https://www.matrimonio.com/hotel-ricevimenti/hotel-sassella-ristorante-jim--e21987
                    self.resp = requests.get(self.url,headers=self.headersP)
                    self.cont = self.resp.content
                    self.soup = BeautifulSoup(self.cont,"html.parser") #self.resp.status_code == 200:
                    self.soup.prettify()


                    ##names
                    try:
                        self.names = self.soup.find_all("h1",attrs={"class":"storefront-header-title"})
                        for self.name in self.names:
                            self.name= self.duzenle(self.name.text).replace(" ","_")
                            self.dy.append(self.name)
                    except Exception as e:
                        self.dy.append(" ")

                    ##address
                    try:
                        self.address = self.soup.find_all("div",attrs={"class":"vendor-address"})
                        for self.adrs in self.address:
                            self.address= self.duzenle(self.adrs.text)
                            self.dy.append(self.address.replace("            "," "))
                    except Exception as e:
                        self.dy.append(" ")

                    ##capacity
                    try:
                        self.capacity = self.soup.find("div",attrs={"class":"mt10 overflow"}).find("p").text
                        self.capacity= self.duzenle(self.capacity)
                        self.dy.append(self.capacity.replace("                                                                   ",""))
                    except Exception as e:
                        self.dy.append(" ")


                    ##ambience
                    try:
                        self.ambiance = self.soup.find("li",attrs={"id":"minifaqs_2"}).find("div",attrs={"class":"mt5 overflow"}).text
                        self.ambiance= self.duzenle(self.ambiance)
                        self.dy.append(self.ambiance.replace("                                                ",":"))
                    except Exception as e:
                        self.dy.append(" ")


                    ##services
                    try:
                        self.services = self.soup.find("li",attrs={"id":"minifaqs_319"}).find("div",attrs={"class":"mt5 overflow"}).text
                        self.services= self.duzenle(self.services)
                        self.dy.append(self.services.replace("                                                ",":"))
                    except Exception as e:
                        self.dy.append(" ")


                    ##location
                    try:
                        self.location = self.soup.find("li",attrs={"id":"minifaqs_8"}).find("div",attrs={"class":"mt5 overflow"}).text
                        self.location = self.duzenle(self.location)
                        self.dy.append(self.location.replace("                                                ",":"))
                    except Exception as e:
                        self.dy.append(" ")

                    ##Accommodation
                    try:
                        self.accommodation = self.soup.find("li",attrs={"id":"minifaqs_21"}).find("div",attrs={"class":"mt5 overflow"}).text
                        #print("Accommodation :",type(self.accommodation))
                        self.accommodation = self.duzenle(self.accommodation)
                        self.dy.append(self.accommodation.replace("                                                "," "))
                    except Exception as e:
                        self.dy.append(" ")

                    ##About
                    try:
                        self.about = self.soup.find("div",attrs={"class":"pure-u-2-3"}).find("div",attrs={"class":"storefront-description post mr40"}).text
                        self.about= self.duzenle(self.about)

                        #self.im.execute("INSERT INTO dugunYerleri(About) VALUES(?)",("./AboutText/"+self.about))
                        self.aboutText = self.soup.find_all("div",attrs={"class":"storefront-description post mr40"})
                        for self.abT in self.aboutText:
                            self.aboutText= self.duzenle(self.abT.text)
                        #self.dosya("AboutText",self.about,self.aboutText)
                        self.dy.append(self.about+self.aboutText)
                    except Exception as e:
                        self.dy.append(" ")

                    ##MoreInformmation
                    try:
                        self.moreInformation = self.soup.find("div",attrs={"class":"storefront-section"}).find("p",attrs={"class":"storefront-title-section"}).text
                        self.moreInformation= self.duzenle(self.moreInformation)

                        #self.im.execute("INSERT INTO dugunYerleri(MoreInformation) VALUES(?)",("./MoreInformationText/"+self.moreInformation))
                        self.mInformation = self.soup.find_all("ul",attrs={"class":"bullet-list"})
                        for self.mI in self.mInformation:
                            self.mInformation= self.duzenle(self.mI.text)
                        #self.dosya("MoreInformationText",self.moreInformation,self.mInformation.replace("                                        "," "))
                        self.dy.append(self.moreInformation+self.mInformation.replace("                                        "," "))
                    except Exception as e:
                        self.dy.append(" ")

                    ##Reviews
                    try:
                        self.reviews = self.soup.find_all("span",{"class":"storefrontItemReviews__ratio"})
                        for self.rvw in self.reviews:
                            self.reviews= self.duzenle(self.rvw.text)
                            self.dy.append(self.reviews)
                    except Exception as e:
                        self.dy.append(" ")


                    ##comments
                    try:
                        self.dizi = []
                        self.comments = self.soup.find("div",attrs={"class":"storefront-section storefrontReviews"}).find_all("blockquote")
                        self.comments2 = self.soup.find_all("p",attrs={"class":"storefrontItemReview__name"})
                        for self.x in range(len(self.comments)):
                            self.dizi.append(self.duzenle(self.comments[self.x].text)+" "+self.duzenle(self.comments[self.x].text))

                        self.dy.append("".join(self.dizi))
                    except Exception as e:
                        self.dy.append(" ")




                    ##Pictures
                    try:
                        self.urlP = self.url+"/fotos/0"
                        self.respP = requests.get(self.urlP)
                        self.contP = self.respP.content
                        self.soupP = BeautifulSoup(self.contP,"html.parser")
                        self.soupP.prettify()
                        self.pics = self.soupP.find_all("img",{"src":True})
                        self.i=1
                        for self.pic in self.pics:
                            self.pic=self.pic['src']
                            if self.pic.find("/emp/") != -1 and self.i <3:
                                self.rp = requests.get(self.pic)
                                if  not os.path.exists("./Pictures"):
                                    os.mkdir("Pictures")
                                if not os.path.exists("./Pictures/"+self.name):
                                    os.mkdir("Pictures/"+self.name)
                                with open("./Pictures/"+self.name+"/"+str(self.i)+".jpg","wb") as fl:
                                    fl.write(self.rp.content)
                                self.i+=1
                        self.dy.append("./Pictures/"+self.name)
                    except Exception as e:
                        self.dy.append(" ")


                    ##maps
                    try:
                        self.maps = self.soup.find_all("img",attrs={"id":"staticmap"})[0]

                        self.y = str(self.maps['data-src']).split("&")
                        #self.y = "".join(self.y).split("&")
                        self.y = self.y[3].split("S%7C")
                        self.dy.append("".join(self.y[-1]))
                    except Exception as e:
                        self.dy.append(" ")


                    print(self.wedding)
                    self.t+=1
                    print("Toplam Link:",self.t)



                    ##sqlite3
                    try:
                        self.vt = sqlite3.connect("dugunYeri.db")
                        self.im = self.vt.cursor()
                        self.im.execute("Create Table If not exists dugunYerleri(Name TEXT UNIQUE,Address TEXT,Capacity TEXT,Ambiance TEXT,Services TEXT,Locations TEXT,Accommodation TEXT,About TEXT,MoreInformation TEXT,Reviews TEXT,Pictures TEXT,Comments TEXT,Maps TEXT)")

                        self.im.execute("INSERT INTO dugunYerleri(Name,Address,Capacity,Ambiance,Services,Locations,Accommodation,About,MoreInformation,Reviews,Pictures,Comments,Maps) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                        (self.dy[0],self.dy[1],self.dy[2],self.dy[3],self.dy[4],self.dy[5],self.dy[6],self.dy[7],self.dy[7],self.dy[9],
                                        self.dy[10],self.dy[11],self.dy[12]))


                        self.vt.commit()
                        print("Kaydedildi\n")


                    except Exception as E:
                        print("Hata Veritabani :",E)
                        if E == "list index out of range":
                            self.__init__(self.oldL,self.oldA+1)

                    finally:
                        self.vt.close()
                        del self.dy



    def duzenle(self,var):
        var = var.strip()
        var = var.replace("\n","")
        return var

dy = dugunYeri()
