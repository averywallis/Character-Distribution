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


lists=zip(listnum, result)
lists=sorted(lists, key=lambda listnum: listnum[0])   # sort by number
lists.sort(reverse=True)
print(list(lists))
l=len([x[1] for x in lists])

for y in range(0,l-1):
    if len(a[y])==len(a[y+1]):
        a=list([r[1] for r in lists])
        print(a[y])
    elif len(a[y])==len(a[y+1]):
        print(a)
          



'''
https://docs.python.org/3/howto/sorting.html#sortinghowto
'''