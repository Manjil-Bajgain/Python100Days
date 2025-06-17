import random
def greet():
    print("WELCOME TO ROCK PAPER SESSIOR GAME:")
greet()
User_input=input("Enter your choice(sessior ,paper,rock):")
computer_input=random.choice(["rock","paper","sessior"])
print(f"computer choice is:{computer_input}")
if(User_input==computer_input):
    print("Both have same choice(DRAW)")
elif(User_input=="sessior" and computer_input=="paper"):
    print("You win the game")
elif(User_input=="paper" and computer_input=="rock" ):
    print("You win the game")
elif(User_input=="rock" and computer_input=="sessior" ):
    print("You win the game")
else:
    print("you loose the game(COMPUTER WINS)")

