#It is the combination of key value pair.
#For example 
dic ={
    "manjil" : "Name of the person",
    "Bajgian":"Sir name of the person"
} 
print(dic["manjil"])


dic1={"name":"Manjil","roll no":23,"address":"Simara,Bara"}
print(dic1)
print(dic1.keys())                          #note you can only write key or keys (your choice)
for keys in dic1.keys():
    print(f" The value corresponding to {keys} is :{dic1[keys]}")



print(dic1.items())
for key,value in dic1.items():
    print(f" The value corresponding to {key} is :{value}")

