>> > (lambda x: x + 1)(2)
3


##########################


def add_one(x):
    return x + 1


3

##########################

s = lambda a: a + 10
print(s(5))  # output -> 15


##########################


# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
    return y * y * y


lambda_cube = lambda y: y * y * y

# using the normally
# defined function
print(cube(3))

# using the lambda function
print(lambda_cube(3))
output - 3
3
##########################


>> > full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
>> > full_name('guido', 'van rossum')
'Full name: Guido Van Rossum'

##########################

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filter(lambda x: x % 2 == 0, list_1)
print(list(filter(lambda x: x % 2 == 0, list_1)))  # output -> [2, 4, 6, 8]


###########################

def myfunc(a, b):
    return a + b


x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(x)
print(list(x))

###########################

cubed = map(lambda x: pow(x, 3), list_1)
x = list(cubed)
print(x)  # [1, 8, 27, 64, 125, 216, 343, 512, 729]

############################

tables = [lambda x=x: x * 10 for x in range(1, 11)]

for table in tables:
    print(table())

'''
Output:
10
20
30
40
50
60
70
80
90
100
'''
#################################