class Mahasiswa:
    def __init__(self, nama, nim, tanggalLahir):
        self.nama = nama
        self.nim =  nim
        self.tanggalLahir = tanggalLahir
        self. matkul = []
        
    def tambahMatkul(self, matkul):
        self.matkul.append(matkul)
        print (f"mahasiswa {self.nama} berhasil input {matkul.nama}")
        print("-"*40)
       
        
    def cetakMatkul(self):
        print (f"Daftar Mata Kuliah {self.nama} : ")
        for i in self.matkul:
            print ('-',end='')
            i.infoMatkul()
            
    def infoMahasiswa(self):
        print ("INFO MAHASISWA")
        print (f"Nama : {self.nama}")
        print (f"NIM : {self.nim}")
        print (f"Tanggal Lahir : {self.tanggalLahir}")
        
class MataKuliah:
    def __init__(self, kodeMatkul,nama, sks):
        self.kodeMatkul = kodeMatkul
        self.nama = nama
        self.sks = sks
        
    def infoMatkul(self):
        print (f" {self.nama}, SKS: {self.sks}")
        
Mahasiswa1 = Mahasiswa("budi",5220411069, "30 September 1958")        
Mahasiswa2 = Mahasiswa("Ella",5220411074, "7 Agustus 2006")

Matkul1 = MataKuliah(2202, "Pemograman Berorientasi Objek", 4)
Matkul2 = MataKuliah(2203, "Metode Penelitian", 2)
Matkul3 = MataKuliah(2204, "Kalkulus", 2)

Mahasiswa1.tambahMatkul(Matkul1)
Mahasiswa1.tambahMatkul(Matkul2)

Mahasiswa2.tambahMatkul(Matkul3)

Mahasiswa1.cetakMatkul()
Mahasiswa2.cetakMatkul()

print('='*50)

class Kendaraan:
    def __init__(self, nama, roda):
        self.nama = nama
        self.roda = roda
        
    def info(self):
        print (f"Nama : {self.nama}, Jumlah Roda: {self.roda}")
    
mobil = Kendaraan("Mobil", 4)

print(mobil.nama)
print(mobil.roda)
mobil.info()

print('='*50)
print('<==========BANK==========>')

class RekeningBank:
    def __init__(self, saldoAwal):
        self.__saldo = saldoAwal
        
    def tarik(self,jumlah):
        if jumlah <= self.__saldo:
            self.__saldo -+ jumlah
            print(f"Penarikan saldo Berhasil!! \nSaldo yang anda miliki senilai {self.__saldo}")
        else:
            print("Saldo tidak Mencukupi!")
    
rekening = RekeningBank(1000000)
# print(rekening.__saldo)
# print(rekening.tarik(0))
rekening.tarik(1000000)

print('='*50)
print('<==========HEWAN==========>')

class Hewan:
    def __init__(self, nama):
        self._nama = nama
        
    def suara(self):
        print("bunyi Hewan!")
       
        
class Serigala(Hewan):
    # def __init__(self, nama):
        # super().__init__(nama)
        
    def suara(self):
        print(f'{self._nama} mengeluarkan Suara Auuuuu!')
        
serigala = Serigala("Serigala")
serigala.suara()

print('='*50)
print('<==========MENU==========>')

class Menu:
    def __init__(self, nama, deskripsi, harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.__harga = harga
        print("-"*30)

    def dipesan(self):
        print(f"Menu      : {self.nama} telah dipesan")
        print(f"Deskripsi : {self.deskripsi}")
        print(f"Harga     : {self.__harga}")
        
    def harga(self):
        print(f"Menu      : {self.nama}")
        print(f"Deskripsi : {self.deskripsi}")
        print(f"Harga     : {self.__harga}")
        
        

menu1 = Menu("Nasi goreng","Nasi digoreng dengan telor dan bumbu", 10000)
menu1.dipesan()
menu2 = Menu("Mie ayam","Mie dengan potongan ayam dan pangsit", 8000)
menu2.dipesan()
print('-'*20)
menu1.harga()
menu2.harga()

print('='*50)
print('<==========BUKU==========>')

class Buku:
    def __init__(self, judul, pengarang, tahunTerbit,waktu):
        self.judul = judul
        self.pengarang = pengarang
        self.tahunTerbit = tahunTerbit
        self.__waktu = waktu
        
    def dipinjam(self,hari):
        if hari <= self.__waktu:
            self.__waktu -= hari
            print(f'Sisa waktu peminjaman {self.__waktu} hari')
        else:
            print("Waktu peminjaman anda telah habis")

    def deskripsi(self):
        print(f"Judul        : {self.judul}")
        print(f"Pengarang    : {self.pengarang}")
        print(f"Tahun Terbit : {self.tahunTerbit}")
        print("Saya Pinjam Buku ini ")
        print("-"*30)

    def dikembalikan(self):
        print(f"Judul        : {self.judul}")
        print(f"Pengarang    : {self.pengarang}")
        print(f"Tahun Terbit : {self.tahunTerbit}")
        print("Saya kembalikan Buku ini ")


buku1 = Buku("Laskar Pelangi","Adrea Hirata", 2005,30)
buku1.deskripsi()
buku1.dipinjam(20)

buku2 = Buku("langit","Tere Liye", 2013,30)
buku2.deskripsi()
buku2.dipinjam(5)

print("="*50)