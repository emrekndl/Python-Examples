import sqlite3

class veriTabani():
    def __init__(self):
        self.createTable()

    def connectionDb(self,database="database.db"):
        try:
            conn = sqlite3.connect(database)
            return conn
        except Exception as e:
            return "Hata :"+str(e)


    def createTable(self):
        try:
            self.cursor = self.connectionDb().cursor()
            self.cursor.execute("Create Table If not exists uyeler(adSoyad TEXT,kullaniciAdi TEXT UNIQUE,parola TEXT)")
            self.connectionDb().commit()
        except Exception as e:
            return "Baglanti olusturulamadi! Hata :"+str(e)
        finally:
            self.connectionDb().close()


    def login(self,kullaniciAdi,parola):
        try:
            self.cursor = self.connectionDb().cursor()
            self.cursor.execute("Select * from uyeler where kullaniciAdi = ? and parola = ?",(kullaniciAdi,parola))
            data = self.cursor.fetchall()
            if len(data) == 0:
                return 0
            else:
                return 1
        except Exception as e:
            return "Tablo olusturulamadi! Hata :"+str(e)
        finally:
            self.connectionDb().close()


    def add(self,adSoyad,kullaniciAdi,parola):
        try:
            self.cursor = self.connectionDb().cursor()
            self.cursor.execute("INSERT INTO uyeler(adSoyad,kullaniciAdi,parola) VALUES(?,?,?)",(adSoyad,kullaniciAdi,parola))
            self.connectionDb().commit()
            return "Kayit Basarili Lutfen Giris Yapınız."
        except Exception as e:
            return "Kayit Basarisiz! :"+str(e)
        finally:
            self.connectionDb().close()

    def delete(self,kullaniciAdi):
        try:
            self.cursor = self.connectionDb().cursor()
            self.cursor.execute("DELETE from uyeler where kullaniciAdi = (?)",(kullaniciAdi,))
            self.connectionDb().commit()
            return "Kaydiniz Basarili Bir Sekilde Silinmistir."
        except Exception as e:
            return "Silme Basarisiz! Hata :"+str(e)
        finally:
            self.connectionDb().close()
    
    def update(self,adSoyad,kullaniciAdi,parola,kAdi):
        try:
            self.cursor = self.connectionDb().cursor()
            self.cursor.execute("UPDATE uyeler SET adSoyad = (?) ,kullaniciAdi = (?) ,parola = (?) where kullaniciAdi = (?)",(adSoyad,kullaniciAdi,parola,kAdi))
            self.connectionDb().commit()
            return "Guncelleme Basarili Lutfen Gırıs Yapiniz."
        except Exception as e:
            return "Guncelleme Basarisiz! Hata :"+str(e)
        finally:
            self.connectionDb().close()
    
    def list(self,kullaniciAdi):
        try:
            self.cursor = self.connectionDb().cursor()
            self.cursor.execute("Select * from uyeler where kullaniciAdi = ?",(kullaniciAdi))
            data = self.cursor.fetchall()
            self.connectionDb().commit()
            return data
        except Exception as e:
            return "Tablodan veriler alinamadi! Hata :"+str(e)
        finally:
            self.connectionDb().close()
    

