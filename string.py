# 3.Program to demonstrate String in Python

# Iterating through a string
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')


# find the index of a "c" in a string "abcde"
>>>  "abcde".index("c")
2

>>> “1:2:3”.split(“:”)
[‘1’, ‘2’, ‘3’]


>>> print("I love {programming} in {python}".format(programming="programming", python="Python"))
'I love programming in Python'


str = 'program'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])

#################################

greeting = 'Good '
time = 'Afternoon'
greeting = greeting + time + '!'
print(greeting)

#################################

str = "Python String"
new_str = 'J' + str[1:]
print(new_str)


Traceback (most recent call last):
  File "app.py", line 2, in <module>
    str[0] = 'J'
TypeError: 'str' object does not support item assignment</module>


################################

str = 'cold'
# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))