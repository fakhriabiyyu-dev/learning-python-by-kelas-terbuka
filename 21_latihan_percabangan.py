# Kalkulator Sederhana 

operator = input("""## Kalkulator Sederhana ##
(1). Pertambahan.
(2). Pengurangan.
(3). Perkalian.
(4). Pembagian.           
Pilih operator diantara (1/2/3/4): """)

nilaiPertama = float(input("Masukkan nilai pertama: "))
nilaiKedua = float(input("Masukkan nilai kedua: "))

# Percabangannya 
if operator == "1":
    hasil = nilaiPertama + nilaiKedua
    print(f"hasilnya adalah {hasil}")
elif operator == "2":
    hasil = nilaiPertama - nilaiKedua
    print(f"hasilnya adalah {hasil}")
elif operator == "3":
    hasil = nilaiPertama * nilaiKedua
    print(f"hasilnya adalah {hasil}")
elif operator == "4":
    hasil = nilaiPertama / nilaiKedua
    print(f"hasilnya adalah {hasil}")
else:
    print("nilai tidak sesuai.")

print("\nAkhir dari program, sekianterima gaji.")