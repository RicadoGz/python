exampleDic={"hi":5,"world":9}
# add new into dictionary
# add a key don'T exist
exampleDic["wow"]=6
print(exampleDic)
# change the value of the key into dictionary
exampleDic["wow"]=0
print(exampleDic)
#del element
exampleDic.pop("wow")
print(exampleDic)

# get all keys in the dictionary
allKeys=exampleDic.keys()
print(allKeys)
# two way go through the dictionary
for key in allKeys:
    print("the key=%s of dictionary is and value is%s"%(key,exampleDic[key]))
print("-------------")
for key in exampleDic:
    print("the key=%s of dictionary is and value is%s"%(key,exampleDic[key]))
#clear dictionary
exampleDic.clear()
print(exampleDic)