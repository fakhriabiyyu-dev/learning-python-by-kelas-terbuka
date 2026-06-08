# Latihan Logika Komparasi 
# membuat gabungan area rentang dari angka

# 1. KASUS GABUNGAN (OR)
# ++++++3-----------10++++++
# Area: Angka < 3 ATAU Angka > 10

print("--- Kasus Gabungan (OR) ---")
inputUser = float(input('Masukkan angka (< 3 atau > 10): '))

nilaiKurangDari = 3
nilaiLebihDari = 10

# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < nilaiKurangDari)

# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > nilaiLebihDari)

# Menggabungkan dengan OR
isCorrect = isKurangDari or isLebihDari

print(f"Status Kurang dari 3: {isKurangDari}")
print(f"Status Lebih dari 10: {isLebihDari}")
print(f"Hasil Akhir (Gabungan): {isCorrect}")

print("\n" + "="*30 + "\n")

# 2. KASUS IRISAN (AND)
# ------3++++++++++10--------
# Area: Angka > 3 DAN Angka < 10

print("--- Kasus Irisan (AND) ---")
inputUser = float(input('Masukkan angka (> 3 dan < 10): '))

# Memperbaiki variabel yang tertukar di kode sebelumnya
nilaiBatasBawah = 3
nilaiBatasAtas = 10

# MEMPERBAIKI LOGIKA:
# Harusnya: inputUser LEBIH BESAR dari 3
isLebihDari = (inputUser > nilaiBatasBawah)

# Harusnya: inputUser KURANG DARI 10
isKurangDari = (inputUser < nilaiBatasAtas)

# Menggunakan AND karena kita mencari nilai di TENGAH
isCorrect = isLebihDari and isKurangDari

print(f"Status Lebih dari 3: {isLebihDari}")
print(f"Status Kurang dari 10: {isKurangDari}")
print(f"Hasil Akhir (Irisan): {isCorrect}")