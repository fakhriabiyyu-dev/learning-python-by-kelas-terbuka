# Latihan Konversi Satuan Temperatur 

# Mengubah Kelvin dan Fahrenheit
print("\n" + "="*52)
print("  PROGRAM KONVERSI TEMPERATUR KELVIN KE FAHRENHEIT")
print("="*52 + "\n")

kelvin = float(input("Masukkan suhu dalam kelvin : "))

# Rumus: K - 273.15
celcius = kelvin - 273.15
fahrenheit = (9/5) * celcius + 32

# print(f"Suhu dalam Fahrenheit adalah: {fahrenheit}")
print(f"Suhu dalam Fahrenheit adalah: {round(fahrenheit, 2)}°F")