# class person:
#     name="Manjil"
#     worksAs="CyberAnalyst"
#     def disply(self):
#         print(f"{self.name} is a {self.worksAs}.")
# obj1=person()
# obj1.disply()
# obj1.name="Silviya"
# obj1.worksAs="HR"
# obj1.disply()



#Using constructor
class a:
    # def __init__(self):
        
        def __init__(self,name,occ):
            print("Hey! I am a constructor:")
            self.name=name    #pass as a argument
            self.occ=occ
        def display(self):
            print(f"{self.name} is a {self.occ}.")


    
obj1=a("Manjil","HR")
obj2=a("Shyam","CyberSecurity")
obj2.display()
obj1.display()
#Obj1.display()
