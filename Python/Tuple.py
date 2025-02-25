a=(1,2,3,4,"manjil")
print(a[0])
print(a[4])
print(a[:4])  # Here 4th index is excluded
print(a[:5])
if "manjil" in a:
    print("manjil is present in in tuple")
if 4 in a:
    print("4 is present in in tuple")
tup=a[1:3]   # Here 3 is excluded 
print(tup)
#NOTE : Like list we cannnot manipulate the tuple so, first we change the tuple to list then we do required manipulation and again we change it to tupel.
#operation in tuple 
tup=("India","China","England","America","Africa")
print(tup)
tem=list(tup)
tem.append("Austrilia")     #add item
tem.pop(2)                  #remove item
tem[2]="Nepal"               #change item
tup=tuple(tem)
print(tup)


#Some of method in list are :
#count
tup1=(1,2,4,32,3,2,3)
# tup1[1]=333     #since we cannot change tuple because the tuple are immutable.
# print(tup1)
print("the sum of 3 in given tuple is :",tup1.count(3))
#index
print("The index of 32 is :",tup1.index(32))
#index(element,start,end)
print("the index of 3 from range of (6-7) is :",tup1.index(3,6,7))







