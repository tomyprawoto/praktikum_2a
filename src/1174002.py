# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#1. Variable
nama = 'habib abdul rasyid'
print (nama)

#2. Input
usia = input("Masukan umur anda :")
print (usia)

#3. Operator
aku = 1
kamu = 2
kita = aku + kamu
print ("Aku dan Kamu"), (kita)

print ("pengurangan")
lo1 = 5
lo2 = 2
kamu_siapa = lo1 - lo2
print (kamu_siapa)

print ("perkalian")
panjang = 5
lebar = 2
luas = panjang * lebar
print (luas)

print ("pembagian")
roti = 8
sobek = 2
kue_sobek = roti / sobek
print (kue_sobek)

#convert
print ("mengubah int ke string")
kamu = "cantik"
kamu2 = 1
kamuitu = kamu + str(kamu2)
print (kamuitu)

print ("mengubah str ke int")
a = 5
b = str(a)
print(b)

#4. perulangan
i = 1
while i < 9:
    print(i)
    i += 1
#while
kue = ["Bolu", "Brownies", "Keju"]
for x in kue:
    print(x)

#5. kondisi
x = 100
y = 20
if x > y:
    print("x lebih besar dari y")
else:
    print("x tidak lebih besar dari y")
#7. try except
try:
    print("habib")
except:
    print("habib abdul rasyid")
finally:
    print("mantap")


#No.1
print(1174002%3)

print("***  ***  **********  ***     ***  **********  *********  ********")
print("***  ***  **********  ***     ***  **********  *********  ********")
print("***  ***         ***  ***     ***  ***    ***  ***   ***       ***")
print("***  ***        ***   ***     ***  ***    ***  ***   ***       ***")
print("***  ***       ***    ***********  ***    ***  ***   ***  ********")
print("***  ***      ***             ***  ***    ***  ***   ***  ********")
print("***  ***     ***              ***  ***    ***  ***   ***  ***     ")
print("***  ***    ***               ***  **********  *********  ********")
print("***  ***   ***                ***  **********  *********  ********")

#No.2
npm = input("Masukan NPM :")
hitung = 0
while(hitung < 2):
    print("Halo, " + str(npm) + " Apa Kabar?")
    hitung = hitung +1

#No.3
npm = input("Masukan NPM : ")
hitung = 0
while(hitung < 2):
    print("Halo, " + str(npm[4:7]) + " Apa Kabar?")
    hitung = hitung +1
    
#No.4
npm = input("Masukan NPM : ")
print("Halo, " + str(npm[-3]) + " Apa Kabar?")

#No.5
a = 1
b = 1
c = 7
d = 4
e = 0
f = 0
g = 2
h = a+b+c+d+e+f+g
i = a*b*c*d*e*f*g

print (a,b,c,d,e,f,g)

#No.6
print(h)

#No.7
print(i)

#No.8
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

#No.9
print(d,g)

#No.10
print(a,b,c)

#No.11
print(a,b,c)
