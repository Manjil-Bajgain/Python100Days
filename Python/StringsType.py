m="manjil"
print(m[0:6])
print(m[-6:-1])
print(m[-5:-1])
# Types of Python String
# NOTE: String are immutable
print("The orginal String is :")
k="Hellow, Everyone it's  me manjil bajgain.!!"
print(k)

#len()
print(len(k))

#rstrip   -> Used to remove the trailing
print(k.split(" ")) # Represent as a list
print(k.lower())
print(k.upper())
print(k.replace("manjil","Yunish"))
print(k.rstrip("!"))
print(k.count("H"))
print(len(k.center(190)))
print(k.center(90))
print(k.capitalize())     #it make msb in upper case and other in lower case
print(k.endswith("!!"))
print(k.endswith("me",23,25))
print(k.find("me"))
print(k.index("me"))   # Same as find() but it throw error if any error is occured.
l=" Hell 12o "
print(l.isalnum())   # it takes o-9 number too 
print(l.isalpha())
print(l.islower())
print(l.isprintable())
print(l.isspace())

