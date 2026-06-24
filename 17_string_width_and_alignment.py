# width dan multiline

# data

data_nama = "Fakhri Abiyyu"
data_umur = 18
data_tinggi = 168
data_nomor_sepatu = 41

judul = " Data String ".center(24,"=")

# string standard
data_str = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(judul)
print(data_str)

# string multiline (dengan menggunakan enter, newline, \n)
data_str = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print(f"\n{judul}")
print(data_str)


# string multiline (kutip tiga)
data_string = f"""nama   = {data_nama}
umur   = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print(f"\n{judul}")
print(data_string)

# cara ngatur spasi bisa juga seperti ini 
# umur   = {data_umur:>5}