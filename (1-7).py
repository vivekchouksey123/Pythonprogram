"""
1	Display float number with 2 decimal places using print()
2	Takes two integer numbers and  return their product.
3	Write a Python program to get the volume of a sphere with radius 10.
4	Accept two numbers from the user and multiply them together.
5	Write a Python program that accepts an integer (a) and computes the value of a+aa+aaa.
6	Write a Python program to calculate the length of a string
7	Write a Python program to parse a string to Float & Integer
"""

"""Answer 1"""
def A1():
    x = 6.6666
    print(round(x, 2))  # First
    print("{: .2f}".format(x))  # second
A1()

#Answer 2
def A2(a, b):
    return (a * b)
x = int(input())
y = int(input())
print(A2(x, y))

#Answer 3
def v_sphere(r):
    vol = (4/3)*3.14*(r**3)
    return vol
r = int(input())
print(v_sphere(r))

#Answer 4
a = int(input())
b = int(input())
print(a*b)

#Answer 5
a = int(input())
eq = a + (a * a) + (a * a * a)
print(eq)

#Answer 6
s = "Akshat"
print(len(s))

#Answer 7

a = "10101"
b = "10101.000"
f = float(b)
i = int(a)
print(type(a), type(b), type(f), type(i))