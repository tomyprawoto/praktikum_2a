# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:18:53 2019

@author: dzihan
"""
#1 variabel
x = 5
y = "John"
print(x)
print(y)

x = 4 
x = "Sally" 
print(x)

#2 input output
npm  = input("Masukan NPM :")
hitung = 0
while(hitung < 95):
    print("Halo, " + str(npm) + " Apa Kabar?")
    hitung = hitung +1

#No.1    
npm =  input("Masukan NPM :")
hitung = 0
while(hitung < 14):
    print("Halo, " + str(npm[4:7]) + " Apa Kabar?")
    hitung = hitung +1
    
#No.2
npm = input("Masukan NPM :")
print("Halo, " + str(npm[-3]) + " Apa Kabar?")

#3 operator dasar aritmatika
#1 penjumlahan
x = 5
y = 3

print(x + y)
#2 pengurangan
x = 5
y = 3

print(x - y)
#3 perkalian
x = 5
y = 3

print(x * y)
#4 pembagian
x = 12
y = 3

print(x / y)
#5 perubahan data ke string
kamu = 'cantik'
kamu2 = 1
kamuitu = kamu + str(kamu2)
print (kamuitu)
#6 string ke int
a = 5
b = str(a)
print(b)
#4 sintak perulangan
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#5 kondisi
a = 33
b = 200
if b > a:
 print("b is greater than a")
#6 error
 x = int(input('Enter a number: '))

whille x%2 == 0:
    print('You have entered an even number.')
else:
    print ('You have entered an odd number.')
#penanganan error
 x = int(input('Enter a number: '))

while x%2 == 0:
    print('You have entered an even number.')
else:
    print ('You have entered an odd number.')
#7 try except
a = 2
b = "4"

try:
    c = a + b
    print(c)
except TypeError:
    print ("Beda Tipe Data Cuk")