# #MAP
# # for cube of one number
# def cube(x):
#     return x*x*x
# print(cube(2))
 


# # To do cube of multiple number we use list:
# a=[1,2,3,4,5]
# b=[]

# # for item in a:
# #     b.append(cube(item))
# # print(b)

# b=list(map(cube,a))  # NOTE: function name ra list name as a argument  
# print(b)
 
# # FILTER
# def filter_function(a):
#     return a>2
# new1=list(filter(filter_function,a))
# print(new1)



#reduce 
# for reduce we need to import the reduce from function tools.
from functools import reduce
number=[1,2,3,4,5]
def sum(x,y):
    return (x+y)
num1=reduce(sum,number)
print(num1)