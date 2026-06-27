# ELIF = else if statment
# contohnya
# if kondisi:
#     aksi
# elif kondisi2:
#     aksi
# # memasukkan kondisi elif sebanyak yang diinginkan 
# else:
#     aksi false

nilai = int(input("Masukkan nilai 1-100: "))

if 90 <= nilai <= 100:
    print(f"Nilai kamu {nilai}")
    print("Itu nilai tertinggi loh!!")
elif 70 <= nilai <= 89:
    print(f"Nilai kamu {nilai}")
    print("Kamu sudah berusaha keras!!")
elif 50 <= nilai <= 69:
    print(f"Nilai kamu {nilai}")
    print("Belajar lagi ya! Jangan bersedih hati.")
elif 0 <= nilai <= 49:
    print(f"Nilai kamu {nilai}")
    print("Kamu serius?? Kamu perlu peduli dengan nilaimu.")
else:
    print(f"Kamu serius menginput ini: {nilai}")
    print("Ini nilai apaan?? Gak sesuai apa yang diminta input.")
  
 