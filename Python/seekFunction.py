f= open('myfile1.txt','r')
f.seek(8)
a=f.read(3)
print(a)

# The tell() function used to say the current position within the file.
current_position=f.tell()    #It gives 11 which is current function in myfile.txt
print(current_position)

#Truncate() function is used to write the number of byte in the file
q=open('one.txt','w')
q.write('Hello manjil')
print()
q.truncate(15)

q=open('one.txt','r')
print(q.read())



