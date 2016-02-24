"""
distribution.py
Author: Avery Wallis
Credit: Ethan, Payton, Doniel

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
def compare(a, b):
    """
    compare - generic comparison function for testing two elements.
    """
    while a > b:
        return a
    return b > a

string= str(input("Please enter a string of text (the bigger the better): "))
string1=string.lower()
print('The distribution of characters in "'+string1+ '" is:')


alph='abcdefghijklmnopqrstuvwxyz'
result=[]
listnum=[]

for c in alph:
    r = string.count(c)
    if not r==0:
        t=(r*c)
        result.append(t)
        listnum.append(r)
        


listnum.sort(reverse=True)
l=len(result)


def bsort(result, listnum):
    """
    bsort - simple sorting algorithm that uses any comparison function
    seq - a list to be sorted
    cmp - a function for comparing two elements of seq
    """
    sorted = False  # assume the seq is not sorted to start with
    while not sorted:
        sorted = True   # assume it's already sorted correctly
        for index, value in enumerate(result): # for every element in seq
            if index > 0:                   # past the first..
                if not listnum(result[index-1], value):  # if this element is out of order
                    sorted = False          # then the list is not sorted yet
                    result[index-1], result[index] = result[index], result[index-1] # and swap it


bsort(result, compare)
print(result)
"""
print(listnum)     
print(result)
"""