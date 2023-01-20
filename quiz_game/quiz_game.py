print("welcom to my computer quiz")

playing = input("Do you want to play? ")
#### chack if player wants to play ####
if playing.lower() != "yes":
    quit()   
print("Okey! Lets play :)")
#### The Game ####
scor = 0 # score tracking

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    scor +=1
else:
    print("Sorry! wrong answer")
    
answer = input("what does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    scor +=1
else:
    print("Sorry! wrong answer")
    
answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct")
    scor +=1
else:
    print("Sorry! wrong answer")
    
answer = input("what does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct")
    scor +=1
else:
    print("Sorry! wrong answer")
    
print("you got " + str(scor) +" questions correct!")
print("you got " + str((scor/4) * 100) +" %. right")