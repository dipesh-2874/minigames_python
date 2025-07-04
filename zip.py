import os

def clear_Terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def drawBoard():
    clear_Terminal()
    print("Enter 'w' to go up 's' for down 'a' for left 'd' for right : ")
    print(" ____ ____ ____ ____ ____ ____")
    print(f"| {pos[0]} | {pos[1]} | {pos[2]} | {pos[3]} | {pos[4]} | {pos[5]} |")
    print(" ____ ____ ____ ____ ____ ____")
    print(f"| {pos[6]} | {pos[7]} | {pos[8]} | {pos[9]} | {pos[10]} | {pos[11]} |")
    print(" ____ ____ ____ ____ ____ ____")
    print(f"| {pos[12]} | {pos[13]} | {pos[14]} | {pos[15]} | {pos[16]} | {pos[17]} |")
    print(" ____ ____ ____ ____ ____ ____")
    print(f"| {pos[18]} | {pos[19]} | {pos[20]} | {pos[21]} | {pos[22]} | {pos[23]} |")
    print(" ____ ____ ____ ____ ____ ____")
    print(f"| {pos[24]} | {pos[25]} | {pos[26]} | {pos[27]} | {pos[28]} | {pos[29]} |")
    print(" ____ ____ ____ ____ ____ ____")
    print(f"| {pos[30]} | {pos[31]} | {pos[32]} | {pos[33]} | {pos[34]} | {pos[35]} |")
    print(" ____ ____ ____ ____ ____ ____")

def move_player(direction, start):
    if direction == 'w' and start - 6 >= 0:
        if pos[start-6] not in numList:
            pos[start-6] = '⬆️ '
        return start - 6
    elif direction == 's' and start + 6 < 36:
        if pos[start+6] not in numList:
            pos[start+6] = '⬇️ '
        return start + 6
    elif direction == 'a' and start % 6 != 0:
        if pos[start-1] not in numList:
            pos[start-1] = '⬅️ '
        return start - 1
    elif direction == 'd' and (start + 1) % 6 != 0:
        if pos[start+1] not in numList:
            pos[start+1] = '➡️ '
        return start + 1
    else:
        raise ValueError("Invalid move or move out of bounds!")
    
def output(start):
    # if pos[start] not in numList:
    #     pos[start] = '🟩'
    if pos[start] == '2 ':
        pos[start] = '2️⃣ '
    elif pos[start] == '3 ':
        pos[start] = '3️⃣ '
    elif pos[start] == '4 ':
        pos[start] = '4️⃣ '
    elif pos[start] == '5 ':
        pos[start] = '5️⃣ '
    elif pos[start] == '6 ':
        pos[start] = '6️⃣ '
    elif pos[start] == '7 ':
        pos[start] = '7️⃣ '
    elif pos[start] == '8 ':
        pos[start] = '8️⃣ '


pos = []
print("Enter the values of the box :")
for i in range(36):
    pos.append(input())
    if(pos[i] == ''):
        pos[i] += ' '
    pos[i] += ' '

drawBoard()
start = pos.index('1 ')
pos[start] = '1️⃣ '
n = 0 
c = '  '
numList = ['1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ']

while(n == 0):
    drawBoard()
    
    if c not in pos:
        break

    dir = input("Enter your move:\n")

    start = move_player(dir, start)
    
    output(start)

dir = input("Enter your move:\n")
start = move_player(dir, start)
output(start)
drawBoard()

    