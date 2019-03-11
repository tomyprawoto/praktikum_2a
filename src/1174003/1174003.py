# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:29:12 2019

@author: asus
"""

#Ketrampilan Pemrograman
#No.1
def jawabanNo1():
    
    npm = input("Masukan NPM :")
    npm = list(str(npm))

    angka1 = {"0":" ###### ", "1":"  ##", "2":" #######  ", "3":"  #######  ", "4":"   #####", "5":"#######", "6":" #######", "7":"#######", "8":" ##### ", "9":" ######  "}
    angka2 = {"0":"###  ###", "1":"####", "2":"##    ### ", "3":"###     ###", "4":"  ##  ##", "5":"##     ", "6":"###     ", "7":"#######", "8":"##   ##", "9":"##    ## "}
    angka3 = {"0":"###  ###", "1":" ###", "2":"     ###  ", "3":"      #### ", "4":" ##   ##", "5":"##     ", "6":"###     ", "7":"   ### ", "8":" ##### ", "9":"##    ## "}
    angka4 = {"0":"###  ###", "1":" ###", "2":"    ###   ", "3":"      #### ", "4":"########", "5":"###### ", "6":"########", "7":"  ###  ", "8":"#######", "9":"######## "}
    angka5 = {"0":"###  ###", "1":" ###", "2":"  ####    ", "3":"###     ###", "4":"      ##", "5":"     ##", "6":"###  ###", "7":" ###   ", "8":"##   ##", "9":"      ## "}
    angka6 = {"0":" ###### ", "1":" ###", "2":"######### ", "3":"  #######  ", "4":"      ##", "5":"###### ", "6":" ###### ", "7":"###    ", "8":" ##### ", "9":"#######  "}
          
    hasil1 = []
    hasil2 = []
    hasil3 = []
    hasil4 = []
    hasil5 = []
    hasil6 = []

    for x in npm:
        hasil1.append(angka1[x])
        hasil2.append(angka2[x])
        hasil3.append(angka3[x])
        hasil4.append(angka4[x])
        hasil5.append(angka5[x])
        hasil6.append(angka6[x])
    
    print(*hasil1, sep=' ')
    print(*hasil2, sep=' ')
    print(*hasil3, sep=' ')
    print(*hasil4, sep=' ')
    print(*hasil5, sep=' ')
    print(*hasil6, sep=' ')

jawabanNo1()

#no.2
def ulang(npm):
    hitung = 0
    while(hitung <3):
        print("Halo, " + str(npm) + " Apa Kabar?")
        hitung = hitung +1
ulang(int(input("Masukkan NPM: ")))

#no.3
def ulang_3_digit_terakhir(npm):
    hitung = 0
    npm = str(npm)
    x = npm[4:7]
    while(hitung < 15):
        print("Halo, " + x + " Apa Kabar?")
        hitung = hitung +1
ulang_3_digit_terakhir(int(input("Masukkan NPM: ")))

#no.4
def digit_3_dari_belakang(npm):
    npm = str(npm)
    x = npm[-3]
    print("Halo, " + x + " Apa Kabar?")
digit_3_dari_belakang(int(input("Masukkan NPM: ")))

#no5
def bawah(npm):
    for i in npm:
        print (i)
    
bawah(input("Masukkan NPM: "))

#no.6
def tambahan(npm):
    jumlah = 0
    for i in npm:
        jumlah += int(i)
    print ("Hasil Penjumlahan NPM adalah : " +str(jumlah))
tambahan(input("Masukkan NPM: "))

#No.7
def kalikan(npm):
    kalikan = 0
    for i in npm:
        kalikan *= int(i)
    print ("Hasil Perkalian NPM adalah : " +str(kalikan))
kalikan(input("Masukkan NPM: "))

#N0.8
def digit_genap(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end ="")
digit_genap(input("Masukkan NPM: "))

#No.9
def digit_ganjil(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 !=0):
            print(n, end ="")
digit_ganjil(input("Masukkan NPM: "))

#No.10
def digit_prima(npm):
    npm = list(map(int, npm))
    prima = []
    for n in npm:
        bilPrima = True
        if n == 0 or n ==1:
            bilPrima = False
        for x in range(2, n):
            if n % x == 0:
                bilPrima = False
        if bilPrima:
            prima.append(n)
                
        for p in prima:
            print(p, end = "")
digit_prima(input("Masukkan NPM: "))

#No.11

#No. 12

#Keterampilan Penanganan error
#No.1
def halo(nama):
    try:
        print("Hallo, "+str(nama))
    except:
        print("Ada Yang Error")
        
halo(input("Cantumkan Nama Anda : "))
