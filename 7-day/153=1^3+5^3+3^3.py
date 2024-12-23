inp=int(input("type in a number and test was that waterloo between 100-1000"))
low=inp%10
mid=(inp//10)%10
high=inp//100
if low**3 + mid**3 + high**3==inp:
    print("nice")
else:
    print("bad")