# Example sequences for slicing

# 1. Slice a list, starting from index 1 to index 4, with a step of 1
my_list = [10, 20, 30, 40, 50]
newList1=my_list[1:4:1]
print(newList1)
# 2. Slice a tuple, starting from the beginning to the end, with a step of 1
my_tuple = (1, 2, 3, 4, 5)
# Example result: (1, 2, 3, 4, 5)
newTupleList=my_tuple[0::1] # first can be 0 or empty
print(newTupleList)
# 3. Slice a string, starting from the beginning to the end, with a step of 2
my_string = "abcdefg"
# Example result: "aceg"
newstringList=my_string[0::2]
print(newstringList)
# 4. Slice a string, starting from the beginning to the end, with a step of -1
my_string = "abcdefg"
# Example result: "gfedcba"
newNegetiveString=my_string[::-1]
print(newNegetiveString)
# 5. Slice a list, starting from index 3 to index 1, with a step of -1
my_list = [10, 20, 30, 40, 50]
# Example result: [40, 30]
newList1=my_list[3:1:-1]
print(newList1)
# 6. Slice a tuple, starting from the beginning to the end, with a step of -2
my_tuple = (1, 2, 3, 4, 5)
# Example result: (5, 3, 1)
newTupleList=my_tuple[::-2] # first can be 0 or empty
print(newTupleList)