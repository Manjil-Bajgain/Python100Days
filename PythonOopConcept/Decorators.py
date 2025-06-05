# Decorators function take a function as an argument
def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning Everyone")
        fx(*args,**kwargs)   # This is the our function which we want to decorate
        print("Thank you for using this function.")
    return mfx

@greet 
def hellow():
    print("Hello!! ")
@greet
def add(a,b):
    print(a+b)

#greet(hellow)()   # This can also be done
hellow()
add(1,2)