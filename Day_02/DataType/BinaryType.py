#bytes function(range 0 to 255)
'''bytes is a function that return an object
butes is immutable that means that cant be change'''

MahadiList=[0,1,2,34,5,56,7,255]

b=bytes(MahadiList)

print(type(b))


#bytesarray
'''This is mutable and range is 0 to 255'''

MahadiList1=[1,2,3,4,5,6,78,9,1]
b1=bytearray(MahadiList1)

b1[0]=100
print(b1[0])
print(type(b1))
