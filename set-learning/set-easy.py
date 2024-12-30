# add a element into set
emptySet=set()
emptySet.add(2)
print("add a elemnt which is 2 into set%s"%emptySet)
# remove a element from set
emptySet.remove(2)
print("remove element which is 2 from set %s"%emptySet)
# random take one element from the set
exampleSet={5,6,5,2,2,3}
randomSet=exampleSet.pop()
print("random set with pop is %s"%randomSet)
#clear a set
exampleSet.clear()
print("set after clear%s",exampleSet)
# how to find the different bteween 2 set
exampleSet1={1,2,3,4,5}
exampleSet2={1,2,7,8,3,9}
differentSet=exampleSet1.difference(exampleSet2)
# it will only show the different to compare with the second set
print(differentSet)

# to update the set 1 and dele the same set between set 1 and set 2
exampleSet1.difference_update(exampleSet2)
print(exampleSet1)
# how to combined two set 
exampleSet1={1,2,3,3,3,3,3,3,3,3,4,5}
exampleSet2={1,2,7,8,3,9}
combinedSet=exampleSet1.union(exampleSet2)
print(combinedSet)
# how to calculate the element in the set
lenSet=len(exampleSet1)
# it not include the same value in the set
print(lenSet)

# go through set
for setNumber in exampleSet1:
    print(setNumber)