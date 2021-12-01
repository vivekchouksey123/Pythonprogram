# 2.Program to demonstrate Tuple

fruit = ("apple",)
fruit.append("hello") #gives error as tuples are immutable

x = list(fruit)
x.append("mango")
y = tuple(x)

###########################
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

###########################
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print tup3;

###########################

my_tuple=()
my_tuple #or print(my_tuple)

###########################
my_tuple=(1,"hello",3.14)
my_tuple

#########################

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#########################

#nested tuple
my_tuple=('house',[1,4,5],(3.14,5.5,60.5))
my_tuple

#########################

#unpacking
a,b,c=my_tuple
print(a," ",b," ",c)

########################