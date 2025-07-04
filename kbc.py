import os

print("<<< Kaun Banega Crorepati >>>")

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

questions = [
    ["Who is the PM of India ?", "Mamata Bandopadhyay","Narendra Modi","Vladimir Putin","Donald Trump",2],
    ["Which planet is known as the 'Red Planet'?","Earth","Venus","Mars","Jupiter",3],
    ["Who wrote the Indian National Anthem 'Jana Gana Mana'?","Bankim Chandra Chattopadhyay","Rabindranath Tagore","Subhash Chandra Bose","Mahatma Gandhi",2],
    ["What does CPU stand for in computers?","Central Process Unit","Control Panel Unit","Central Processing Unit","Central Power Unit",3],
    ["Which Mughal emperor built the Taj Mahal?","Akbar","Aurangzeb","Jahangir","Shah Jahan",4],
    ["Who is known as the 'Missile Man of India'?","Vikram Sarabhai","Dr. A.P.J. Abdul Kalam","Homi Bhabha","C.V. Raman",2],
    ["Which of the below is a programming language ?", "Cobra","Anaconda","Python","Panther",3],
    ["In which year did India win its first Cricket World Cup?","1979","1983","1987","1992",2],
    ["Which Indian classical dance form is native to Kerala?","Kathak","Bharatanatyam","Kuchipudi","Kathakali",4],
    ["The term “Bluetooth” was named after a king from which country?","Germany","Norway","Denmark","Sweden",3],
    ["Who composed the famous Indian epic 'Mahabharata'?","Tulsidas","Kalidasa","Ved Vyasa","Valmiki",3],
    ["What is the full form of 'ISRO'?","Indian Scientific Research Organization","Indian Space Research Organisation","International Space Research Operation","Indian Satellite Rocket Operation",2],
    ["Who was the first Indian to win a Nobel Prize?", "Rabindranath Tagore","Mother Teresa","C.V. Raman","Amartya Sen",1],
    ["Which among the following is India's first satellite?","INSAT-1A","Bhaskara","Rohini","Aryabhata",4],
    ["What is the name of the first woman IPS officer of India?","Indira Gandhi","Kiran Bedi","Aruna Asaf Ali","Kalpana Chawla",2]
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]

Balance = 0

for i in range(len(questions)):
    key = input("Enter 0 to quit or any other key to continue : ")
    clearTerminal()
    if(key == '0'):
        print("OK, You're now out of the game.")
        print(f"Your current balance is rupees {levels[i-1]}")
        break
    print(f"\nYour question for rupees {levels[i]} is \n\n{i+1}) {questions[i][0]}")
    print(f"1. {questions[i][1]}   2. {questions[i][2]}")
    print(f"3. {questions[i][3]}   4. {questions[i][4]}")
    answer = int(input("\nWhat's your ans(1-4) : "))
    flag = (answer == questions[i][-1])
    if(flag == True):
        print("Correct Answer!!")
    else:
        print(f"Sorry you're wrong... The correct answer is {questions[i][5]}. {questions[i][questions[i][5]]}")
        print("It's over!!")
        break
    if(i == 4):
        Balance = levels[i]
    elif(i == 9):
        Balance = levels[i]
    elif(i == 14):
        Balance = levels[i]
   
print(f"You're taking rupees {Balance} to home.")
print("Thanks for playing!!")