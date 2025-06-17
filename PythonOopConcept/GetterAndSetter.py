class Myclass:
    def __init__(self, n):
        self._value = n  # use _value internally

    @property
    def value(self):
        return 10 * self._value  # safely return the scaled value
    @value.setter
    def value1(self,num):
        self._value=num/10


    def show(self):
        print(f"The given value is {self._value}")

obj = Myclass(10)
print(obj.value)   # prints 100
obj.show()         # prints "The given value is 10"
obj.value1=1000
print(obj.value1)