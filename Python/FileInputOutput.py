 # Python provides the several ways to manipulate file
 # Before perform any operation on the file ,We must open it first .
 # Python provide the open() function to open the file. It take the two argument one is file name and another is file mode.
 # The mode are : 'a' for append ,'r' for read ,'w' for write



#READING THE FILE

# f= open('myFile.txt','r')
# f= open('myFile.txt','rt') #open this file as text form
# f= open('myFile.txt','rb') #open this file as binary form.To open .jpg file ,.pdf file or .exe file we use rb mode
# #print(f)
# # #print(f)
# text=f.read()
# print(text)
# f.close()


# WRITING THE FILE
# a=open('Myfile1.txt','w')
# a.write("Hi i am manjil")
# a.close()  # NOTE: close function is mandatory to execute the program

#Append the file

# a=open('Myfile1.txt','a')  # append mode
# a.write(". I am from Simara,Bara")
# a.close()



# By using the "with" keyword we don't need to use close function
a=open('Myfile1.txt','a')   # Insteade of this we can use as a too. 
with open('Myfile1.txt','a') as a:
    a.write(" I dont need close function:")   