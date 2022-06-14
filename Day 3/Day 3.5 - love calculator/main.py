
is_running = True

while is_running:
    
    name_1 = input("Enter the first name: \n").lower()
    name_2 = input("Enter the second name: \n").lower()

    combined_name = name_1 + name_2

    t = combined_name.count('t')
    r = combined_name.count('r')
    u = combined_name.count('u')
    e = combined_name.count('e')
    true = t + r + u + e

    l = combined_name.count('l')
    o = combined_name.count('o')
    v = combined_name.count('v')
    e = combined_name.count('e')
    love = l + o + v + e

    love_result = str(true) + str(love)
    love_result_as_int = int(love_result)

    if (love_result_as_int < 10) and (love_result_as_int > 90):
        print(f"Your score is {love_result_as_int}, you go together like coke and mentos.")
    elif (love_result_as_int > 40) and (love_result_as_int < 50):
        print(f"Your score is {love_result_as_int}, you are alright together.")
    else:
        print(f"Your score is {love_result_as_int}. Love doctor is unable to detect your compatibility.\nYou might want to follow your mind on this.")

    play_again = input("Do you want to play again?\nType yes or no: ").lower()
    if (play_again == 'yes'):
        continue
    else:
        is_running = False
        print("Thank you for stopping by today. See you next time!")