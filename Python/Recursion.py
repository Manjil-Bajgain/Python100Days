# def fact(n):
#     if(n==1 or n== 0):
#         return 1
#     else:
#         return(n*fact(n-1))
# print("Enter the number that you want to get factorial:")
# x=int(input())
# result=fact(x)
# print(f"The factorial of the {x}! is :",result)


#The iteration is goes like this:
"""5*fact(4)
5*4*fact(3)
5*4*3*fact(2)
5*4*3*2*fact(1)  # Here the condition stop.Because the fact(1) return the 1.
"""

#Recursion to calculate the fibonacci series.
def fibo(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))
print("Enter the number that you want to get fibonacci series :")
x=int(input())
result=fibo(x)
for i in range(x):
    print(fibo(i),end=",")

    