#In previous version of of python the string formating is difficult. It required long code to formate the f-string
#for example:
intro1="Hi! , I am {} and i am from {},Bara" 
intro="Hi! , I am {1} and i am from {0},Bara" 
name="Manjil"
city="Simara"
print(intro.format(name,city))
print(intro1.format(name,city))



#Then to solve this long code format problem f-string is generated
print(f"Hi! , I am {name} and I am from {city},Bara")
f=float(208.393)
print(f"the float value is : {f}")
print(f"the float value is : {f:.1f}")
#I can also print f-string like this 
print(f"Hi!! , I am {{name}} and i am from {{city}}")  #use double curly bracket