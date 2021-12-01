# 1.Program to show list comprehension

l = ['hello', 'user', 1]

for x in l:
    print(x, end=" ")

###############################
my_list = []
my_list

###############################
my_list = [1, 2, 3]
my_list

###############################
my_list = [1, "hello", 3.4]
my_list

###############################
my_list = ['c', 's', 'i', 't', 'a', 'c', 'r', 'o']
my_list[0]

##############################
my_list = ['c', 's', 'i', 't', 'a', 'c', 'r', 'o', [2, 0, 1, 3]]
my_list[-1][1]

##############################
my_list[2:5]

##############################
my_list[-1][1] = 9  # list are mutable
my_list

##############################
my_list.extend([9, 11, 14])
my_list

############################
print(my_list + [11, 12, 13])

##########################
print(["hello"] * 5)

##########################
my_list.insert(1, 90)
my_list

###########################
odd = [1]
my_list.append(odd)
my_list

###########################
my_list = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
my_list.remove(3)
my_list