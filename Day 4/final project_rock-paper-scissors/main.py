import random
choice = ['''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
    ''', '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|   
    ''', '''
                                                                                
.d8888b  .d8888b888.d8888b .d8888b  .d88b. 888d888.d8888b  
88K     d88P"   88888K     88K     d88""88b888P"  88K      
"Y8888b.888     888"Y8888b."Y8888b.888  888888    "Y8888b. 
     X88Y88b.   888     X88     X88Y88..88P888         X88 
 88888P' "Y8888P888 88888P' 88888P' "Y88P" 888     88888P' 
    ''']
#user block
user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if user == "0":
    print('''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
    ''')
elif user == "1":
    print('''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|   
    ''')
elif user == "2":
    print('''
                                                                                
.d8888b  .d8888b888.d8888b .d8888b  .d88b. 888d888.d8888b  
88K     d88P"   88888K     88K     d88""88b888P"  88K      
"Y8888b.888     888"Y8888b."Y8888b.888  888888    "Y8888b. 
     X88Y88b.   888     X88     X88Y88..88P888         X88 
 88888P' "Y8888P888 88888P' 88888P' "Y88P" 888     88888P' 
    ''')
else: 
    print("Incorrect choice !")

#computer block
computer = random.randint(0, 2)
print(f"Computer chose:\n{choice[computer]}")

#decide winner
if user == "0":
    if computer == choice[0]:
        print("There is a tie!")
    elif computer == choice[1]:
        print("You lose!")
    else:
        print("You win!")
elif user == "1":
    if computer == choice[0]:
        print("You win!")
    elif computer == choice[1]:
        print("There is a tie!")
    else:
        print("You lose!")
elif user == "2":
    if computer == choice[0]:
        print("You lose!")
    elif computer == choice[1]:
        print("You win!")
    else:
        print("There is a tie!")
else:
    print("You have entered an invalid number, you lose!")