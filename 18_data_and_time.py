# Date and time (latihan)

import datetime as dt

tanggal_hari_ini = dt.date.today()
print(tanggal_hari_ini)
# Cara manggil otomatis nama harinya dengan pakai %A
print(f"Hari ini adalah hari = {tanggal_hari_ini:%A}")
# Beberapa fungsi spesifik soal datetime dengan %
# %a (huruf kecil): Nama hari versi pendek/singkatan (contoh: Mon, Tue, Wed).
# %A (huruf besar): Nama hari versi lengkap (contoh: Monday, Tuesday).

# %b: Nama bulan versi singkatan (contoh: Jan, Feb, Mar).
# %B: Nama bulan versi lengkap (contoh: January, February).
# %d: Hari dalam bentu angka dua digit.
# %m: Bulan dalam bentuk angka dua digit (01 sampai 12).

# %y (huruf kecil): Tahun dua digit terakhirnya saja (contoh: 26 untuk tahun 2026).
# %Y (huruf besar): Tahun versi lengkap empat digit (contoh: 2026).

# bisa juga di set sesuai keinginan kita 
tanggal_merdeka = dt.date(2026, 8, 17)
print(tanggal_merdeka)


# cara pendeteksi tanggal lahir 
print("Silakan masukkan tanggal, \nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t:")) 
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah = {tanggal_lahir:%A, %d %B %Y}")

# cara menghitung umur 
hari_ini = dt.date.today()
print(f"Hari ini adalah: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari % 365) // 30
print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")
