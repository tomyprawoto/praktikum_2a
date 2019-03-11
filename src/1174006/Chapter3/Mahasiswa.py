# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:56:31 2019

@author: vanerz
"""

class Mahasiswa:
    jumlahMahasiswa = 0
    
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = nama
        Mahasiswa.jumlahMahasiswa +=1
            
    def tampilkanProfil(self):
        print("NPM :", self.npm)
        print("Nama :", self.nama)
        print()