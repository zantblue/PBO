# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RRgeh-PgUnfp9bOuWzeZ5nG99hCGkRLy
"""

# Apa itu Object Oriented Programing
#  1.di python semuanya adalah objek, seperti list, string
#  2.di python objek disebut class
#  3.OOP itu memungkinkan kita buat objek sendiri termasuk methods dan atributnya.

print(type("saya adalah string"))

class Namaclass:
  def __init__(self, nama_atribut1,nama_atribut2):
    self.nama_atribut1 = nama_atribut1
    self.nama_atribut2 = nama_atribut2

  def nama_method(self):
    return #nulis fungsi

class person:
  def __init__(self, nama, umur):
    self.nama = nama
    self.umur = umur

  def introduce(self):
      return f'Halo Nama Saya Adalah {self.nama} dan Umur saya {self.umur} tahun'
#membuat objek person dari kelas person
person = person("Mizuru", 19)

#memanggil metode introduce dan mengakses atribut person dan umur menggunakan self
print(person.introduce())

class Mahasiswa:
  def __init__(self, nama, nim, jurusan):
    self.nama = nama
    self.nim = nim
    self.jurusan = jurusan
    #inisialisasi daftar nilai list kosong
    self.nilai = []

  def tambahnilai(self, matakuliah, nilai):
    self.nilai.append([matakuliah,nilai])

  def rata_rata_nilai(self):
    total_nilai = sum(nilai for matakuliah, nilai in self.nilai)
    rata_rata = total_nilai / len (self.nilai) if self.nilai else 0
    return rata_rata

  def info(self):
    print(f"Nama :{self.nama}")
    print(f"NIM:{self.nim}")
    print(f"Jurusan:{self.jurusan}")
    print(f"Rata-rata_Nilai:{self.rata_rata_nilai()}")

mahasiswa1 = Mahasiswa("Mizuru", 5220411093, "Informatika")
mahasiswa1.tambahnilai("Apti",90)
mahasiswa1.tambahnilai("Alpro", 85)
mahasiswa1.tambahnilai("PBO", 82)
mahasiswa1.info()