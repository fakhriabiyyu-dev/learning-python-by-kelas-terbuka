# Operasi Komparasi 
print("\n" + "="*23)
print("   Operasi Komparasi")
print("="*23)

# setiap hasil dari operasi komparasi adalah boolean 

# >,<,>=,<=,==,!=, is, is not

a = 4
b = 2

print("Nilai a :",a)
print("Nilai b :",b,"\n")

# lebih besar dari > 
print("========= Lebih besar dari >")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2 # False karena nilainya harus benar benar lebih besar bukan sama.
print(b,'>',2,'=',hasil)

# kurang dari > 
print("\n========= Kurang dari <")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2 # False karena nilainya harus benar benar lebih besar bukan sama.
print(b,'<',2,'=',hasil)

# lebih dari sama dengan >= 
print("\n========= lebih dari sama dengan >=")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2 # Jika nilainya sama maka true juga
print(b,'>=',2,'=',hasil)

# kurang dari sama dengan <= 
print("\n========= kurang dari sama dengan <=")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2 # Jika nilainya sama maka true juga
print(b,'<=',2,'=',hasil)

# sama dengan ==
print("\n========= sama dengan (==)")
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 2
print(b,'==',2,'=',hasil)

# tidak sama dengan !=
print("\n========= sama dengan (!=)")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# tidak sama dengan !=
print("\n========= sama dengan (!=)")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# 'is' sebagai komparasi object identity
# ia tidak bisa digunakan untuk literal misalnya 
# hasil = x is 5 (5 adalah literal)
print("\n========= object identity ")
print("\n========= is")
x = 5 # ini adalah assigment untuk object
y = 5
print('nilai x =',x,',id =',hex(id(x)))
print('nilai y =',y,',id =',hex(id(y)))
hasil = x is y
print(hasil)

print("\n========= is not")
x = 5 # ini adalah assigment untuk object
y = 6
print('nilai x =',x,',id =',hex(id(x)))
print('nilai y =',y,',id =',hex(id(y)))
hasil = x is y
print(hasil)