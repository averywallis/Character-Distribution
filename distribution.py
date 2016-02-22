"""
distribution.py
Author: Avery Wallis
Credit: Ethan

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
a=(string1.count('a'))
b=(string1.count('b'))
c=string1.count('c')
d=string1.count('d')
e=string1.count('e')
f=string1.count('f')
g=string1.count('g')
h=string1.count('h')
i=string1.count('i')
j=string1.count('j')
k=string1.count('k')
l=string1.count('l')
m=string1.count('m')
n=string1.count('n')
o=string1.count('o')
p=string1.count('p')
q=string1.count('q')
r=string1.count('r')
s=string1.count('s')
t=string1.count('t')
u=string1.count('u')
v=string1.count('v')
w=string1.count('w')
x=string1.count('x')
y=string1.count('y')
z=string1.count('z')
list1=list()
list1=list1.append(a)
list1=list1.sort()
print(list1)

