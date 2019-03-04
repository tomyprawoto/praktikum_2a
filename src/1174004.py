# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#no1
print(1174004%3)


print ("+++ +++  +++++++++++ +++   +++  +++++++++  +++++++++  +++    +++")
print ("+++ +++  +++++++++++ +++   +++  +++++++++  +++++++++  +++    +++")
print ("+++ +++         +++  +++   +++  ++     ++  ++     ++  +++    +++")
print ("+++ +++        +++   +++   +++  ++     ++  ++     ++  +++    +++")
print ("+++ +++       +++    +++++++++  ++     ++  ++     ++  ++++++++++")
print ("+++ +++      +++           +++  ++     ++  ++     ++         +++")
print ("+++ +++     +++            +++  ++     ++  ++     ++         +++")
print ("+++ +++    +++             +++  ++     ++  ++     ++         +++")
print ("+++ +++   +++              +++  ++     ++  ++     ++         +++")
print ("+++ +++  +++               +++  +++++++++  +++++++++         +++")
print ("+++ +++ +++                +++  +++++++++  +++++++++         +++")
       
#nomor 2
npm = input("Masukan NPM :")
hitung = 0
while(hitung < 4):
     print("Halo, " +  str(npm) + " Apa Kabar?")
     hitung = hitung +1
     
     
#nomor 3
npm = input("Masukan NPM :")
hitung = 0
while(hitung < 4):
    print("Halo, " + str(npm[4:7]) + " Apa Kabar?")
    hitung = hitung +1
    
#nomor 4
npm = input("Masukan NPM :")
print("Halo, " + str(npm[-3]) + " Apa Kabar?")

#nomor 5
a = 1
b = 1
c = 7
d = 4
e = 0
f = 0
g = 4
h = a+b+c+d+e+f+g
i = a*b*c*d*e*f*g

print(a,b,c,d,e,f,g)

#nomor 6
print(h)

#nomor 7
print(i)

#nomor 8
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

#nomor 9
print(e,f,g)

#nomor 10
print(a,b,c,g)

#nomor 11
print(a,b,c,g)

#2.1
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:52:26 2019

@author: Knoy
"""

#1.variable python
nama = 'mas choi'
print (nama)

#2. input user
nama = raw_input("masukan nama anda :")
print (nama)

#2.input user 2
umur = input("tolong masukan umur anda :")
print (umur)

#3.aritmatika
#penjumlahan
aku = 0
kamu = 1
kita = kamu + aku
print "aku kamu itu", (kita)

#perkalian
panjang = 10
lebar = 5
luas = panjang * lebar
print(luas)

#pengurangan
dia1 = 10
dia2 = 5
dia_siapa = dia1 - dia2
print(dia_siapa)

#pembagian
a = 14
b = 4
c = a / b
print(c)

#mengubah int ke str
kamu = 'cantik'
kamu2 = 1
kamuitu = kamu + str(kamu2)
print (kamuitu)

#mengubah str ke int
a = 5
b = str(a)
print (b)

#4.perulangan
#while loop
count = 1
while (count < 15):
    print count
    count = count + 2

#for loop
kamu = ["cantik", "manis", "sholeha"]
for aku in kamu:
    print("saya suka cewek yang", aku)

#nested loop
i = 1
while(1 < 5):
    j = 1
    while(j <= 5):
        j += 1
    i += 1

#5.kondisi 
nilai = 9
if(nilai > 11):
    print("selamat ulang tahun")
else:
    print("selamat datang")

#kondisi di dalam kondisi
nilai = 9
if nilai > 9:
    print("nilai A")
elif nilai > 7:
    print("nilai B")
else:
    print("nilai C")
    
#6.jenis error


#7.pemakaian try except
try:
    print("choi")
except:
    print("mas choi ganteng")
finally:
    print("memang ganteng")





    