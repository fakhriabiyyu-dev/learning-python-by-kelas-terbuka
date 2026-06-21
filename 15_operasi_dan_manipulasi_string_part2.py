# operator dalam bentuk method

## menambahkan cade dari dtring ##

# merubah semua ke upper case
contoh1 = "bro!"
print("normal = " + contoh1)
print("upper = " + contoh1.upper()) # merubah semua ke upper case

# merubah semua ke lower case
contoh2 = "Aku KetcHe AbIs"
print("normal = " + contoh2)
print("lower = " + contoh2.lower()) # merubah semua ke lower case

## pengecekan dengan isX method ##

# contoh untuk pengecekkan lower case
salam = "hey brother!"
apakah_lower = salam.islower() # mengecek apakah semua char dalam string itu lower case
print("apakah " + salam + " itu lower case? = " + str(apakah_lower))  

# contoh untuk pengecekkan upper case
print("apakah " + contoh2 + " itu upper case? = " + str(contoh2.isupper())) # mengecek apakah semua char dalam string itu upper casez

# isalpha(), untuk mengecek semuanya huruf dan tidak kosong
# isalnum(), untuk mengecek semuanya huruf atau angka dan tidak kosong 
# isdecimal(), untuk mengecek semuanya angka dan tidak kosong
# isspace(), untuk mengecek semuanya spasi, tab, newline dan tidak kosong
# istitle(), untuk mengecek semuanya title case, yaitu setiap awal kata diawali dengan huruf besar dan sisanya huruf kecil

judul = "It Is Okay Not To Be Orkay" # untuk istitle() gak boleh ada tanda petik
print("apakah " + judul + " itu title case? = " + str(judul.istitle())) # mengecek apakah semua char dalam string itu title case

## pengecekan komponen dengan startswith() dan endswith() ##
# penting untuk memerhatikan kecil besar huruf 
cek_start = "Kimdokja Oppa".startswith("Kim") # untuk mengecek apakah string diawali dengan komponen tertentu
print("apakah " + "Kimdokja Oppa" + " diawali dengan 'Kim'? = " + str(cek_start))

cek_end = "Kimdokja Oppa".endswith("Oppa") # untuk mengecek apakah string diakhiri dengan komponen tertentu
print("apakah " + "Kimdokja Oppa" + " diakhiri dengan 'Oppa'? = " + str(cek_end))

## penggabungan komponen dengan join() split() ##
pisah = ['aku', 'sayang', 'kamu']
print("list = " + str(pisah))
gabung = " ehem ".join(pisah)
print("gabungan = " + gabung)

print("")
gabungan = "aku ehem sayang ehem kamu"
pisah = gabungan.split() # defaultnya split itu memisahkan dengan spasi
print("pisah = " + str(pisah))

# contoh lain 
gabungan = "aku ehem sayang ehem kamu"
pisah = gabungan.split(" ehem ") # memisahkan dengan string " ehem "
print("pisah = " + str(pisah))

# print(5*"=" + " data " + "="*5)
## alokasi karakter rjust(), ljust(), center() ##

kanan = "kanan".rjust(10) # untuk mengalokasikan karakter ke kanan dengan total lebar 10
print("'" + kanan + "'")

kiri = "kiri".ljust(10) # untuk mengalokasikan karakter ke kiri dengan total lebar 10
print("'" + kiri + "'")

tengah = "tengah".center(10) # untuk mengalokasikan karakter ke tengah dengan total lebar 10
print("'" + tengah + "'")

# kalo mau buat yang rapih bisa seperti ini 
judul = " data ".center(20,"=") # yang muncul cuman 14 sama dengan karena 6 sisanya itu adalah dari string " data "
print(judul)

## kebalikannya dengan strip() ##
tengah = tengah.strip() # untuk menghapus spasi di kiri dan kanan
print("'" + tengah + "'")
 