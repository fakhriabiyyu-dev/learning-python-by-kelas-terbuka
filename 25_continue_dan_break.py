# Break 

angka = 0 

# ini standarnya 
# while angka < 5:
#     angka += 1
#     print(f"angka sekarang => {angka}")

#     if angka == 3:
#         print("Disini tandanya bang!")
#         break

#     print("Lanjut guyss")

# print("Udahan ya bang!")

# contoh lain
# Kenapa gak ada tanda? karena True artinya datanya terus benar 
data_integer = int(input("hitung sampai = "))
while True:
    angka += 1
    print(f"count = {angka}")

    if angka == data_integer:
        print("Disini tandanya!")
        break

    print("Lanjut guyss")

print("Udahan ya bang!")
