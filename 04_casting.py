# Belajar Casting
# mengubah dari satu tipe ke tipe lain 
# tipe data + int, float, string, bool

## INTEGER
print("=====INTEGER=====")
data_int = 7
print("data : ", data_int, ", type : ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # Data bool ini jika angka itu lebih dari 0 maka true, jika kurang dari nol aka false
print("data : ", data_float, ", type : ", type(data_float))
print("data : ", data_str, ", type : ", type(data_str))
print("data : ", data_bool, ", type : ", type(data_bool))


## FLOAT
print("=====FLOAT=====")
data_float = 9.9
print("data : ", data_float, ", type : ", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) # Data bool ini jika angka itu lebih dari 0 maka true, jika kurang atau sama dengan nol aka false
print("data : ", data_int, ", type : ", type(data_int))
print("data : ", data_str, ", type : ", type(data_str))
print("data : ", data_bool, ", type : ", type(data_bool))

## BOOLEAN
print("=====BOOLEAN=====")
data_bool = False
print("data : ", data_bool, ", type : ", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool) # Data bool ini jika angka itu lebih dari 0 maka true, jika kurang atau sama dengan nol aka false
print("data : ", data_int, ", type : ", type(data_int))
print("data : ", data_str, ", type : ", type(data_str))
print("data : ", data_float, ", type : ", type(data_float))

## STRING
print("=====STRING=====")
data_str = ""
print("data : ", data_str, ", type : ", type(data_str))

data_int = int(data_str) # string harus angka
data_float = float(data_str) # string harus angka
data_bool = bool(data_str) # false jika string kosong
print("data : ", data_int, ", type : ", type(data_int))
print("data : ", data_float, ", type : ", type(data_float))
print("data : ", data_bool, ", type : ", type(data_bool))