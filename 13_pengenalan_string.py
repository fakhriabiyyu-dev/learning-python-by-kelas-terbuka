data = "ini adalah string"
print(data)
print(type(data))


# 1. Cara membuat string 

'''
    1. bisa menggunakan single quote 'isi string'
    2. bisa menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

# 2. Menggunakan backslash di string

# ini contoh yang digabungkan 
print('"\nHalo, apa kabar?"')
print("'Halo, apa kabar?'")

# ======================
# jika didalam kalimat menggunakan single quote, maka bagusnya string kita pakai double quote
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \
# Membuat tanda ' ini menjadi string meski pakai single quote
print('\nmari kita shalat jum\'at')
print('g\'day, isn\'t it?')
# ======================

# backslash \
# cara biar backslashnya dianggap backslash adalah dengan pakai backslash lagi 
print("\nC:\\user\\Abiyyu")

# tab \t
print("\nfakhri\tabiyyu, jauhan")
print("\nfakhri\t\tabiyyu, semakin jauhan")

# backspace \b
print("\nfakhri \babiyyu, jadi gak ada spasinya")

# ======================================

# newline \n
print("\nbaris pertama. \nbaris kedua.") # Newline / Line Feed, bentuknya \n

# Karakter \r berfungsi untuk mengembalikan kursor ke awal baris yang sama, tanpa pindah ke baris bawahnya.
print("baris pertama. \rbaris kedua.") # Carriage Return, bentuknya \r

# kedua istilah itu sebenarnya relate dalam fitur pengetikan keyboard kita 
# bisa di coba fitur itu dengan pencet tombol insert dan akan terlihat jelas berbeda 

print("baris pertama. \r\nbaris kedua.") # Line Feed Carriage Return, ini di pakai semua windows
# ======================================

# 3. String literal atau raw

# hati-hati
print('C:\new folder') # ini jadi masalah karena backslash itu di hitung enter kan?

# bagaimana kalau misalnya ada banyak \\ nya? seperti link path google?
# maka seperti ini saja
# menggunakan raw string 
print(r'C:\new \t\r\b\\folder') # meskipun kita mengguakan backslash lagi didalam string raw, akna tetap di hitung STRING.

# multiline literal string
print("""
Nama : Fakhri
Kelas : 2 SMK
""")

# multiline literal string dan RAW 
print(r"""
Nama : Fakhri
Kelas : 2 SMK
Website : www.fakhriabiyyudev.id/home
""")

