x = input("Enter First number:")
y = input("Enter Second Number:")
i = int(x)
j = int(y)
print("The Sum:", i + j)

Or else even
we
can
simplify
the
above
program:
x = int(input("Enter Fisrt number:"))
y = int(input("Enter Second Number:"))
print("The Sum:", i + j)

##########################

a, b = [int(x) for x in input("Enter two numbers:").split(",")]
print("The Sum:", a + b)

##########################

x = int(input(“Enter
Number
1: ”))
y = int(input(“Enter
Number
2: ”))
print(“The
sum = ”, x + y)

Output:
Enter
Number
1: 34
Enter
Number
2: 56
The
sum = 90

##########################

# Taking input from the user
name = input("Enter your name: ")

# Output
print("Hello, " + name)
print(type(name))