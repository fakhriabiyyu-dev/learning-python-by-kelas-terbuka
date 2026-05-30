# Latihan Konversi Satuan Temperatur 

# Mengubah Fahrenheit ke kelvin
print("\n" + "="*52)
print("  PROGRAM KONVERSI TEMPERATUR FAHRENHEIT KE KELVIN")
print("="*52 + "\n")

fahrenheit = float(input("Masukkan suhu dalam fahrenheit : "))

# Rumus: (F - 32) * 5/9 
celcius = (fahrenheit - 32) * 5 / 9
kelvin = celcius + 273.15

# print(f"Suhu dalam Kelvin adalah: {kelvin}")
print(f"Suhu dalam Kelvin adalah: {round(kelvin, 2)}K")