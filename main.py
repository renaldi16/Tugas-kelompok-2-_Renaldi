import json
from os import system, name 
import datetime
tm = datetime.datetime.now()
tm = tm.strftime("%d %B %y")
        

#tampilan
def sun():
    with open("total.txt",'r') as files:
        data = json.load(files)
        terjual = data["terjual"]
        alirandana = data["alirandana"]
    print("====TUGAS DASPEM KELOMPOK 2====")
    print(f"|Hari Ini : {tm}|")
    print(F"|Total Penjualan : Rp. {alirandana}|Barang Terjual :{terjual}|")
   


#AUTO CLEAR CONSOLE
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')

#HAPUS SPACEBAR AWAL DAN AKHIR PADA INPUT
def removefirstendspaces(string):
    return "".join(string.rstrip().lstrip())

#HANYA MENERIMA INPUT ANGKA
def get_int_jumlah():
    userdata = input("Berapa Banyak  :")
    try:
        user_num = int(userdata)
        return user_num
    except ValueError:
        print("Anda Menulis Huruf :(\nHanya Menerima Input Angka!!")
        return(get_int_jumlah())
def get_int_harga():
    userdata = input("Masukan Harga Baru  :")
    try:
        user_num = int(userdata)
        return user_num
    except ValueError:
        print("Anda Menulis Huruf :(\nHanya Menerima Input Angka!!")
        return(get_int_harga())        

#MASUKAN BARANG
def inputbarang():
    while True:
        clear()
        sun()
        print("\n==Masukan Data Barang=====================")   
        add = {}
        tambahbarang = input("Nama barang  :")
        tambahbarang = removefirstendspaces(tambahbarang)
        ltambahbarang = tambahbarang.lower()
        tambahharga = get_int_harga()
        add[ltambahbarang] = tambahharga
        
    
        with open("data.txt", "r+") as files:
            data = json.load(files)
            data.update(add)
            files.seek(0)
            json.dump(data, files)
        print("Data Telah di input")
        menu = input("\n\n1) Ada barang lagi\n0) Selesai\n==========)  :")
        menu = removefirstendspaces(menu)
        if menu == "0":
            break
#CEK BARANG    
def liststockbarang():
    while True:
        clear()
        sun()
        with open('data.txt') as files:
            data = json.load(files)
            print("\n==BARANG TERSEDIA======================= ")
            for j in data:
                #print(f"{j}   : sisa {dataj[j]} pcs")
                print(f"{j}    : Rp.{data[j]}")
            i = input("\n0) selesai\n==========)  :")
            i = removefirstendspaces(i)
            if i == "0":
                break
        print("====================================")
#TAMPILAN BARANG
def listhargabarang():
    with open('data.txt') as files:
        data = json.load(files)
        print("==BARANG YANG TERSEDIA======================= ")
        for j in data:
            #print(f"{j}   : sisa {dataj[j]} pcs")
            print(f"{j}    : Rp.{data[j]}")
        print("=============================================")

#TRANSAKSI
def transaksi():
    totalbayar = 0
    totalb = "\n\n"
    jumlahb = 0
    #history
    with open('total.txt','r+') as history_file:
        datahistory = json.load(history_file) 
    now = datetime.datetime.now()
    time = now
    yadd = f"\nTransaksi {time}"
    with open('data.txt','r+') as files:
        data = json.load(files)
        while True:
            clear()
            sun()  
            print("\n==TRANSAKSI=======================")   
            listhargabarang()
            x = input("Nama Barang :")
            x = x.lower()
            x = removefirstendspaces(x)
            jh = data.get(x) 
            if jh != None:               
                y = get_int_jumlah() 
                totalh = jh * y
                totalbayar = totalbayar + totalh
                totalbayarstr = str(jh * y)
                totalb = totalb +" -"+ x + "         "+str(y) +" pcs"+"      Rp."+totalbayarstr +"\n"
                yadd =  yadd + f"\npembelian {x} sebanyak {y} dengan harga Rp.{totalh}"
                #jumlahbarang
                jumlahb = jumlahb + y

                print("\n\n==========Struk Pembelian==========")
                print(totalb)
                print(f"\nTotal Harga Rp.{totalbayar}")
            
                m = input("\n\n==================================== \n 1) Lagi\n 2) Selesai Dan Batal\n 0) Selesai Dan Simpan\n==========)  :")
                m = removefirstendspaces(m)
                if m == "2":
                    break 
                elif m == "0":
                    f = open("stock.txt",'a')
                    f.write(yadd)
                    f.close
                    datahistory["alirandana"] += totalbayar 
                    datahistory["terjual"] += jumlahb
                    #datahistory["terlaris"] =
                    with open('total.txt','w') as history_file:
                        json.dump(datahistory, history_file)

                    break

                                                    
            else:
                print(f"\n\nBarang {x} tidak ada di list barang :)")
                print("Silahkan Input Barang Di Menu input Barang!!")
                print("\n==========Struk Pembelian==========")
                print(totalb)
                print(f"\nTotal Harga = Rp{totalbayar}")
                m = input("\n\n==================================== \n 1) Lagi\n 2) Selesai Dan Batal\n 0) Selesai Dan Simpan\n==========)  :")
                m = removefirstendspaces(m)
                if m == "2":

                    break
                elif m == "0":
                    print(datahistory)
                    f = open("stock.txt",'a')
                    f.write(yadd)
                    f.close
                    datahistory["alirandana"] += totalbayar 
                    datahistory["terjual"] += jumlahb
                    #datahistory["terlaris"] =
                    with open('total.txt','w') as history_file:
                        json.dump(datahistory, history_file)
                    break
#RIWAYAT
def riwayat():
    clear()
    sun()
    x = open("stock.txt",'r')
    print(x.read())
    x.close
    m = input("0) Selesai\n==========)  :")
    m = removefirstendspaces(m)
    if m == "0":
        pass
#RESET RIWAYAT DAN TOTAL PENJUALAN 
def reset():
    clear()
    sun()
    m = input("\n 1) Reset Semua Catatan Pembelian\n 0) Batal\n==========)  :")
    m = removefirstendspaces(m)
    if m == "1":
        with open("total.txt",'r') as files:
            data = json.load(files)
            data["alirandana"] = 0
            data["terjual"] = 0
        with open("total.txt",'w') as files:
            json.dump(data, files)
            
        x = open("stock.txt",'w')
        x.write = ""
        x.close
        clear()
        sun()
        print("\nData Telah Di Hapus")
        m = input("0) Selesai\n==========)  :")
        m = removefirstendspaces(m)
        if m == "0":
            pass
    elif m == "0":
        pass

# HAPUS BARANG
def hapusbarang():
    while True:
        clear()
        sun()
        listhargabarang()
        hapus = input("\nNote!! Barang yang di input langsung terhapus\nNama Barang  : ")
        hapus = hapus.lower()
        removefirstendspaces(hapus)
        with open("data.txt",'r+') as files:
            data = json.load(files)
            dataget = data.pop(hapus, None)
            if dataget != None:
                with open("data.txt",'w') as files:
                    json.dump(data, files)
                print(" ( Telah Di Hapus)")
                m = input("=====================\n 1) Hapus Barang Lagi?\n 0) Selesai\n==========)  :")
                removefirstendspaces(m)
                if m == "0":
                    break
            else:
                print(" (Barang Tidak Ada)")
                m = input("=====================\n 1) Hapus Barang Lagi?\n 0) Selesai\n==========)  :")
                removefirstendspaces(m)
                if m == "0":
                    break
#UBAH HARGA
def ubahharga():
    while True:
        clear()
        sun()
        print("========UBAH HARGA========")
        barang =input("Nama Barang  : ")
        barang = barang.lower()
        with open("data.txt",'r+') as files:
            data = json.load(files)
            dataget = data.get(barang)
            if dataget != None:
                print(f"Harga Saat Ini Rp.{data[barang]}")
                harga = get_int_harga()
                data[barang] = harga
                with open("data.txt",'w') as files:
                    json.dump(data , files)
                print("(Berhasil Di Ubah)")
                m = input("=====================\n 1) Ubah Lagi? \n 0) Selesai\n==========)  :")
                if m == "1":
                    pass
                elif m == "0":
                    break
            else:
                print("(Barang Tidak Ada)")
                m = input("=====================\n 1) Ubah Lagi? \n 0) Selesai\n==========)  :")
                if m == "1":
                    pass
                elif m == "0":
                    break


#MAIN
while True :
    clear()
    sun()

    m = input("\n== MAIN MENU SUN ====================\n 1) Barang Dagangan\n 2) Transaksi \n 3) Riwayat Transaksi \n 4) Reset \n 0) Selesai\n==========)  :")
    m = removefirstendspaces(m)
    if m == "1":
        clear()
        sun()
        while True :
            clear()
            sun()
            m = input("\n==MENU BARANG=======================\n 1) Input Barang\n 2) Cek Barang\n 3) Ubah Harga\n 4) Hapus Barang\n 0) Selesai\n==========)  : ")
            m = removefirstendspaces(m)
            if m == "1":
                inputbarang()
            elif m == "2":
                liststockbarang()
            elif m == "3":
                ubahharga()
            elif m == "4":
                hapusbarang()
            elif m == "0":
                break
    elif m == "2":
        transaksi()
    elif m == "3":
        riwayat()
    elif m == "4":
        reset()
    elif m == "0":
        clear()
        sun()
        print("Terima kasih Telah Mencoba --SUN-- Versi 1.1 (Kelompok 2 Tugas Daspem)")
        break



