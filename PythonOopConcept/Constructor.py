class professional:
    def __init__(self,n,w):     # Parameterized constructor
        self.name=n
        self.Work=w

    def info(self):
        print(f"{self.name} work as a {self.Work}.")

a=professional("Ram","HR")   # This "a" is pass as a self, So it seems like two argument is pass but in reality three argument is passing 
b=professional("Manjil","Cyber scurity Analyst")
a.info()
a.info()
b.info()


# Note: Python do not support the multiple constructor at a time like (c++)
# It does not support the default and parameterized constructor at a time. 
