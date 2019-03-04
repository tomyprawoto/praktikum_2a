# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:54:28 2019

@author: user
"""

#Soal Praktek
#nomor 1
print ("###   ###   ###########   ###   ###   #########   #########   #########")
print ("###   ###   ###########   ###   ###   #########   #########   #########")
print ("###   ###          ###    ###   ###   ##     ##   ##     ##   ###      ")
print ("###   ###         ###     ###   ###   ##     ##   ##     ##   ###      ")
print ("###   ###        ###      #########   ##     ##   ##     ##   ###      ")
print ("###   ###       ###             ###   ##     ##   ##     ##   #########")
print ("###   ###      ###              ###   ##     ##   ##     ##   #########")
print ("###   ###     ###               ###   ##     ##   ##     ##         ###")
print ("###   ###    ###                ###   ##     ##   ##     ##         ###")
print ("###   ###   ###                 ###   #########   #########   #########")
print ("###   ###  ###                  ###   #########   #########   #########")
       
#nomor 2
npm = input("Masukan NPM :")
hitung = 0
while(hitung <= 87):
     print("Halo, " +  str(npm) + " Apa Kabar?")
     hitung = hitung +1
     
     
#nomor 3
npm = input("Masukan NPM :")
hitung = 0
while(hitung <= 15):
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
g = 5
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
j = "jantung"
k = 1
print("Tetap" +str(j),k)

l = input("Masukan NPM Kamu :")
print("NPM Kamu Adalah : "+l)

m = 10
n = 2
o = j + k
p = j * k 
q = j - k
r = j / k
s = "10"
print(o,p,q,r)
print(int(s))
print(str(m))
t = 12
for u in range(t):
    print("Ini Yang Ke : "+str(u))
while(t <= 15):
    print(" Ini yang Betul")
    t = t + 1
v = 12
if(v==12):
    print("Dua Belas")
if(v==13):
    print("Tiga Belas")
else:
    print("Dua Belas")
if(v==11):
    print("Sebelas")
elif(v==12):
    print("Sebelas")
else :
    print("Tiga Belas")
w = 10
x = "10"
try:
    y = w+x
    print(y)
except TypeError:
    print("We Are Different")
