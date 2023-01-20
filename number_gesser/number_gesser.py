import random
gusses = 0
random_number = random.randint(0,11)
while True:
    gusses += 1
    user_gess = input("make a guess between 0-10: ")
    if user_gess.isdigit():
        user_gess = int(user_gess)
        if user_gess < 0 or user_gess > 10:
            print("next time Gess a number between 1-10!")
            quit()
    else:
        print("next time pleas type in a number!")
        quit()
    if user_gess == random_number:
        print("You got it right!!!")
        break
    elif user_gess > random_number:
            print("you are above the number")
    else:
        print("you were below the number")
        
print("you got it in ", gusses, " gusse")