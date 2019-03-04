#Boolean
var = True
print(var)

#String
var = "Kadek Diva Krishna Murti"
print(var)

#Integer
var = 1174006
print(var)

#Float
var = 5.5
print(var)

#Hexadecimal
var = 0x5
print(var)

#Complex
var = 5j
print(var)

#List
var = [1,2,3,4,5]
print(var)
print(var[0])

#Tuple
var = (1,2,3,4,5)
print(var)
print(var[0])

#Set
var = {1,2,3,4,5}
print(var)


#Dictionary
var = {1:'satu', 2:'dua', 'tiga':3}
print(var)
print(var[1])

#Input dan Output
nama = input('Masukan nama anda : ')
print('Hallo, '+nama)


#Operator Dasar Aritmatika
#Pertambahan
angka1 = 2
angka2 = 3
hasil = angka1+angka2
print(hasil)

#Pengurangan
angka1 = 5
angka2 = 3
hasil = angka1-angka2
print(hasil)

#Perkalian
angka1 = 2
angka2 = 3
hasil = angka1*angka2
print(hasil)

#Pembagian
angka1 = 6
angka2 = 3
hasil = angka1/angka2
print(hasil)

#Modulus
angka1 = 7
angka2 = 3
hasil = angka1%angka2
print(hasil)

#Perpangkatan
angka1 = 6
angka2 = 2
hasil = angka1**angka2
print(hasil)

#Pembulatan Pembagian
angka1 = 7
angka2 = 3
hasil = angka1//angka2
print(hasil)

#Mengubah Tipe Data
#String ke Integer
var_str = '5'
var_int = int(var_str)
print(var_int)

#Integer ke String
var_int = 5
var_str = str(var_int)
print(var_str)

#While Loop
hitung = 1
while (hitung < 6):
    print (hitung)
    hitung += 1

#For Loop
angka = [1,2,3,4,5]
for a in angka:
    print(a)

#Nested Loop
i = 1
while(i < 5):
    j = 1
    while(j <= 5):
        print('#')
        j += 1
    i += 1
    
#If
angka = 5
if angka > 0:
    print(angka, "adalah bilangan positif.")

#If Else
angka = -5
if angka > 0:
    print(angka, "adalah bilangan positif.")
else:
    print(angka, "adalah bilangan negatif.")

#Elif
angka = 0
if angka > 0:
    print(angka, "adalah bilangan positif.")
elif angka < 0:
    print(angka, "adalah bilangan negatif.")
else:
    print(angka, "adalah bilangan nol.")


#Kondisi di dalam kondisi
if angka > 0:
    print(angka, "adalah bilangan positif.")
    if angka > 50:
        print(angka, "adalah bilangan lebih dari 50.")
    else:
        print(angka, "adalah bilangan kurang dari 50.")
elif angka < 0:
    print(angka, "adalah bilangan negatif.")
else:
    print(angka, "adalah bilangan nol.")
    
#Try Except
try:
  print(te)
except:
  print("Terjadi kesalahan penulisan kode")
finally:
  print("Try except telah selesai") 

#Jawaban No. 1
  
print(1174006%3)
#mod3 = 1

print("  ##   ## #########    ###  ######   ######   ########")
print("#### #### ########   ##### ###  ### ###  ### ###")
print(" ###  ###     ###  ### ### ###  ### ###  ### ###")
print(" ###  ###    ###  ######## ###  ### ###  ### ########")
print(" ###  ###   ###        ### ###  ### ###  ### ###   ###")
print(" ###  ###  ###         ###  ######   ######   #######")

#Jawaban No. 2

npm = input("Input : ")
ulang = 1
while(ulang <= 6):
    print("Halo, "+str(npm)+" apa kabar?")
    ulang += 1

#Jawaban No. 3

npm = input("Input : ")
ulang = 1
while(ulang <= 6):
    print("Halo, "+str(npm[4:7])+" apa kabar?")
    ulang += 1
    
#Jawaban No. 4
    
npm = input("Input : ")
print("Halo, "+str(npm[-3])+" apa kabar?")

#Jawaban No. 5

a = 1
b = 1
c = 7
d = 4
e = 0
f = 0
g = 6

npm = [a,b,c,d,e,f,g]

for n in npm:
    print(n, end ="")

print()
#Jawaban No. 6

print(a+b+c+d+e+f+g)

#Jawaban No. 7

print(a*b*c*d*e*f*g)

#Jawaban No. 8

for n in npm:
    print(n)
         
#Jawaban No. 9
    
for n in npm:
    if(n % 2 == 0):
        if(n != 0):
            print(n, end ="")

print()        
#Jawaban No. 10
        
for n in npm:
    if(n % 2 != 0):
        print(n, end ="")

print()
#Jawaban No. 11

print(c)
