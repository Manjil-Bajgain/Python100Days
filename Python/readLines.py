# f= open('aa.txt','r')
# while True:
#     line=f.readline()
#     if not line:
#        break
#     print(line)



# Real Life example is:
#If in file the marks value is given then,
# f= open('aa.txt','r')
# i=0
# while True:
#     i=i+1
#     line=f.readline()
#     if not line:
#        break
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     print(f"The marks in {i} of math is: {m1} ")
#     print(f"The marks in {i} of science is: {m2} ")
#     print(f"The marks in {i} of nepali is: {m3} ")


# WriteLines()

f= open('aa.txt','w')
line=['line1\n','line2\n','line3\n']
f.writelines(line)
f.close()