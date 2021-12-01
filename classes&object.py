class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)  # output--> 5


#################

def sum():
    a = 20
    b = 40
    c = a + b
    return c


print("The sum is given by:", sum())

Output:
The
sum is given
by: 60


#################

class dog:
    attr1 = “Canidae”
    attr2 = “dog”

    def fun(self):
        print(“I’m
        a”, self.attr1)
        print(“I’m
        a”, self.attr2)

        Bruno = dog()
        print(Bruno.attr1)
        Bruno.fun();

        output:
        Canidae
        I’m
        a
        Canidae
        I’m
        a
        dog

        #################

        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def myfunc(self):
                print("Hello my name is " + self.name)

        p1 = Person("John", 36)
        p1.myfunc()

        # Hello my name is John

        #####################

        def max_of_two(x, y):
            if x > y:
                return x

        return y

        def max_of_three(x, y, z):
            return max_of_two(x, max_of_two(y, z))

        Sample
        Example
        to
        test
        the
        Program:

        print(max_of_three(3, 6, -5))
        # Output: 6

        #####################

        lass
        Person:

        def __init__(self, name):
            self.name = name

        def say_hi(self):
            print('Hello, my name is', self.name)

    p = Person('Vivek')
    p.say_hi()