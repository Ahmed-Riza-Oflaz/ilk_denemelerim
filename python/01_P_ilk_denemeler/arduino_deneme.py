import serial

port = serial.Serial('com3',9600)

while True:
    veri_girişi = input("ledi açmak için a kapatmak için b :")
    if (veri_girişi=="a"):
        port.write(b'a')
    elif (veri_girişi=="b"):
        port.write(b'b')
    elif ( veri_girişi=="c"):
        port.write(b'c')