from hitung import perhitungan
class masukan (perhitungan) :
     
    print ("\n*******************************************************************")
    print ("*           List Smartphone Flagship Terbaru 2018                 *")
    print ("*******************************************************************")
    print ("* 1. Samsung Galaxy S9 PLus (Disc. 10%)    Harga = Rp. 14.000.000 *")
    print ("* 2. Iphone X (Disc 10%)                   Harga = Rp. 18.000.000 *")
    print ("* 3. LG V30+ (Free Speker JBL Flip 3)      Harga = Rp.  9.000.000 *")
    print ("* 4. Nokia 9 (Free Power Bank Vivan Mf20)  Harga = Rp. 10.000.000 *")
    print ("* 5. Xiaomi mi 7 (Free Xioami Amazfit)     Harga = Rp.  8.000.000 *")
    print ("* 6. Vivo V9 (Free Hardcase)               Harga = Rp.  4.000.000 *")
    print ("* 7. Exit                                                         *")
    print ("*******************************************************************")

    menu = float(input("PILIH NOMOR BERAPA : "))
    hitung = perhitungan()
    if menu == 1:
        hitung.flagshippil1()
    elif menu == 2:
        hitung.flagshippil2()
    elif menu == 3:
        hitung.flagshippil3()
    elif menu == 4:
        hitung.flagshippil4()
    elif menu == 5:
        hitung.flagshippil5()
    elif menu == 6:
        hitung.flagshippil6()
    elif menu == 7:
        exit()
    else:
        print ("Maaf angka yang anda masukan tidak terdaftar di list")