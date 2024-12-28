#what is a string, string basic same as a tuple of list can't indivudal change the value
stringExample="hello,wolrd"
print(stringExample[2])
"""_summary_
    Traceback (most recent call last):
  File "/Users/gz/Desktop/python0-50/1-day/string-advance/string-advance.py", line 4, in <module>
    stringExample[2]="o"
    ~~~~~~~~~~~~~^^^
TypeError: 'str' object does not support item assignment
    """
#stringExample[2]="o"
# this was how you call the value of the string
stringIndexTwo=stringExample[2]
print(stringIndexTwo)
# how to search a elemnt in the string
stringSearhIndex=stringExample.index("l")
print("the L in the string example is in the index %d",stringSearhIndex)
# how to reaplace a string
newString=stringExample.replace("l","9")
print(newString)
# how to seplit the string
newSeplitString=stringExample.split("l")
print("the new string been split by l%s",newSeplitString)
# how to remove the begian and end space or some word in the string
stringExample="                  he    l l o,wol r d     "
newRemoveSpaceString=stringExample.strip()
print("new remove sting is %s"%newRemoveSpaceString)
stringExample="hhhhello,wolrheqweqwqewhdhhh"
newRemoveWorld=stringExample.strip("h")
# only will remove the begian and end
print("new remove sting is %s"%newRemoveWorld)
# how to cound the single char
newCountString=stringExample.count("h")
print(newCountString)
newlen=len(stringExample)
print(newlen)

