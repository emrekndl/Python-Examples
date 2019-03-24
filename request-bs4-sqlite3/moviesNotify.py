import requests
from bs4 import BeautifulSoup
import subprocess


class boxOffice():
    def __init__(self):
        self.url = "https://boxofficeturkiye.com/hafta-sonu/?yil=2019&hafta=10"
        self.headersP = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}
        self.resp = requests.get(self.url, headers=self.headersP)
        print(self.resp.ok)
        self.cont = self.resp.content
        self.soup = BeautifulSoup(self.cont, 'lxml')
        self.d1 = []
        self.d2 = []
        self.boxOfficeTurkiye = self.soup.find_all("a", attrs={"class": "film"})
        for self.boxV in range(0, 10):
            self.d1.append(self.boxOfficeTurkiye[self.boxV].get("title").strip())

        # self.boxVizyon = self.soup.find_all("td",attrs={"bgcolor":"#ffff99"})
        self.boxOfficeT = self.soup.find_all("td", attrs={"nowrap": "nowrap", "align": "left"})
        for self.box in range(0, 10):
            self.d2.append(self.boxOfficeT[self.box].text.strip())

        self.d = list(zip(self.d1, self.d2))
        for self.i in self.d:
            self.sendmessage(" ".join(self.i))
            # print(" ".join(self.i))

    def sendmessage(self, message):
        subprocess.Popen(['notify-send', message])
        return


i = boxOffice()
