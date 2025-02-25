#Python Docstring are the string literals that appears right after the defination of function,method ,class ,or module.
def square(n):
     """This function takes n as an argument and just return the square 
of the given number.""" 
     print(n**2)
square(3)
print(square.__doc__) 