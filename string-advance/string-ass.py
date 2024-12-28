#Given a string: "itheima itcast boxuegu"
testString="itheima itcast boxuegu"
#Count how many occurrences of the substring "it" are in the string.
stringCount=testString.count("it")
print("hvae %d it in the string"%stringCount)
#Replace all spaces in the string with the character "|".
replaceString=testString.replace(" ","|")
print(replaceString)
#Split the string by "|" to get a list.
splitString=replaceString.split("|")
print(splitString)