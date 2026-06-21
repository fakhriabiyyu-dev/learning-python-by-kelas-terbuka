# operasi dan manipulasi string 

# 1. menyambung string (concatenate)
nama_pertama = "Fakhri"
nama_tengah = "D"
nama_akhir = "Abiyyu"

# nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
nama_lengkap = f"{nama_pertama} {nama_tengah} {nama_akhir}"
print(nama_lengkap)

# 2. menghitung panjang string
panjang_nama = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang_nama))

# 3. mengubah string menjadi huruf besar atau kecil

# mengecek apakah ada komponen char atau string di dalam string

huruf = "f" # perbedaan huruf berpengaruh pada hasil
status = huruf in nama_lengkap
print("string " + huruf + " ada di " + nama_lengkap + " = " + str(status))

huruf = "F" # perbedaan huruf berpengaruh pada hasil
status = huruf in nama_lengkap
print("string " + huruf + " ada di " + nama_lengkap + " = " + str(status))

# Ini untuk hasil sebaliknya pada fungsi di bawah menggunakan not in 
huruf = "f" # perbedaan huruf berpengaruh pada hasil
status = huruf not in nama_lengkap
print("string " + huruf + " ada di " + nama_lengkap + " = " + str(status))

# mengulang string 
print("wk"*10)
print(10*"wk")

# indexing 
print("index ke-0 dari " + nama_lengkap + " = " + nama_lengkap[0]) # indexing dimulai dari 0
print("index ke-1 dari " + nama_lengkap + " = " + nama_lengkap[1]) # indexing dimulai dari 0
print("index ke-(-1) dari " + nama_lengkap + " = " + nama_lengkap[-1]) # indexing negatif dimulai dari -1
print("index ke-[0,6] dari " + nama_lengkap + " = " + nama_lengkap[0:6]) # slicing dimulai dari 0 sampai 5

print("index ke-[0,2,4,6,8,10] dari " + nama_lengkap + " = " + nama_lengkap[0:11:2]) # slicing dengan step 2 dimulai dari 0 sampai 10

# ascii code
print("item paling kecil dari " + nama_lengkap + " = " + min(nama_lengkap)) # item paling kecil berdasarkan urutan ascii
print("item paling besar dari " + nama_lengkap + " = " + max(nama_lengkap)) # item paling besar berdasarkan urutan ascii    

ascii_code = ord(" ") # mengubah char menjadi ascii code
print("ascii code dari spasi = " + str(ascii_code))
data = 117 # mengubah ascii code menjadi char
print("char dari ascii code 117 = " + chr(data))

# 4. operator dalam bentuk method
# yang dihitung method itu adalah count()
data = "fathir d abyaz"
jumlah = data.count("a") # menghitung jumlah char a dalam string
print("jumlah char a dalam " + data + " = " + str(jumlah))
