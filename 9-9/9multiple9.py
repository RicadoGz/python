firstLine=1
secondLine=1
lineNumber=0
while(firstLine<=9):
    secondLine=1
    print()
    while(secondLine<=firstLine):
        print("%d * %d=%d  "%(firstLine,secondLine,firstLine*secondLine),end="")
        secondLine+=1
    firstLine+=1


