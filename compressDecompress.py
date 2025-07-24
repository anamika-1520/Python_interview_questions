import zlib
string = input("enter the string :")

comperssed_string=zlib.compress((string.encode()))

print("compressed string is : ",comperssed_string)

decompressed_string=zlib.decompress(comperssed_string)
print("decompressed string is : ",decompressed_string)