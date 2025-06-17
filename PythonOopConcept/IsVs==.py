# NOte: "is" and "==" is comparision operator but it have the folowing differences i.e
# 1. "is" operator compare the identity.
# 2. ""=="" operator compare the value

# a=(1,2,3)
# b=(1,2,3)
a=[1,2,3,4]
b=[1,2,3,4]
print(a is b)   # exact location of object in the memory
print(a ==b )
