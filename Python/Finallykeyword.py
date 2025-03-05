def fun():
    try:
        a=([1,2,3,4,5])
        x=int(input("Enter the Index:"))
        print(a[x])
        return 1
    except:
        print("Invalid index:")
        return 0
    finally:                        #NOTE: function return vaya pani finally execute vairako in both error or non error case.
        print("I am always executed:")

x=fun()
print(x)
