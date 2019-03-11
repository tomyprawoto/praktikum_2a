# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Soal Teori
#No.1 Number
x = 5 
print(x, "tipenya adalah ", type(x))
x = 2.0
print(x, "tipenya adalah ", type(x))
x = 1+2j
print(x, "tipenya adalah ",type(x))

#No.1 String 
kalimat = "Nama saya Nico"

print(kalimat)      # menampilkan string lengkap
print(kalimat[0])   # menampilkan karakter pertama
print(kalimat[-1])  # menampilkan karakter terakhir
print(kalimat[4:7]) # menampilkan dari indeks 4 - 6
print(kalimat[:4])  # menampilkan dari indeks 0 - 3

#No.1 List
a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

#No.1 Tuple
white = (255,255, 255)
red = (255,0,0)
print(white)
print(red[0])
print(red[1])

#No.1 Set
# set integer 
my_set = {1,2,3} 
print(my_set) 

# set dengan menggunakan fungsi set() 
my_set = set([1,2,3]) 
print(my_set) 

# set data campuran 
my_set = {1, 2.0, "Python", (3,4,5)} 
print(my_set) 

# bila kita mengisi duplikasi, set akan menghilangkan salah satu 
# output: {1,2,3} 
my_set = {1,2,2,3,3,3} 
print(my_set) 

#No.2
npm  = input("Masukan NPM :")
print(npm)

#No.3 Penjumlahan
a = 2
b = 3
print(a+b)

#No.3 Pengurangan
a = 2
b = 3
print(a-b)

#No.3 Perkalian
a = 2
b = 3
print(a*b)

#No.3 Pembagian
a = 2
b = 3
print(a/b)

#3.Mengubah Integer ke String
npm  = 1174096
print("Halo, " + str(npm) + " Apa Kabar?")

#3. Mengubah String Ke Integer
npm  = "5"
print(int(npm))

#4. Pengulangan while
i = 1
while i < 9:
  print(i)
  i += 1

#4. Pengulangan For
kue = ["Bolu", "Bakpao", "Apem"]
for x in kue:
  print(x)
  
#5.If
x = 100
y = 20
if x > y:
  print("x lebih besar dari y")
else:
  print("x tidak lebih besar dari y")

#7. try dan except
x = 17
y = "19"
try:
    z = x+y
    print(z)
except TypeError:
    print("Berbeda tipe datanya")





#Soal Praktek
#No.1
print("###  ###  ##########  ###   ###  #########  #########  #########")
print("###  ###  ##########  ###   ###  #########  #########  #########")
print("###  ###        ###   ###   ###  ###   ###  ###   ###  ###      ")
print("###  ###       ###    ###   ###  ###   ###  ###   ###  ###      ")
print("###  ###      ###     #########  ###   ###  #########  #########")
print("###  ###     ###            ###  ###   ###        ###  ###   ###")
print("###  ###    ###             ###  ###   ###        ###  ###   ###")
print("###  ###   ###              ###  #########  #########  #########")
print("###  ###  ###               ###  #########  #########  #########")
      
#No.2
npm  = input("Masukan NPM :")
hitung = 0
while(hitung < 96):
    print("Halo, " + str(npm) + " Apa Kabar?")
    hitung = hitung +1

#No.3    
npm =  input("Masukan NPM :")
hitung = 0
while(hitung < 15):
    print("Halo, " + str(npm[4:7]) + " Apa Kabar?")
    hitung = hitung +1
    
#No.4
npm = input("Masukan NPM :")
print("Halo, " + str(npm[-3]) + " Apa Kabar?")

#No.5
a = 1
b = 1
c = 7
d = 4
e = 0
f = 9
g = 6
h = a+b+c+d+e+f+g
i = a*b*c*d*e*f*g

print(a,b,c,d,e,f,g)

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
print(d,e,g)

#No.10
print(a,b,c,f)

#No.11
print(a,b,c,)

