# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:06:54 2019

@author: Aegis
"""
#No 1
print("###  ###  ###########  ###   ###  #########  ######  ###########")
print("###  ###  ###########  ###   ###  #########  ######  ###########")
print("###  ###         ###   ###   ###  ##     ##     ###         ### ")
print("###  ###        ###    ###   ###  ##     ##     ###        ###  ")
print("###  ###       ###     #########  ##     ##  ######       ###   ")
print("###  ###      ###            ###  ##     ##  ######      ###    ")
print("###  ###     ###             ###  ##     ##  ###        ###     ")
print("###  ###    ###              ###  ##     ##  ###       ###      ")
print("###  ###   ###               ###  #########  ######   ###       ")
print("###  ###  ###                ###  #########  ######  ###        ")

#No 2
npm = input("Masukan NPM :")
hitung = 0
while(hitung < 27):
    print("Halo, " + str(npm) + " Apa kabar?")
    hitung = hitung +1

#No 3
npm = input("Masukan NPM :")
hitung = 0
while(hitung < 9):
    print("Halo, " + str(npm[4:7]) + " Apa kabar?")
    hitung = hitung +1

#No 4
npm = input("Masukan NPM :")
print("Halo, " + str(npm[-3]) + " Apa kabar?")

#No 5
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

#No 6
print(h)

#No 7
print(i)

#No 8
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

#No 9
print(d,f)

#No 10
print(a,b,c,g)

#No 11
print(a,b,c,g)

j = "hati"
k = 1
print("Tetap" +str(j),k)

l = input("Masukan NPM :")
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
    print("Yap Ini Betul")
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