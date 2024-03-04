      #Asal Sayı Programı
while True:
 
 
 print("""
Yapmak istediğin işlemi seç

1)Bir sayının Asal Olup olmadığını öğrenmek.
2)Belli aralıktaki asal sayıları bulmak.
3)Aralarında asal sorgulaması yapmak.

""")

 islem = input("Yapacağın işlemin numarasını gir:")


 if islem == "1":
    
    sayi = int(input("Hangi sayıyının asal olup olmadığını öğrenmek istiyorsun?\n"))

    for i in range(2,sayi):
        if sayi % i == 0:
            print(sayi,"bir asal sayı değildir.")
            input("\nDevam etmek için ENTER tuşuna bas\n")
            break
        elif i == sayi-1:
            print(sayi,"bir asal sayıdır.")
            input("\nDevam etmek için ENTER tuşuna bas\n")

 elif islem == "2":
    kontrol = 1
    while kontrol == 1:
     kontrol -= 0
     sayi1 = int(input("Aralığın ilk sayısını gir:"))
     sayi2 = int(input("Aralığın son sayısın gir:"))
     asallar = ""
    
     if sayi1 >= sayi2:
       print("İlk sayı 2.sayıdan büyük veya eşit olamaz.")
       input("\nDevam etmek için ENTER tuşuna bas\n")
     elif sayi1 < 0 or sayi2 < 0:
       print("Sayılar 0'dan küçük olamaz.")
       input("\nDevam etmek için ENTER tuşuna bas\n")
       
     else:
      kontrol += 1
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

 elif islem == "3":
   kontrol = 1
   while kontrol == 1:
    kontrol -= 1
    sayi1 = int(input("Sayı 1: "))
    sayi2 = int(input("Sayı 2: "))
    if sayi1 > sayi2:
      for i in range(2,sayi2+1):
         if sayi1 % i == 0 and sayi2 % i == 0:
            print(sayi1,sayi2,"aralarında asal değildir.")
            input("\nDevam etmek için ENTER tuşuna bas\n")
            break
         elif i == sayi2:
            print(sayi1,sayi2,"aralarında asaldır.")
            input("\nDevam etmek için ENTER tuşuna bas\n")

    elif sayi1 < sayi2:
      for i in range(2,sayi1+1):
         if sayi1 % i == 0 and sayi2 % i == 0:
            print(sayi1,sayi2,"aralarında asal değildir..")
            input("\nDevam etmek için ENTER tuşuna bas\n")
            break
         elif i == sayi1:
            print(sayi1,sayi2,"aralarında asaldır.")
            input("\nDevam etmek için ENTER tuşuna bas\n")

    else:
      print("Sayılar aynı olamaz.")
      input("Devam etmek için ENTER tuşuna bas.")
      kontrol += 1

 else:
   print("3 Numaradan birisini seç.")
   input("\nDevam etmek için ENTER tuşuna bas\n")




   