class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetails(self):
        print(f"The employee id is {self.id}.\nThe employee name is {self.name}.")

# inheritance concept
class programmer(employee):
    def access(self):
        print(f"The employee id is {self.id}.\nThe employee name is {self.name}.")

obj=employee("Manjil",1)
obj.showDetails()
obj1=programmer("Hari",1) 
obj1.access()

    