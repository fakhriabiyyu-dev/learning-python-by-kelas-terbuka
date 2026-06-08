# Operasi Logika atau Boolean 

# not, or, and, xor 

print("\n" + "="*30)
print("   Operasi Logika / Boolean")
print("="*30 + "\n")

# NOT 
print("========= NOT =========")
a = False
c = not a
print('data a =',a)
print('--- NOT')
print('data c =',c)

# OR (Jika salah satu adalah True maka hasilnya True)
print("\n========= OR =========")
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
a = True
b = False
c = a or b
print(a,' OR',b,'=',c)
a = True
b = True
c = a or b
print(a,' OR',b,' =',c)


# AND (Jika dua duanya True maka hasilnya True)
print("\n========= AND =========")
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,' AND',b,'=',c)
a = True
b = True
c = a and b
print(a,' AND',b,' =',c)


# XOR tandanya ^
# akan true jika salah satu akan True, sisanya False 
print("\n========= XOR =========")
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,' XOR',b,' =',c)