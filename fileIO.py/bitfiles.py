f1=open("file1.txt","wb")
# **Above statement will creater a new file file1.txt in binary mode. w for write mode and b for binary mode.

f2=open("file2.txt","ab")
# Above statement will open file named file2.txt in append as well as binary mode. a for append mode and b for binary mode.

f3=open("file2.txt","rb")

f3=open("file2.txt","rb")


#closing a file
f1.close()


print(b'\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83'.decode('utf-8'))
print(b'\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83'.decode('latin-1'))


#BITWISE OPRT


# Code to demonstrate bitwise operations
# Some bytes to play with
byte1 = int('11110000', 2)  # 240
byte2 = int('00001111', 2)  # 15
byte3 = int('01010101', 2)  # 85
  
# Ones Complement (Flip the bits)
print(~byte1)
# AND
print(byte1 & byte2)
# OR
print(byte1 | byte2)
# XOR
print(byte1 ^ byte3)
# Shifting right will lose the 
# right-most bit
print(byte2 >> 3)
# Shifting left will add a 0 bit 
# on the right side
print(byte2 << 1)
# See if a single bit is set
bit_mask = int('00000001', 2)  # Bit 1 
# Is bit set in byte1?
print(bit_mask & byte1)
# Is bit set in byte2?
print(bit_mask & byte2)






# def _int_32_tobites(i):
#     """Converting an integer to four bites in little endian format"""
#     #& : Bitwise and
#     #>> : Right-shift
#     return bytes((i & 0xff
#                   i >> 8 & 0xff
#                   i >> 16 & 0xff
#                   i >> 32 & 0xff
#                   ))
