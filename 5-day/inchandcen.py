value=float(input("plz input the cen of your high"))
size=input("give me inch or cen")
if size == "cen":
    result=value/2.54
else:
    result=value*2.54
print(result)

