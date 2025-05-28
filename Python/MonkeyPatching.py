#How Monkey Patching work 

def add(a,b):        #wanting this addition function do suntraction we use monkey patching. 
    return a+b

def sub (a,b):
    return a-b

add=sub 
print(f"The subtraction of the two number is:{add(5,2)}")