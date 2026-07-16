# Mencoba menggambar segitia menggunakan perulangan looping 
# contohnya seperti di bawah 
# *
# **
# ***
# ****
# *****

sisi = 4

# dummy variable 
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1