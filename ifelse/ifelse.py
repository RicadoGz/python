import random
randomNumber = random.randint(1,100)
print("lets guess the number1-100 you can guess 6time")
userGuess=int(input("first time"))
userTime=0
while(True):
    if (userGuess==randomNumber):
        print("you are right and guess %d times"%userTime)
        break 
    else:
        if(userGuess>randomNumber):
            print("too big")
            userGuess=int(input(f"{userTime+2} time"))
            userTime+=1
        else:
            print("too less")
            userGuess=int(input(f"{userTime+2} time"))
            userTime+=1