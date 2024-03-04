import os
from datetime import datetime
import locale
import sys
import time

locale.setlocale(locale.LC_ALL)

ad = input("adınız nedir :")

def kullanıcıgiriş(isim):
    print("hoşgeldin", isim )

kullanıcıgiriş(ad)

def amaç():
    while True:
        print("""işlem seçiniz :
            1- tarih ve saati öğren
            2- giriş yap
            3- ilerideki programa geç
            0- bitir """)
        işlemisteği = input("işlem :")
        if işlemisteği == "0":
            sys.exit() 
        elif işlemisteği == "1":
            şu_an = datetime.now()
            print(datetime.ctime(şu_an))
            time.sleep(1)
            input("devam etmek için enter tuşuna basınız...")
        elif işlemisteği == "3":
            break
amaç()








sys_kullanıcı_adı = "ahmet rıza oflaz"
sys_şifre = "123456"
while True:
    while True:
        kullanıcıadı = input("kullanıcı adını giriniz :")
        şifre = input("şifreyi giriniz :")

        if kullanıcıadı != sys_kullanıcı_adı and sys_şifre != sys_şifre:
            print("kullanıcı adı ve şifre hatalı tekrar deneyiniz...")
            continue
        elif kullanıcıadı == sys_kullanıcı_adı and şifre != sys_şifre:
            print("şifre hatalı tekrar deneyiniz...")
            continue
        elif kullanıcıadı != sys_kullanıcı_adı and şifre == sys_şifre:
            print("kullanıcı adı hatalı tekrar deneyiniz...")
            continue
        elif kullanıcıadı == sys_kullanıcı_adı and şifre == sys_şifre:
            print("giriş yapıldı....")
            break

    while True:

        print("""
    *************************************
            ...işlemler...
    0 -) programı sıfırla
    1 -) kullanıcı adı değiştirme
    2 -) şifre değiştirme
    3 -) dosyaya görev ekleme
    4 -) görevleri yazdırma
    5 -) matematiksel işlemler
    6 -) görev dosyasını sıfırla
    *************************************""")
        işlem = input("işlem seçiniz :")

        if işlem == "0":
            print("program sıfırlanıyor...")
            break
        elif işlem == "1":
            yenikullanıcıadı = input("yeni kullanıcı adını giriniz :")
            sys_kullanıcı_adı = yenikullanıcıadı
            print("kullanıcı adı değiştirildi...")
            input("devam etmek için enter tuşuna basınız...")
        elif işlem == "2":
            yenişifre = input("yeni şifreyi giriniz :")
            sys_şifre = yenişifre
            print("şifre değiştirildi...")
            input("devam etmek için enter tuşuna basınız...")
        elif işlem == "3":
            görev = input("dosyaya eklenecek görevi giriniz :")
            with open("şirketkayıtları.txt","a",encoding="utf-8")as file:
                ekleme = []
                ekleme.append(görev)

                for i in ekleme:
                    file.write(i)
            print("dosyaya kaydedildi...")
            input("devam etmek için enter tuşuna basınız...")
        elif işlem == "4":
            print("görevler :")
            with open("şirketkayıtları.txt","r",encoding="utf-8")as file:
                for i in file:
                    print(i)
            input("devam etmek için enter tuşuna bas...")
        elif işlem == "5":
            while True:
                print("""************************
                    0 -) programı bitir
                    1 -) sayıları toplama
                    2 -) faktöriyel bulma
                    3 -) asalmı değilmi sorgu 
                    4 -) belli aralıklardaki asal sayılar 
                    5 -) aralarında asal sorgulaması yapmak
                    ***************************""")
                işlem2 = input("işlem seçiniz :")
                
                if işlem2 == "0":
                    print("matematik işlemlerinden çıkış yapılıyor...")
                    break
                elif işlem2 == "1":
                    while True:
                        try:
                            sayı = int(input("sayı giriniz :"))
                            for i in sayı:
                                toplam = 0
                                toplam += i
                                print("toplamı :",toplam)
                            if sayı == 0:
                                print("sayıların toplamı :",toplam)
                                print("program sonlanıyor...")
                                break
                        except ValueError:
                            print("sayı giriniz...")
                        input("devam etmek için enter tuşuna bas...")
                elif işlem2 == "2":
                    def hesapla_faktoriyel(number):
                        factorial = 1
                        if number >= 0:
                            for i in range(1, number + 1):
                                factorial *= i
                            return factorial
                        else:
                            return None
    
                    number = int(input("Lütfen faktöriyelini bulmak istediğiniz sayıyı giriniz...\n"))
                    factorial = hesapla_faktoriyel(number)
                    
                    if factorial:
                        print(f"Girdiğiniz sayının faktöriyeli: {number}! = {factorial}")
                    else:
                        print("Negatif sayıların faktöriyeli olmaz!")
                elif işlem2 == "3":
                    while True:

                        sayı2 = int(input("sayıyı giriniz :"))
                        if sayı2 == 0:
                            print("sonlandırılıyor...")
                            break
                        for i in range(2,sayı2):
                            if sayı2 % i == 0:
                                print("bu sayı asal değildir...")
                                continue
                            elif i == sayı2-1:
                                print(sayı2,"bir asal sayıdır.")
                                input("\nDevam etmek için ENTER tuşuna bas\n")
                elif işlem2 == "4":
                        while True:
                            sayi1 = int(input("Aralığın ilk sayısını gir:"))
                            sayi2 = int(input("Aralığın son sayısın gir:"))
                            asallar = ""

                            if sayi1 == 0 and sayi2 == 0:
                                print("program sonlanıyor...")
                                break                       
                            else:
                                for i in range(sayi1+1,sayi2):
                                    for j in range(2,i):
                                        if i % j == 0:
                                            break
                                        elif j == i-1:
                                            asallar += str(i) + ", "
                                            if asallar == "":
                                                print("Bu aralıkta hiçbir asal sayı bulunmuyor.")
                                                input("\nDevam etmek için ENTER tuşuna bas\n")
                                            else:
                                                print("Bu aralıktakı asal sayılar: ",asallar)
                                                input("\nDevam etmek için ENTER tuşuna bas\n")
                                                continue
        elif işlem == "6":
            eminmisin = input("dosyayı silmek istediğinize eminmisiniz...")

            if eminmisin == "evet":
                os.rmdir("şirketkayıtları.txt")
                