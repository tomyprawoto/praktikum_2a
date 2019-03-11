# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 08:18:19 2019

@author: Dwi
"""
#chapter3
#no1
def fungsi(x):
  return 5 * x

print(fungsi(3))
print(fungsi(5))
print(fungsi(9))

#no2
import mymodule

a = mymodule.person1["age"]
print(a)
  
#no3
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("uwi", 19)
p1.myfunc()

#no4
#import mymodule
#c = 300
#d = 10

#e = belajar.pengurangan(c,d)
#print (e)

#no5
#from mymodule import *
#print (penulisan(int(input("write your NPM"))))

#no6
from folder import kalkulator

a = 100
b = 50

hasil1=kalkulator.Penambahan(a,b)
hasil2=kalkulator.Pengurangan(a,b)
hasil3=kalkulator.Perkalian(a,b)
hasil4=kalkulator.Pembagian(a,b)

print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)

#no7
#from folder.Mahasiswa import Mahasiswa

#mhs1.tampilkanprofil()
#mhs2.tampilkanprofil()
#print ("totalnya adalah", Mahasiswa.jumlahMahasiswa)

#penanganan Eror
#def penanganan_error(c,d):
#    try :
#        c = c+d
#        print(e)
#    except TypeError:
#        print("beda ya gais")