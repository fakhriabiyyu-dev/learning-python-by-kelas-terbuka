# Operator Bitwise, Operator Biner, Binary

# Operasi pada masing masing bit 
# 0-0-0-0-0-0-0-0 || Ini panjang nilainya
# 7-6-5-4-3-2-1-0 || Banyaknya nilai

a = 9
b = 5

# bitwise OR (|)
c = a | b
print("\n" + "="*15,"OR","="*15)
print("nilai :",a,", binary :",format(a,"08b"))
print("nilai :",b,", binary :",format(b,"08b"))
print("="*30,"(|)")
print("nilai :",c,", binary :",format(c,"08b"))

# bitwise AND (&)
c = a & b
print("\n" + "="*15,"AND","="*15)
print("nilai :",a,", binary :",format(a,"08b"))
print("nilai :",b,", binary :",format(b,"08b"))
print("="*30,"(&)")
print("nilai :",c,", binary :",format(c,"08b"))

# bitwise XOR (^) 
c = a ^ b
print("\n" + "="*15,"XOR","="*15)
print("nilai :",a,", binary :",format(a,"08b"))
print("nilai :",b,", binary :",format(b,"08b"))
print("="*30,"(^)")
print("nilai :",c,", binary :",format(c,"08b"))

# bitwise NOT (~) 
c = ~a
print("\n" + "="*15,"NOT","="*15)
print("nilai :",a,", binary :",format(a,"08b"))
print("="*30,"(~)")
print("nilai :",c,", binary :",format(c,"08b"))

# Kalau mau di flip bisa pakai XOR (^)
print("="*30,"(^)")
d = 0b0000001001
e = 0b1111111111
print("nilai :",e^d,", binary :",format(e^d,"08b"))

# shifting 

# shift right (>>)
c = a >> 1 # geser berapa kali
print("\n" + "="*15,"SHIFT RIGHT","="*15)
print("nilai :",a,", binary :",format(a,"08b"))
print("="*30,"(>>)")
print("nilai :",c,", binary :",format(c,"08b"))

# shift left (<<)
c = a << 2 # geser berapa kali
print("\n" + "="*15,"SHIFT LEFT","="*15)
print("nilai :",a,", binary :",format(a,"08b"))
print("="*30,"(<<)")
print("nilai :",c,", binary :",format(c,"08b"))

