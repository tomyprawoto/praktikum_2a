# -*- coding: utf-8 -*-
"""

@author: Tomy
"""


#No 1
print("###  ###  ###########  ###   ###  #########  ##########  ###")
print("###  ###  ###########  ###   ###  #########  ##########  ###")
print("###  ###         ###   ###   ###  ##     ##         ###  ###")
print("###  ###        ###    ###   ###  ##     ##         ###  ###")
print("###  ###       ###     #########  ##     ##  ##########  ###")
print("###  ###      ###            ###  ##     ##  ##########  ###")
print("###  ###     ###             ###  ##     ##         ###  ###")
print("###  ###    ###              ###  ##     ##         ###  ###")
print("###  ###   ###               ###  #########  ##########  ###")
print("###  ###  ###                ###  #########  ##########  ###")

#No 2
npm = input("Masukan NPM :")
hitung = 0
while(hitung < 51):
    print("Halo, " + str(npm) + " Apa kabar?")
    hitung = hitung +1

#No 3
npm = input("Masukan NPM :")
hitung = 0
while(hitung < 9):
    print("Halo, " + str(npm[0:7]) + " Apa kabar?")
    hitung = hitung +1

#No 4
npm = input("Masukan NPM :")
print("Halo, " + str(npm[-3]) + " Apa kabar?")

#No 5
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
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
print(d,e,f)

#No 10
print(a,b,c,g)

#No 11
print(a,b,c,g)

x = "mantan 1"
z = 5
print("Tetap" +str(x),z)

l = input("Masukan NPM :")
print("NPM Kamu Adalah : "+l)

m = 100
n = 25
o = m + n
p = m * n 
q = m - n
r = m / n
s = "100"
print(o,p,q,r)
print(int(s))
print(str(m))

t = 12
for u in range(t):
    print("Ini Yang Ke : "+str(u))

while(t <= 15):
    print("Yeyyyyyyy Betul")
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
    print("Gabisa Coyyyy")
