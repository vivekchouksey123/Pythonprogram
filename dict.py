thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#################

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

####################

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))

####################

Dict = {1: 'JavaTpoint', 2: 'Peter', 3: 'Thomas'}

pop_ele = Dict.pop(3)
print(Dict)

###################
dict = {'Name': 'Vivek', 'Age': 19, 'Class': '12'}
del dict['Name'];
dict.clear();
del dict;

print
"dict['Age']: ", dict['Age']
print
"dict['School']: ", dict['School']
###################

Dict = {'Dict1': {1: 'Vivek},
        'Dict2': {'Name': 'For'}}

print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])