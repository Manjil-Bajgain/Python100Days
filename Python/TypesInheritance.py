# #Single Inheritance

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.child_variable = "child variable"
#         def use_protected(self):
#             # accessing the protected method from parent
#             parent_msg=self._protected_method():
#                 return print(f"The message from parent {Parent_msg}")
        
        
#      #creating the instance of chld
# child_instance=Child()
# print(child_instance._protected_method)


class Parent:
    def greet(self):    #self ma object pass hunxa
        print("Namastay!!!")
class Child(Parent):
    pass



child1=Child()
child1.greet()
