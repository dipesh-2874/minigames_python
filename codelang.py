import random as rd

c = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encode():
    data = input("Enter the text to encode : ")
    dataList = data.split(" ")
    for i in range(len(dataList)):
        if(len(dataList[i])<=3):
            dataList[i] = rd.choice(c)+dataList[i]+rd.choice(c)
            dataList[i] = dataList[i][::-1]
        else:
            dataList[i] = dataList[i][-2:]+dataList[i][2:-2]+dataList[i][:2]
            dataList[i] = rd.choice(c)+rd.choice(c)+dataList[i]+rd.choice(c)+rd.choice(c)
            dataList[i] = dataList[i][::-1]
    output = ''
    for i in range(len(dataList)):
        output = output + (dataList[i]) + ' '
    
    print(output)


def decode():
    data = input("Enter the encoded text : ")
    dataList = data.split(" ")
    for i in range(len(dataList)):
        if(len(dataList[i])<=7):
            dataList[i] = dataList[i][1:-1]
            dataList[i] = dataList[i][::-1]
        else:
            dataList[i] = dataList[i][::-1]
            dataList[i] = dataList[i][2:-2]
            dataList[i] = dataList[i][-2:]+dataList[i][2:-2]+dataList[i][:2]

    output = ''
    for i in range(len(dataList)):
        output = output + (dataList[i]) + ' '
    
    print(output)

choice = input("Enter 0 to decode and 1 to encode : ")
if(choice == '0'):
    decode()
elif(choice == '1'):
    encode()
else:
    raise SyntaxError("Invalid!! Enter 0 or 1.")
