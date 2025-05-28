import os
# Helps to make the 100 folder automatically
# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0,100): 
#     os.mkdir(f"data/Day{i+1}")

# If i need to rename the 100 folder name then 

# for i in range(0, 100): 
#     os.rename(f"data/Tutorial{i+1}", f"data/TutorialP {i+1}")  # Note source and destination


# To know the list of folde
# folder=os.listdir("data")
# # print(folder)

# for i in folder:
#     print(folder)

#To go specific file inside the folder we use 
folder=os.listdir("data")
print(folder)
for i in folder:
    print(i)
    print(os.listdir(f"data/{i}"))

