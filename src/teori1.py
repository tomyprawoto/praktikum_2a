# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:29:17 2019

@author: lenovo
"""

#no1
#integer
x = 1
y = 1.2
z = 2+5j

print(type(x))
print(type(y))
print(type(z))

#string
a = "Hello, World!"
print(a[1]) #untuk mencetak huruf terpilih tidak semua

b = "Hello, World!"
print(b[2:5]) #mencetak huruf dari rentang huruf ke 2-5

a = " Hello, World! "
print(a.strip()) #mengembalikan "Hello, World!"

a = "Hello, World!"
print(len(a)) #mencetak berapa jumlah huruf yang ada

a = "Hello, World!"
print(a.lower()) #menjadikan lowercase

a = "Hello, World!"
print(a.upper()) #menjadikan uppercase

#boolean
a = 12
b = 10
if (a < b):
  print("Isi variabel a lebih kecil daripada variabel b")
elif (a > b):
  print("Isi variabel a lebih besar daripada variabel b")
else:
  print("Isi variabel a sama dengan variabel b")
    
#no2
nama = input("Masukan namamu :")
print("Halo, " + str(nama))

#no3
x = 4
y = 2
print(x + y) #penambahan

x = 4
y = 2

print(x - y) #mengurangan

x = 4
y = 2

print(x * y) #perkalian

x = 5
y = 3

print(x / y) #pembagian

x = 6
y = 2

print(x % y) #modulus

#no4
#perulangan while
i = 1
while i < 6:
  print(i)
  i += 1
  
#perulangan for
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#no5
#If statement
a = 33
b = 200
if b > a:
  print("b is greater than a")

#elif statement
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#else statement
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#no7
try:
  print(x)
except:
  print("An exception occurred")