# PROGRAM UTAMA//////////////////////////////////////////////////////////////////
print("======================================================")
print()
print("SELAMAT PAGI MAS/MBA😄..., APAKAH ANDA PENJUAL ATAU PEMBELI?")
print("(Isi dengan 'Penjual' atau 'Pembeli')")
print()
print("======================================================")

box = []
box.append("Lampu tidur")
box.append("Permen yupi")
box.append("HADIAH UTAMA IPHONE 14")
box.append("Buku atlas dunia")


def email():
    print("===================================================================================")
    print()
    print("Silahkan login dengan akun anda.")
    uname = input("Email/Username: ")
    upass = input("Password: ")
    print()
    print("===================================================================================")
    if uname == "firzandiads" and upass == "123123qwe" or uname == "firzandi@gmail.com" and upass == "123123qwe":
        verivikasi()
    else:
        print("Email/Username atau Password kamu SALAH!")
        email()


def verivikasi():
    print("=========================================")
    print()
    print("Silahkan isi data diri kamu di bawah ini!")
    namaBeli = input("Nama lengkap pembeli/penerima:")
    alamatBeli = input("Alamat tujuan:")
    print()
    print("=========================================")
    print()


def fungsiawal():
    anda = input("PILIH OPSI:")
    print()
    print()
    # PROGRAM PENJUAL//////////
    if anda == "Penjual" or "penjual" or "PENJUAL":
        email()
    # PROGRAM PEMBELI////////////////////////////////////////////////////////////////
    elif anda == "Pembeli" or "pembeli" or "PEMBELI":
        print("===================================================================================")
        print()
        print("Apakah anda ingin membeli Mystery Box dengan hadiah utama SMARTPHONE IPHONE 20 ini?")
        print("1. Ya, saya bersedia membeli!")
        print("2. Batalkan beli")
        print()
        print("===================================================================================")

        beli = input("MENU:")

        # ///////////////////////////////////////////////////////////////////////////////
        if beli == "1":
            print("=========================================")
            print()
            print("Silahkan isi data diri kamu di bawah ini!")
            namaBeli = input("Nama lengkap pembeli/penerima:")
            alamatBeli = input("Alamat tujuan:")
            print()
            print("=========================================")
            print()

            print()
            print("=========================================")
            print()
            print("Dengan identitas pembeli di bawah ini!")
            print("Nama: ", namaBeli)
            print("Alamat: ", alamatBeli)
            print("Mendapatkan barang... ", box.pop())
            print()
            print("=========================================")


        # ELSE///////////////////////////////////////////////////////////////////////////
        else:
            print("Maaf kode salah")


fungsiawal()