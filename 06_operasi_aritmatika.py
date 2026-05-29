# Operasi Artimatika 
a = 22
b = 3

print("Operasi aritmatika")

# operasi pertambahan
hasil = a + b
print(a,'+',b,'=',hasil)

# operasi pengurangan
hasil = a - b
print(a,'-',b,'=',hasil)

# operasi perkalian
hasil = a * b
print(a,'*',b,'=',hasil)

# operasi pembagian
hasil = a / b
print(a,'/',b,'=',hasil)

# operasi eksponen (pangkat) ** 
hasil = a ** b 
print(a,'**',b,'=',hasil)

# operasi modulus (sisa hasil bagi) %
hasil = a % b 
print(a,'%',b,'=',hasil)

# operasi floor division //
# operasi pembagian yang membulatkan menjadi bilangan bulat terdekat 
hasil = a // b 
print(a,'//',b,'=',hasil)

# prioritas operasi, operational precendence

x = 3
y = 2
z = 4

# contoh asal 
hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

"""
kasta prioritas operasi 
() kurung 
* / % // kali, bagi, modulus dan floor division
+ - tambah, kurang  
"""