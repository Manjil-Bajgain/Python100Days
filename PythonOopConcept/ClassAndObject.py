class person:
    name="Manjil"
    occupation="Cyber Security"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")   #self is used to access data from it's specific object.

# making object of it we get
a=person()
print(a.name)
a.name="Ram"
a.occupation="Software Developer"
a.info()
b=person()
b.info()
