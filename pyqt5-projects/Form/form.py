import sys
import sqlite3
import veritabani
from PyQt5 import QtWidgets


class Pencere1(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.vt = veritabani.veriTabani()
        self.ini_ui()
        


    def ini_ui(self):
        self.kullaniciAdi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giris Yap")
        self.kayit = QtWidgets.QPushButton("Kaydol")
        self.label = QtWidgets.QLabel("")
        self.kAdi = QtWidgets.QLabel("Kullanici Adi")
        self.p = QtWidgets.QLabel("Parola")

        vBox = QtWidgets.QVBoxLayout()
        vBox.addWidget(self.kAdi)
        vBox.addWidget(self.kullaniciAdi)
        vBox.addWidget(self.p)
        vBox.addWidget(self.parola)
        vBox.addWidget(self.label)
        vBox.addStretch()

        hBox = QtWidgets.QHBoxLayout()
        hBox.addStretch()
        hBox.addLayout(vBox)
        hBox.addStretch()
        hBox2 = QtWidgets.QHBoxLayout()
        hBox2.addWidget(self.giris)
        hBox2.addWidget(self.kayit)
        vBox.addLayout(hBox2)

        self.setLayout(hBox)

        self.setWindowTitle("Kullanici Girisi")
        self.giris.clicked.connect(self.login)
        self.kayit.clicked.connect(self.register)
        self.show()
  
    def login(self):
        adi = self.kullaniciAdi.text()
        par = self.parola.text()
        data = self.vt.login(adi,par)
        if data == 0:
            self.label.setText("Kullanici Yok!\nLutfen Tekrar Deneyin")
        elif data == 1:
            self.p3 = Pencere3(adi)
            self.hide()
        else:
            self.label.setText(str(data))
    
        
    def register(self):
        self.p2 = Pencere2()
        self.hide()
    


class Pencere2(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.vt = veritabani.veriTabani()
        self.ini_ui2()
        

    def ini_ui2(self):
        self.adSoyad = QtWidgets.QLineEdit()
        self.adSoyadLabel = QtWidgets.QLabel("Ad Soyad :")
        self.kAdi = QtWidgets.QLineEdit()
        self.kAdiLabel = QtWidgets.QLabel("Kullanıcı Adı :")
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.parolaLAbel = QtWidgets.QLabel("Parola :")
        self.kaydol = QtWidgets.QPushButton("Kaydol")
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.giris = QtWidgets.QPushButton("Giris")
        self.label = QtWidgets.QLabel("")

        vBox = QtWidgets.QVBoxLayout()
        vBox.addWidget(self.adSoyadLabel)
        vBox.addWidget(self.adSoyad)
        vBox.addWidget(self.kAdiLabel)
        vBox.addWidget(self.kAdi)
        vBox.addWidget(self.parolaLAbel)
        vBox.addWidget(self.parola)
        vBox.addStretch()
        hBox = QtWidgets.QHBoxLayout()
        hBox.addWidget(self.kaydol)
        hBox.addWidget(self.temizle)
        vBox.addLayout(hBox)
        vBox.addWidget(self.giris)
        vBox.addStretch()
        vBox.addWidget(self.label)
        self.setLayout(vBox)

        self.kaydol.clicked.connect(self.kayit)
        self.temizle.clicked.connect(self.clear)
        self.giris.clicked.connect(self.girisYap)
        self.setWindowTitle("Kayit")
        self.show()

    def kayit(self):
        adS = self.adSoyad.text()
        kAd = self.kAdi.text()
        p = self.parola.text()
        self.label.setText(self.vt.add(adS,kAd,p))
        

    def girisYap(self):
        self.p =Pencere1()
        self.hide()

    def clear(self):
        self.adSoyad.clear()
        self.kAdi.clear()
        self.parola.clear()



class Pencere3(QtWidgets.QWidget):
    def __init__(self,adi):
        super().__init__()
        self.vt = veritabani.veriTabani()
        self.ini_ui3(adi)
        self.ad=adi
    
    def ini_ui3(self,adi):
        self.label = QtWidgets.QLabel("")
        self.duzenle = QtWidgets.QPushButton("Bilgilerini Duzenle")
        self.cikis = QtWidgets.QPushButton("Cikis")
        self.sil = QtWidgets.QPushButton("Kaydini Sil")
        vBox = QtWidgets.QVBoxLayout()
        vBox.addWidget(self.label)
        vBox.addStretch()
        vBox.addWidget(self.duzenle)
        vBox.addWidget(self.sil)
        vBox.addWidget(self.cikis)
        self.setLayout(vBox)
        self.label.setText("Hos Geldin "+adi)

        self.duzenle.clicked.connect(self.kayitDuzenle)
        self.sil.clicked.connect(self.kayitSil)
        self.cikis.clicked.connect(self.cikisYap)
        self.setWindowTitle("Kullanici :"+adi)
        self.show()

    def kayitDuzenle(self):
        self.d = Pencere4(self.ad)
        self.hide()
        
    def kayitSil(self):
        self.label.setText(self.vt.delete(self.ad))
        self.duzenle.hide()
        self.sil.hide()
     

    def cikisYap(self):
        QtWidgets.qApp.quit()

class Pencere4(QtWidgets.QWidget):
    def __init__(self,ad):
        super().__init__()
        self.vt = veritabani.veriTabani()
        self.ini_ui4(ad)
        self.ad=ad

    def ini_ui4(self,ad):
        self.adSoyad = QtWidgets.QLineEdit()
        self.adSoyadLabel = QtWidgets.QLabel("Ad Soyad :")
        self.kAdi = QtWidgets.QLineEdit()
        self.kAdiLabel = QtWidgets.QLabel("Kullanıcı Adı :")
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.parolaLAbel = QtWidgets.QLabel("Parola :")
        self.guncelle = QtWidgets.QPushButton("Guncelle")
        self.giris = QtWidgets.QPushButton("Giris")
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.label = QtWidgets.QLabel("")

        vBox = QtWidgets.QVBoxLayout()
        vBox.addWidget(self.adSoyadLabel)
        vBox.addWidget(self.adSoyad)
        vBox.addWidget(self.kAdiLabel)
        vBox.addWidget(self.kAdi)
        vBox.addWidget(self.parolaLAbel)
        vBox.addWidget(self.parola)
        vBox.addStretch()
        hBox = QtWidgets.QHBoxLayout()
        hBox.addWidget(self.guncelle)
        hBox.addWidget(self.temizle)
        vBox.addLayout(hBox)
        vBox.addWidget(self.giris)
        vBox.addStretch()
        vBox.addWidget(self.label)
        self.setLayout(vBox)

        self.guncelle.clicked.connect(self.kayitGuncelle)
        self.temizle.clicked.connect(self.clear)
        self.giris.clicked.connect(self.girisYap)

        self.data = self.vt.list(ad)
        
        self.adSoyad.setText(str(self.data[0][0]))
        self.kAdi.setText(str(self.data[0][1]))
        self.parola.setText(str(self.data[0][2]))

        self.setWindowTitle("Guncelle")
        self.show()
    
    def girisYap(self):
        self.p =Pencere1()
        self.hide()
        

    def kayitGuncelle(self):
        adS = self.adSoyad.text()
        kAd = self.kAdi.text()
        p = self.parola.text()
           
        self.label.setText(self.vt.update(adS,kAd,p,self.ad))
        
    def clear(self):
        self.adSoyad.clear()
        self.kAdi.clear()
        self.parola.clear()


#if __name__ == '__main__':
# import veritabani
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere1()
sys.exit(app.exec_())
