import random as rd

def check(comp , user):
    if(comp == user):
        return 0
    elif(user == (comp+1) or comp == (user+2)):
        return 1
    else:
        return -1

print("<<< ROCK✊-PAPER🤚-SCISSORS✌️ >>>")
print("         LET'S PLAY!!!\n\n")

l = ["Rock✊","Paper🤚","Scissors✌️"]

computer = rd.choice(l)
compc = l.index(computer)

player = int(input("Enter 0 for rock✊, 1 for paper🤚 and 2 for scissors✌️ : "))
if player not in range(3):
    raise ValueError("Enter between 0 to 2!!")

print(f"Your choice {l[player]}")
print(f"Computer's choice {l[compc]}")

result = check(compc,player)

if(result == 0):
    print("Draw!!")
elif(result == 1):
    print("Congrats!! You Won..")
else:
    print("Sorry!! You lose..")