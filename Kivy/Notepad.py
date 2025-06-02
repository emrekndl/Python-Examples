# -*- coding: utf-8 -*-

import os
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.popup import Popup



class kaydetForm(Popup):
    pass


class dosyaAcForm(Popup):
    pass


class metinDuzenleyici(App):

    def hataGoster(self, hata):
        icerik = Label(text=hata)
        popup = Popup(title='Yapilamadi !', content=icerik)
        popup.size_hint = (0.7, 0.7)
        icerik.bind(on_touch_down=popup.dismiss)
        popup.open()

    def kaydetDialog(self):
        form = kaydetForm()
        form.open()

    def kaydetDosyaAdi(self, form):
        secilenDosya = form.ids.dosyaSecim.selection  # kaydet de secilen dosya
        if secilenDosya:
            if len(secilenDosya) > 0:
                # dosyayinin yolunu ve adini ayirir
                dosyaAdi = os.path.split(secilenDosya[0])[1]
                form.ids.dosyaAdi.text = dosyaAdi

    def kaydetIslemi(self, form):
        self.sonPatika = form.ids.dosyaSecim.path
        self.sonDosya = form.ids.dosyaAdi.text
        if not self.sonDosya:
            self.hataGoster("Dosya adi giriniz!!!")
        else:
            try:
                dosyaTamIsim = os.path.join(self.sonPatika, self.sonDosya)
                with open(dosyaTamIsim, "w") as file:
                    file.write(self.root.ids.metin.text)
            except Exception as e:
                self.hataGoster("Dosya yazilamadi! :"+e)

    def dosyaAcDialog(self):
        form = dosyaAcForm()
        form.open()

    def dosyaOku(self, dosyaSecim):
        if dosyaSecim.selection:
            if len(dosyaSecim.selection) > 0:
                (self.sonPatika, self.sonDosya) = os.path.split(
                    dosyaSecim.selection[0])  # dosya yolu ve dosya adı ayrılır
                try:
                    self.root.ids.metin.text = open(
                        dosyaSecim.selection[0]).read()
                    self.root.ids.metin.cursor = self.root.ids.metin.get_cursor_from_index(0)
                except Exception as e:
                    self.hataGoster("Dosya Acilamadi! :"+e)
        else:
            self.hataGoster("Dosya secilmedi!!")

    def temizle(self, metin):
        metin.text = ""

    def build(self):
        self.sonPatika = os.getcwd()  # patikayı bulunduğu dizine esitler
        self.sonDosya = ''


if __name__ == "__main__":
    metinDuzenleyici().run()
