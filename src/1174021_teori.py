#Teori 
#No.1 Variabel
nama = 'Muhammad Fahmi'
print (nama)

#tipe data Boolean
print(True)

#tipe data String
print("Muhammad Fahmi")
print('Politeknik Pos Indonesia')

#tipe data Integer
print(20)

#tipe data Float
print(1.5)

#tipe data List
print([1,2,3,4,5])
print(["satu", "dua", "tiga"])

#tipe data Tuple
print((1,2,3,4,5))
print(("satu", "dua", "tiga"))

#tipe data Dictionary
print({"nama":"Fahmi", 'umur':19})

#No.2 Input Output
nama = input("Masukkan Nama : ")
print(nama)

# Mengambil input
nama = raw_input("nama: ")
umur = input("umur: ")

# Menampilkan output
print "Assalamualaikum",nama,"umur kamu",umur,"tahun"

#No.3 Operator Dasar Aritmatika
#Pertambahan
angka1 = 5
angka2 = 5
hasil = angka1+angka2
print(hasil)

#Pengurangan
angka1 = 5
angka2 = 5
hasil = angka1-angka2
print(hasil)

#Perkalian
angka1 = 5
angka2 = 5
hasil = angka1*angka2
print(hasil)

#Pembagian
angka1 = 5
angka2 = 5
hasil = angka1/angka2
print(hasil)

#Modulus
angka1 = 5
angka2 = 5
hasil = angka1%angka2
print(hasil)

#Perpangkatan
angka1 = 5
angka2 = 5
hasil = angka1**angka2
print(hasil)

#Pembulatan Pembagian
angka1 = 5
angka2 = 5
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

#No.4 Perulangan 
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
	
#No.5 Sintak untuk memilih kondisi
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
	
#No.6 Jenis Error

#NO.7 Try Except
try:
  print(te)
except:
  print("Telah terjadi kesalahan dalam penulisan kode")
finally:
  print("Try except telah selesai") 



