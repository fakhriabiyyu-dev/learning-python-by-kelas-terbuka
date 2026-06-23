# format string

## contoh generic ##
# string 
nama = "fakhri"
format_str = f"hello {nama}"

print(format_str)

# boolean 
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# angka 
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

## bilangan bulat ##
angka = 15 # ini adalah angka desimal
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

jutaan = 2000000
format_str = f"jutaan = {jutaan:,}" # Output: 2,000,000 (otomatis menambahkan koma sebagai pemisah ribuan)

## bilangan desimal atau float ##
pi = 3.14159265 # ini adalah angka desimal atau float 
# Default float (6 digit di belakang koma)
format_float1 = f"bilangan desimal = {pi:f}"  # Output: 3.141593 (otomatis dibulatkan)

# btw . (titik di bawah itu menandakan titik didalam bilangan desimal kita)
format_float2 = f"bilangan desimal = {pi:.2f}"  # Output: 3.14 (dibulatkan ke 2 angka di belakang koma)
format_float3 = f"bilangan desimal = {pi:.0f}"  # Output: 3 (dibulatkan ke angka bulat terdekat)
print(format_float1)
print(format_float2)
print(format_float3)

# menampilkan leading zeros (angka nol di depan)
angka = 2005.54321
format_float4 = f"bilangan desimal leading zero = {angka:010.2f}"  # menampilkan total karakter yang kita inginkan, termasuk titik dan angka di belakang koma)
print(format_float4)

## bilangan biner ##
angka = 5
format_biner = f"bilangan biner = {angka:b}" # Output: 101

# Tampilan biner dengan total 8 digit (ditambah 0 di depan)
print(f"8 Bit: {angka:08b}")    # Output: 00000101
print(format_biner)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10.321
# bisa pake d kalau bilangan bulat, f kalau desimal, atau b kalau biner
format_minus = f"angka minus = {angka_minus:+d}" # fungsi + disini adalah sebuah aturan/instruksi format (formatting rule)
format_plus = f"angka plus = {angka_plus:+.2f}"    
print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi matematika di dalam placeholer {}
harga = 10000
jumlah = 5

format_string = f"total harga = Rp.{harga * jumlah}" # sangat fleksible
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"  # Output: 0b11111111
format_octal = f"octal = {oct(angka)}"    # Output: 0o377
format_hexadecimal = f"hexadecimal = {hex(angka)}"  # Output: 0xff
print(format_binary)
print(format_octal)
print(format_hexadecimal)