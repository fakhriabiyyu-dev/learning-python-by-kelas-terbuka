# Operator Assigment
# Operasi yang dapat dilakukan dengan penyingkatan

a = 5 # ini adalah assigment
print('nilai a =',a)

a += 1 # ini artinya sama aja a = a + 1
print('nilai a += 1, nilai a menjadi',a)

a -= 2 # ini artinya sama aja a = a - 2
print('nilai a -= 2, nilai a menjadi',a)

a *= 5 # ini artinya sama aja a = a * 2
print('nilai a *= 5, nilai a menjadi',a)

a *= 5 # ini artinya sama aja a = a * 2
print('nilai a *= 2, nilai a menjadi',a)

a /= 2 # ini artinya sama aja a = a / 2
print('nilai a /= 2, nilai a menjadi',a)

# Modulus dan FLoor Division 
b = 10
print('\nnilai b =',b)
b %= 3
print('nilai b %= 3, nilai b menjadi',b)

b = 10
print('\nnilai b =',b)
b //= 3
print('nilai b //= 3, nilai b menjadi',b)

# Pangkat / Eksponen 
a = 5
print('nilai a =',a)
a **= 3
print('nilai a **= 3, nilai a menjadi',a)

# operasi bitwise 
# OR 
print("\n" + "="*15,"OR","="*15)
c = True
print("nilai c =",c)
c |= False
print('nilai c |= False, nilai c menjadi',c)
c = False
print("nilai c =",c)
c |= False
print('nilai c |= False, nilai c menjadi',c)

# AND 
print("\n" + "="*15,"AND","="*15)
c = True
print("nilai c =",c)
c &= False
print('nilai c &= False, nilai c menjadi',c)
c = True
print("nilai c =",c)
c &= True
print('nilai c &= True, nilai c menjadi',c)

# XOR 
print("\n" + "="*15,"XOR","="*15)
c = True
print("nilai c =",c)
c ^= False
print('nilai c ^= False, nilai c menjadi',c)
c = True
print("nilai c =",c)
c ^= True
print('nilai c ^= True, nilai c menjadi',c)

print("\n" + "="*15,"SHIFTING","="*15)
# Geser geser / Shifting
d = 0b0100
print("nilai d =",format(d,'04b'))
d >>= 2
print("nilai d >>=",format(d,'04b'))
d <<= 1
print("nilai d <<=",format(d,'04b'))
