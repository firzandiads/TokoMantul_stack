box = []
box.append("Mousepad")
box.append("Casing OPPO")
box.append("Lampu tidur")
box.append("Permen yupi")
box.append("HADIAH UTAMA IPHONE 14")
box.append("Buku atlas dunia")
box.append("Mobil remot")

statusBrg = ['-> Sebagai tumpukan barang yang paling bawah', '', '', '', '-> Sebagai hadiah utama', '', '-> Sebagai tumpukan barang yang paling atas']

noBrg = ['7. ','6. ','5. ','4. ','3. ','2. ','1. ']

def mengecekBrg():
    print("=================================================================\n")
    print("  BARANG-BARANG PADA TUMPUKAN GUDANG YANG MASIH TERSEDIA: \n")
    for noBrg1,box1,statusBrg1 in zip(noBrg,box,statusBrg):
        print ("  ",noBrg1,box1,statusBrg1)
    print()
    print("=================================================================\n\n")
    mainmenu()

def kodesalah():
    print("MAAF KODE SALAH")
    tampilan1()

def mainmenu():
    print("===============================================")
    print("==                                           ==")
    print("==    - - - - M A I N   M E N U - - - -      ==")
    print("==                                           ==")
    print("==    1. Ada pembeli yang ingin membeli      ==")
    print("==    2. Cek barang                          ==")
    print("==                                           ==")
    print("==    0. EXIT                                ==")
    print("==                                           ==")
    print("===============================================")
    menuPenjual = input("OPSI: ")
    print()
    print()
    if menuPenjual=="1":
        tampilan2penjual()
    elif menuPenjual=="2":
        mengecekBrg()
    elif menuPenjual=="0":
        tampilanExit()
    else :
        kodesalah()

def tampilanExit():
    print("    ///////////////////////////////////////////////////////////////////////////////")
    print("   //                                                                           //")
    print("  //    TERIMA KASIH TELAH MENGGUNAKAN LAYANAN PADA TOKO MANTUL KAMI😊😊💕     //")
    print(" //                                                                           //")
    print("///////////////////////////////////////////////////////////////////////////////\n\n")

def tampilan2penjual():
    print("=============================================\n")
    print("  SILAHKAN ISI DATA PEMBELI DI BAWAH INI!\n")
    namaBeli = input("   Nama lengkap pembeli: ")
    alamatBeli = input("   Alamat tujuan: ")
    nomorBeli = input("   Nomor HP: ")
    print()
    print("=============================================\n\n")

    print("===============================================\n")
    print("    Dengan identitas pembeli di bawah ini!     \n")
    print("      Nama: ", namaBeli)
    print("      Alamat: ", alamatBeli)
    print("      Nomor HP: ", nomorBeli)
    print()
    print("      Mendapatkan barang... ", box.pop(),)
    print()
    print("===============================================\n\n")
    
    print("=====================================")
    print("==                                 ==")
    print("==    APAKAH ADA PEMBELI LAGI?     ==")
    print("==                                 ==")
    print("==      1. Ya                      ==")
    print("==      2. Tidak                   ==")
    print("==      3. Main Menu               ==")
    print("==                                 ==")
    print("==      0. EXIT                    ==")
    print("==                                 ==")
    print("=====================================")
    beliLagi1 = input("OPSI: ")
    print()
    print()
    if beliLagi1=="1":
        tampilan2penjual()
    elif beliLagi1=="2":
        tampilan1()
    elif beliLagi1=="3":
        mainmenu()
    elif beliLagi1=="0":
        tampilanExit()
    else :
        kodesalah()

def tampilan2pembeli():
    print("=============================================\n")
    print("  SILAHKAN ISI DATA KAMU DI BAWAH INI!\n")
    namaBeli = input("   Nama lengkap penerima: ")
    alamatBeli = input("   Alamat tujuan: ")
    nomorBeli = input("   Nomor HP: ")
    print()
    print("=============================================\n\n")

    print("===============================================\n")
    print("    Dengan identitas kamu di bawah ini!     \n")
    print("      Nama: ", namaBeli)
    print("      Alamat: ", alamatBeli)
    print("      Nomor HP: ", nomorBeli)
    print()
    print("      Mendapatkan barang... ", box.pop(),)
    print()
    print("===============================================\n\n")
    
    
    print("==========================================")
    print("==                                      ==")
    print("==   APAKAH KAMU INGIN MEMBELI LAGI?    ==")
    print("==                                      ==")
    print("==     1. Ya                            ==")
    print("==     2. Tidak                         ==")
    print("==                                      ==")
    print("==     0. EXIT                          ==")
    print("==                                      ==")
    print("==========================================")
    beliLagi2 = input("OPSI: ")
    print()
    print()
    if beliLagi2=="1":
        tampilan2pembeli()
    elif beliLagi2=="2":
        tampilan1()
    elif beliLagi2=="0":
        tampilanExit()
    else :
        kodesalah()

def penjualDef():
    print("==========================================\n")
    print("    SILAHKAN LOGIN DENGAN AKUN ANDA\n     ")
    uname = input("     Email/Username: ") 
    upass = input("     Password: ")
    print()
    print("==========================================")
        
    if uname=="firza" and upass=="1234" or uname=="ti@gmail.com" and upass=="1234" :
        print("Anda Berhasil LOGIN\n\n")
        mainmenu()

    else :
        print("Email/Username atau Password kamu SALAH!\n\n")
        penjualDef()
        
def pembeliDef(): 
    print("==============================================================================================")  
    print("==                                                                                          ==")     
    print("==  Apakah anda yakin ingin membeli Mystery Box dengan hadiah utama SMARTPHONE IPHONE 14?   ==")
    print("==                                                                                          ==") 
    print("==     1. Ya, saya bersedia membeli!                                                        ==")
    print("==     2. Batalkan beli                                                                     ==")
    print("==                                                                                          ==") 
    print("==     0. EXIT                                                                              ==")
    print("==                                                                                          ==") 
    print("==============================================================================================")  
    beli = input("PILIH OPSI:")
    print()
    print()
        
    if beli=="1" :
        tampilan2pembeli()
    elif beli=="2":
        tampilan1()
    elif beli=="0":
        tampilanExit()
    else :
        kodesalah()
        
def tampilan1():
    print("\n=======================================================================")
    print("==                                                                   ==")
    print("==              - - - - T O K O   M A N T U L - - - -                ==")
    print("==                                                                   ==")
    print("==   SELAMAT PAGI MAS/MBA😊..., APAKAH ANDA PENJUAL ATAU PEMBELI?    ==")
    print("==     *Isi 'Penjual' atau 'Pembeli' untuk lanjut                    ==")
    print("==     *Isi '0' untuk mengakhiri                                     ==")
    print("==                                                                   ==")
    print("=======================================================================")
    anda = input("ISI OPSI: ")
    print()
    print()
    if anda=="Penjual" :
        penjualDef()
    elif anda=="penjual" :
        penjualDef()
    elif anda=="PENJUAL" :
        penjualDef()
        
    elif anda=="Pembeli" :
        pembeliDef()  
    elif anda=="pembeli" :
        pembeliDef()  
    elif anda=="PEMBELI" :
        pembeliDef()
        
    elif anda=="0" :
        tampilanExit()
        
    else :
        kodesalah()
        
tampilan1()