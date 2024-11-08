def entry_input(entry):
    file_input = input(entry)
    while not file_input:
        print("Username dan Password tidak boleh kosong, tolong ulangi lagi !")
        file_input = input(entry)
    return file_input

def ubah(df):
    try:
        nama = entry_input("Nama lama : ")
        if nama not in df['nama'].values:
            print("Data tidak ditemukan !")
            return df
        name = entry_input("Nama baru : ")
        kontak = int(entry_input("Nomor kontak (+62): "))
        jk = int(entry_input("kendaraan roda : "))
        merek = entry_input("Merek kendaraan : ")
        warna = entry_input("Warna kendaraan : ")
        durasi = int(entry_input("Durasi penitipan : "))
        tiket = f"S{len(df)+1}A{durasi}H"
        if jk == 2:
            biaya = durasi*30000
        elif jk == 4:
            biaya = durasi*50000
        else :
            biaya = durasi*100000 
        harga = biaya
        bayar = entry_input("Pembyaran Cash/Dp : ")
        if jk == 2:
            lokasi = "lantai 3"
        elif jk == 4:
            lokasi = "lantai 2"
        else:
            lokasi ="lantai 1"
        tempat = lokasi

        df.loc[df['nama'] == nama, ['nama','kontak','tiket','roda','merek','warna','durasi','biaya','bayar','lokasi']] = [name,kontak,tiket,jk,merek,warna,durasi,harga,bayar,tempat]
        df.to_csv('Data_CSV.csv', index=False)
        print(f"Data {nama} Berhasil di ubah ")
    except ValueError :
        print("Masukkan data dengan Benar !")
    return df

def delete(df):
    x = entry_input("Nama yang ingin di hapus : ").strip().lower() 
    df['nama'] = df['nama'].str.lower()  
    df = df[df['nama'] != x]
    df.to_csv('Data_CSV.csv', index=False)
    print(f"Data dengan nama {x} telah dihapus.")
    return df

def add(df):
    try:
        nama = entry_input("Nama Pemilik : ")
        kontak = int(entry_input("Nomor kontak (+62): "))
        roda = int(entry_input("kendaraan roda : "))
        merek = entry_input("Merek kendaraan : ")
        warna =entry_input("Warna kendaraan : ")
        durasi = int(entry_input("Durasi penitipan : "))
        tiket = f"S{len(df)+1}A{durasi}H"
        if roda == 2:
            biaya = durasi*30000
        elif roda == 4:
            biaya = durasi*50000
        else :
            biaya = durasi*100000 
        harga = biaya
        bayar = entry_input("Pembyaran Cash/Dp : ")
        if roda == 2:
            lokasi = "lantai 3"
        elif roda == 4:
            lokasi = "lantai 2"
        else:
            lokasi ="lantai 1"
        tempat = lokasi

        df.loc[len(df)] = [nama,kontak,tiket,roda,merek,warna,durasi,harga,bayar,tempat]
        df.to_csv('Data_CSV.csv', index = False)
        print(f"Data atas Nama {nama} Berhasil ditambahkan")

    except ValueError :
        print("Masukkan data dengan Benar !")
    return df
    

def search(df):
    nama = input("Masukkan Nama : ").strip().lower() 
    df['nama'] = df['nama'].str.lower()
    df = df[df['nama'] == nama]
    if len(df) == 0:
        print(f"Data atas nama {nama} tidak ditemukan")
    else:
        print(df)

def ubah_item(df):
    nama = input("masukkan data nama pemilik yang ingin diubah : ").strip().lower()
    pemilik = df[df['nama'].str.lower() == nama]
    if len(pemilik) == 0 :
        print("data tidak ditemukan!")
    else:
        x = input("apa yang ingin diubah : ").strip().lower()
        z = ['nama','kontak','tiket','roda','merek','warna','durasi','biaya','bayar','lokasi']
        if x in z: 
            new = input(f"Masukkan {x.capitalize()} baru : ")
            df.loc[df['nama'] == nama,f'{x}'] = [new]
            print(f"Berhasil mengubah {x} pada data {nama}")
        else :
            print("kolom tidak ditemukan")
        
        df.to_csv('Data_CSV.csv', index = False)
        return df
  