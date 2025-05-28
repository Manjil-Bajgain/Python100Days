x=9  #Global variable
print(x)


def hello():
    global x   
    x=8      # it chnage the global variable to local variable
    print(f"The local variable is:{x}")   # it print 8
    
   

print(f"The Global variable is:{x}")
hello()

