import random
answer=random.randint(1,100)
counter=0
while True:
    counter+=1
    number=int(input("guess"))
    if number>answer:
        print("too big")
    elif number<answer:
        print("too small")
    else:
        print("right")
        break
print(f"you guess{counter}time")
    