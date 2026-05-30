# Latihan Konversi Satuan Temperatur 

# program konversi celcius ke satuan lain 

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukkan suhu dalam celcius : '))
print("suhu adalah",celcius, "Celcius")

# Reamur 
# 4 / 5 * C 
reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur, "Reamur")

# Fahrenheit 
fahrenheit = (9/5) * celcius + 32
print("suhu dalam fahrenheit adalah",fahrenheit, "Fahrenheit")

# Kelvin 
kelvin = celcius + 273.15
print("suhu dalam kelvin adalah",kelvin, "Kelvin")