#Sets do not print the dublicate/repeated data
info={2,3,4,5,2}
print(info)
#In set order does not matter.
info1={"Ram","Maniil",2,4,5}
print(info1)           #It does not print the in order as mention in set
print(type(info1))

#If we make a empty set the  it type will be the dictionary
info2={}
print(type(info2))


# If we want to create the empty set then we use ()
info3=set()
print(type(info3))


#Using for loop
for value in info:
    print(value)