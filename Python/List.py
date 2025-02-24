list=[10,22,39,23]
print(list)
# list.append('Manjil')
# list.append(100)
# print(list)
# list.sort()
# print(list)
list.reverse()
print(list)
list.sort(reverse=True)
print(list)
print(list.index(10))   #after reverse the index is at 3rd position 

mist=list.copy()
mist[0]=0                 
print(mist)      #here list does not change 
print(list)
list.insert(1,20)       #here no override simply insert and position of that data increase respectively
print(list)
m=[100,100,1999]
list.extend(m)
print(list)
k=list+m
print(k)
