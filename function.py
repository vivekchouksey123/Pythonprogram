def my_function():
    print("Hello from a function")


my_function()


######################

def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


######################

def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(56))
print(absolute_value(-44))


# 56
# -44
############################

# defining the function
def change_string(str):
    str = str + " Hows you "
    print("printing the string inside function :", str)


string1 = "Hi I am there"

# calling the function
change_string(string1)

print("printing the string outside function :", string1)
Output:

printing
the
string
inside
function: Hi
I
am
there
Hows
you
printing
the
string
outside
function: Hi
I
am
there


############################

def my_func():
    x = 30
    print("Value inside function:", x)


x = 50
my_func()
print("Value outside function:", x)


# Value inside function: 30
# Value outside function: 50

############################

def greet(name, msg):
    print("Hello", name + ', ' + msg)


greet("Vivek", "Good Morning")


# Hello Vivek, Good Morning

############################

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(4)


############################

def factorial(x):  # Recursion
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))


num = 4
print("The factorial of", num, "is", factorial(num))


# The factorial of 4 is 24

###########################
# The output shows an error because we are trying to access a local variable y in a global scope whereas the local variable only works inside var() or local scope.
def var():
    y = "local"


var()
print(y)


##################################
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

# inner: nonlocal
# outer: nonlocal