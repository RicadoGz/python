"""_summary_
given the following employee information, use dictionaries to complete the data recording.
Using a for loop, for all employees with a level of 1, increase their level by 1 and their salary by 1000.

Name	Department	Salary	Level
    """
exampleDic={
      "tx":{
          "depart":"tech",
          "salary":3000,
          "leverl":1
      },
    "wjj":{
                  "depart":"mark",
          "salary":5000,
          "leverl":2
    },
    "self":{
                  "depart":"mark",
          "salary":7000,
          "leverl":3
    },
    "tlx":{
                  "depart":"tech",
          "salary":4000,
          "leverl":1
    },
    "zbw":{
                  "depart":"mark",
          "salary":6000,
          "leverl":2
    }  
}
print(exampleDic)
for key in exampleDic:
    if exampleDic[key]["leverl"]==1:
        exampleDic[key]["salary"]+=1000
print("---------------")
print(exampleDic)