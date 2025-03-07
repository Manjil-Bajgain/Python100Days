# x= int((input("Enter the Number form 1 to 9(1-9) :")))
# if (x<1 or x>9):
#     raise ValueError("The number you enter is not from between (1-9)")





User = input("Enter The Value Between 5 And 9 : ")
try:
    if (User == "Quit" or "quit" ):
        print("Better Luck Next Time!")
    else:
        if (int(User)>= 5 and int(User) <= 9):
            print(f"Congrulations! Your Entered Number {User} Is Between 5 And 9")
            print("Good Job!")
        elif (int(User) <= 4 or int(User) >= 10):
            raise ValueError("Error : Inavlid Input (Value Should Be In 5 And 9)")
except ValueError as e:
    print(e)