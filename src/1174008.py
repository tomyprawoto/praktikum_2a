# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:24:33 2019

@author: PERSONAL
"""

#Nomor 1
print ("***  ***   ***********   ***   ***   *********   *********   *********")
print ("***  ***   ***********   ***   ***   *********   *********   *********")
print ("***  ***          ***    ***   ***   **     **   **     **   **     **")
print ("***  ***         ***     ***   ***   **     **   **     **   **     **")
print ("***  ***        ***      *********   **     **   **     **   **     **")
print ("***  ***       ***             ***   **     **   **     **   *********")
print ("***  ***      ***              ***   **     **   **     **   **     **")
print ("***  ***     ***               ***   **     **   **     **   **     **")
print ("***  ***    ***                ***   **     **   **     **   **     **")
print ("***  ***   ***                 ***   *********   *********   *********")
print ("***  ***  ***                  ***   *********   *********   *********")

#Nomor 2
npm = input("Masukan NPM :")
hitung = 0
while(hitung <= 87):
     print("Halo, " +  str(npm) + " Apa Kabar?")
     hitung = hitung +1
     
#Nomor 3
npm = input("Masukan NPM :")
hitung = 0
while(hitung <= 15):
    print("Halo, " + str(npm[4:7]) + " Apa Kabar?")
    hitung = hitung +1
    
#Nomor 4
npm = input("Masukan NPM :")
print("Halo, " + str(npm[-3]) + " Apa Kabar?")

#Nomor 5
a = 1
b = 1
c = 7
d = 4
e = 0
f = 2
g = 7
h = a+b+c+d+e+f+g
i = a*b*c*d*e*f*g
print(a,b,c,d,e,f,g)

#Nomor 6
print(h)

#Nomor 7
print(i)

#Nomor 8
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

#Nomor 9
print(d,g)

#Nomor 10
print(a,b,c,f)

#Nomor 11
print(a,b,c,)


#1. Variable Di Python
nama = 'Arjun Yuda Firwanda'
print (nama)

#2. Input User dan Output Ke Layar
nama = input("Masukkan Nomor: ")
print(nama)

#3. Operasi Aritmatika
#Penjumlahan
x = 7
y = 9
total = x + y
print(total)

#Perkalian
m = 5
n = 5
total = m * n
print(total)

#Pengurangan
a = 9
b = 5
total = a - b
print(total)

#Pembagian
p = 10
q = 5
total = p / q
print(total)

#Mengubah Integer Ke String
aku1 = 'ganteng'
kamu2 = 1
kamuitu = aku1 + int(kamu2)
print(kamuitu)

#Mengubah String Ke Integer
x = 3
y = str(x)
print(y)

#4. Perulangan
#While Loop
count = 1
while(count < 15):
    print (count)
    count = count + 2

#For Loop
kamu = ["Ganteng", "Manis", "Sholeh"]
for aku in kamu:
    print("Saya Suka Cowok yang", aku)

#Nested Loop
i = 1
while(1 < 5):
    j = 1
    while(j <= 5):
        j += 1
    i += 1

#5. Kondisi
nilai = 10
if(nilai > 12):
    print("Selamat Ya")
else:
    print("Selamat Datang")

#Kondisi Di Dalam Kondisi
nilai = 9
if nilai > 9:
    print("Nilai A")
elif nilai > 7:
    print("Nilai C")

#6. Jenis-jenis Error Di Dalam Python



#7. Pemakaian Try Except
try:
    print("Arjun")
except:
    print("Arjun Ganteng")
finally:
    print("Memanglah")


