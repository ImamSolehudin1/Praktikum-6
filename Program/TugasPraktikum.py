nama = []
nim = []
tugas = []
uts = []
uas = []

def pilih():
    print ("\n")
    print ("==========================================")
    print ("=============== MENU PILIHAN =============")
    print ("==========================================")
    print ("(1) Tampilkan")
    print ("(2) Tambah")
    print ("(3) Ubah")
    print ("(4) Hapus")
    print ("==========================================")
    pilih = input(" Pilih Menu : ")
    
    if pilih == '1':
        tampilkan()
    elif pilih == '2':
        tambah()
    elif pilih == '3' :
        ubah()
    elif pilih == '4':
        hapus()
    else:
        print ("Inputan Salah!")
    print (" ")
    print (" ")

def judul():
    print ("==========================================")
    print ("===PROGRAM MENAMPILKAN NILAI MAHASISWA====")
    print ("==========================================")


def tambah():
    judul()
    print("\t\tTambah Data")
    print("="*42)
    nama1 = input("Nama        : ")
    nama.append(nama1)
    nim1 = int(input("NIM         : "))
    nim.append(nim1)
    tugas1 = int(input("Nilai Tugas : "))
    tugas.append(tugas1)
    uts1 = int(input("Nilai UTS   : "))
    uts.append(uts1)
    uas1 = int(input("Nilai UAS   : "))
    uas.append(uas1)
    print (" ")
    print ("\tDATA BERHASIL DI SIMPAN !")

def tampilkan():
    judul()
    print("\t\tMenampilkan Data")
    print("="*42)

    for i in range (len(nim)):
        print("%d.  Nama         :  %s" % (i+1, nama[i]))
        print("    Nim          :  %s" % nim[i])
        print("    Nilai Tugas  :  %.f" % tugas[i])
        print("    Nilai UTS    :  %.f" % uts[i])
        print("    Nilai UAS    :  %.f" % uas[i])

def hapus():
    print("Menghapus Data")
    print("="*42)
    h = int(input("Masukan No Urut : "))
    if (h > len(nama[h])):
        print("Data Salah")
    else:
        nama.remove(nama[h])
    print("Data Berhasil Dihapus.")

def ubah():
    print("Mengubah Data")
    print("="*42)
    u = int(input("Masukan No Urut : "))
    if (u > len(nama[u])):
        print('Inputan Salah!')
    else:
        nama2 = input('Nama Baru : ')
        nama[u] = nama2
    print("Data Berhasil DIubah")
if __name__=="__main__":
    while (True):
        pilih()
