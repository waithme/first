ll_words:
All_words.py:
import sys

input_string = sys.argv[1]
pattern = sys.argv[2]
string_list = list(input_string)
# Add any parameters you require to the function signature here

def all_words_recursive(input_list, begin, end):
    # WRITE your implementation of this function here
    # ['a‘,'b','c'] -> [c.b.a]
    if begin == end:
        for i in input_list:
            print(i, end='')
        print()
    for m in range(begin, end + 1):
        input_list[m], input_list[begin] = input_list[begin], input_list[m] # swap the adjancent element
        all_words_recursive(input_list, begin + 1, end)                     # use recursion to implement the swap on the previous line 
        input_list[m], input_list[begin] = input_list[begin], input_list[m] 

    pass

# Add any parameters you require to the function signature here
def all_words_iterative(input_list, begin, end):
    # WRITE your implementation of this function here
    if begin == end:
        for i in input_list:
            print(i, end='')
        print()
    for m in range(begin, end + 1):
        input_list[m], input_list[begin] = input_list[begin], input_list[m]
        all_words_recursive(input_list, begin + 1, end)
        input_list[m], input_list[begin] = input_list[begin], input_list[m]


# WRITE your main code here
if pattern == "recursive":
    all_words_recursive(string_list, 0, len(string_list) - 1)
elif pattern == "iterative":
all_words_iterative(string_list, 0, len(string_list) - 1)