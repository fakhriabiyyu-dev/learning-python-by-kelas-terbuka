# Mengecek tipe data dalam variable

a = 10
print(type(a))

# tipe data: Angka satuan yang gak ada komanya (integer)
data_integer = 100
print("data : ", data_integer, ", bertipe : ", type(data_integer))

# tipe data: angka dengan koma (float)
data_float = 1.5
print("data : ", data_float, ", bertipe : ", type(data_float))

# tipe data: kumpulan karakter (string) 
data_string = "abiyyu 10"
print("data : ", data_string, ", bertipe : ", type(data_string))

# tipe data; biner true/false (boolean) 
data_boolean = True # False
print("data : ", data_boolean, ", bertipe : ", type(data_boolean))

print("\n")
## tipe data khusus

# bilangan kompleks 
data_complex = complex(5,6)
print("data : ", data_complex, ", bertipe : ", type(data_complex))

# tipe data dari bahasa C 

from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double, ", bertipe : ", type(data_c_double))
