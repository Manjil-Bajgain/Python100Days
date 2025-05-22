# How import works in Python

# import math
# x= math.floor(2.3)
# print(x) 
# y=math.ceil(2.3)
# print(y)
# result=math.sqrt(9)
# print(result)


# We can also use the math function by taking it out in the beginning like as follows

# from math import sqrt,pi
# # Now we can directly use the auet function and pi 
# y=sqrt(16)*pi
# print(y) 


# We can also use the all the function present in the module by using  the star 
# from math import *
# y=sqrt(16)*pi
# print(y)
# # But this method is not recommended because many function coming from which module may cause confusion.
   
# we can use "as" to make the short form like as follows

# from math import sqrt as s
# result= s(9)
# print(result)

# We can also do this like as follows:
# import math as s
# result =s.sqrt(16)
# print(result) 


# for example we don't know about which function is available in the math module 
#   then we can  print that function with the help of dir function
# import math 
# print(dir(math))
# # to print it class
# print(math.nan,type(math.nan))


# Also we can import function or variable from the another slide.
from manjil import greets,greet  # In this case also we can use *
greet()
print(greets)
