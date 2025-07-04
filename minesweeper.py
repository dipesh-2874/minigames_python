import os
import random as rd

pos = []
for i in range(25):
    if i<9:
        pos.append(str(i+1)+' ')
    else:
        pos.append(str(i+1))

minesList = []
minesList = (rd.sample(range(0,24),6))

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def board():
    print("<<< MINESWEEPER >>>\n")
    print(" ---- ---- ---- ---- ----")
    print(f"| {pos[0]} | {pos[1]} | {pos[2]} | {pos[3]} | {pos[4]} |")
    print(" ---- ---- ---- ---- ----")
    print(f"| {pos[5]} | {pos[6]} | {pos[7]} | {pos[8]} | {pos[9]} |")
    print(" ---- ---- ---- ---- ----")
    print(f"| {pos[10]} | {pos[11]} | {pos[12]} | {pos[13]} | {pos[14]} |")
    print(" ---- ---- ---- ---- ----")
    print(f"| {pos[15]} | {pos[16]} | {pos[17]} | {pos[18]} | {pos[19]} |")
    print(" ---- ---- ---- ---- ----")
    print(f"| {pos[20]} | {pos[21]} | {pos[22]} | {pos[23]} | {pos[24]} |")
    print(" ---- ---- ---- ---- ----")

def check(box, choice):
    if (box-1) not in minesList:
        if choice == 's':
            pos[box-1] = '⛏️ '
        elif choice == 'f':
            pos[box-1] = '🚩'
        else:
            raise ValueError("Invalid choice !")
        
    else:
        if choice == 's':
            global g
            g += 1
            for k in range(6):
                pos[minesList[k]] = '💥'
            return
        elif choice == 'f':
            pos[box-1] = '🚩'
        else:
            raise ValueError("Invalid choice !")

board()
g = 1
while(g == 1):
    box = int(input("Enter the box number : "))
    choice = input("Enter 's' for spade and 'f' for flag : ")

    clearTerminal()
    check(box, choice)
    board()
    if g>1:
        print("Wrong Move!! Mines blusted...\n")