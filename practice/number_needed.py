'''
Given two strings,  and , that may or may not be of the same length, 
determine the minimum number of character deletions required to make 
and  anagrams. Any characters can be deleted from either of the strings.
'''

def number_needed(a, b):
    string1 = list(a)
    string2 = list(b)
    length1 = len(string1)
    length2 = len(string2)
    counter = 0 
    for char in string1:
        if char in string2:
            counter += 1
            index = string2.index(char)
            string2.pop(index)
    return (length1 - counter) + (length2 - counter)
            
a = input().strip()
b = input().strip()

print(number_needed(a, b))
