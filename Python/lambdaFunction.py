# def name():
#     print("My name is manjil.")
# name()

def apply(fx,value):
    return 6+fx(value)
  ## NOTE: lambda function do not contain any name.
square=lambda x:x*x
# x=3
# print(f"the square of given value {x} is:{square(x)}")

# avg=lambda x,y:(x+y)/2
# print(f"The average value is : {avg(2,3)}")


## even we can use the function as the argument
 

#function ma ni function pass garauna sakinxa.
print(apply(square,2))