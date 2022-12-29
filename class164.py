# advabnce min() and max()

# numbers = [1,2,4,5,7]
# print(min(numbers))


names = ['subhradeep manna', 'sourya', 'ab', 'z']
print(max(names,key = lambda item : len(item)))

students = {
    'subhradeep' : {'score':50, 'age': 19},
    'sourya' : {'score':75, 'age': 16},
    'rajeev' : {'score':76, 'age': 23}
}

print(max(students, key = lambda item : students[item]['age']))

# students2 = [
#     {'name':'subhradeep','score':90, 'age': 19},
#     {'name':'sourya','score':70, 'age': 16},
#     {'name':'rajeev','score':60, 'age': 23},
# ]
# print(max(students2,key = lambda item:item.get('age'))['name'])
