"""
8   Given two integer numbers return their sum. If the sum is greater than 100, then return their product.
9   Write a Python program to calculate the sum of three given numbers, if the values are not - equal then return four times of their sum
10  A shop will give discount of 50% if the cost of purchased quantity is more than 10000. Ask user for quantity suppose
    , one unit will cost 100. Judge and print total cost for user.
11  To check whether a number is divisible by 8 and 12 or not.
12  To check whether a given number is even or odd.
13  "Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
      Percentage >= 90% : Grade A
      Percentage >= 80% : Grade B
      Percentage >= 70% : Grade C
      Percentage >= 60% : Grade D
      Percentage >= 40% : Grade E
      Percentage < 40% :  Grade F"
14  Take input of age of 3 people by user and determine oldest and youngest among them.
15  "Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
      For first 50 units Rs. 0.50/unit
      For next 100 units Rs. 0.75/unit
      For next 100 units Rs. 1.20/unit
      For unit above 250 Rs. 1.50/unit
      An additional surcharge of 20% is added to the bill"
"""
# Answer 8

def sum(a,b):
    return a+b
a = int(input())
b = int(input())
sum = sum(a,b)
if sum > 100:
    print(a*b)
else:
    print(sum)

#Answer9

a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print(a+b+c)
else:
    print(a*b*c)


#Answer 10

unit = int(input())
cost = unit * 100
if cost > 10000:
    print(10000/2)
else:
    print(cost)

#Answer 11

num = int(input())
if num % 8 == 0 and num % 12 == 0:
    print ("number is divisible by 8 and 12")
else:
    print("number is not divisible by 8 and 12")

#Answer 12

num = int(input())
if num % 2 == 0:
    print("number is even")
else:
    print("number is add")

#Answer 13

def cal_p(a, b, c, d, e):
    per = int(int(a+b+c+d+e)/5)
    return per
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

Per = cal_p(a, b, c, d, e)

if Per >= 90:
    print("Grade A")
elif Per >= 80:
    print("Grade B")
elif Per >= 70:
    print("Grade C")
elif Per >= 60:
    print("Grade D")
elif Per >= 40:
    print("Grade E")
else:
    print("Grade F")

# Answer 14

a1, a2, a3 = [int(x) for x in input("Enter age of three persons: ").split()]
print("The Oldest person is of age:", max(a1, a2, a3))
print("The Youngest person is of age:", min(a1, a2, a3))


# Answer 15

def ans15():
    x = int(input("Enter Units of electricity: "))
    cost = 0
    if x - 50 > 0:
        cost = 50 * (.50)
        if x - 150 > 0:
            cost = cost + 75
            if x - 250 > 0:
                cost = cost + 120 + (x - 250) * 1.50
            else:
                cost = cost + (x - 150) * 1.20
        else:
            cost = cost + (x - 50) * .75
    else:
        cost = x * (0.50)
    cost = cost + cost / 5
    print("You have to Pay total amount of Rs.", cost)


ans15()