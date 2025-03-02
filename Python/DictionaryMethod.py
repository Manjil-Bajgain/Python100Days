e1={12:"manjil",13:"Shyam",14:"Hari"}
e2={15:"rajiv",16:"Thakur",17:"Sita"}
# print(e1,e2)
# e1.update(e2)
# print(e1)
# e1.clear()
# print(e1)
print(e2.pop(15))   #note : It only print the pop value .
print(e2)

#popitem() -> it is used to pop the last key value of the dictionary
e1.popitem()
print(e1)     # Hari is removed.


#del keyword is used to delete the dictionary
del e1[12]
print(e1)
del e1
# print(e1)   give error because it is already deleted.