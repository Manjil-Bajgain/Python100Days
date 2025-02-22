# #There are two types of function 
# # 1) User Define function
# # 2) Build-in-function
# def valueChecker(a,b):
#     if(a>b):
#         print(f"{a} is greater than {b}")
#     elif(a==b):
#         print(f"{a} and {b} is same")
#     else:
#         print(f"{a} is smaller than {b}")
# x=int(input("Enter the two number:"))
# y=int(input("Enter the two number:"))
# valueChecker(x,y)


# def total_sum(*numbers):
#     return sum(numbers)

# print(f"The sum of numbers is: {total_sum(1, 2, 3, 4, 5)}")


#Nested Function
message=input("Enter some message:")
def outer_function(message):
    def inner_function():
        print("Inner function")
    inner_function()
    return message
print("From outer function:",outer_function(message))
    


