# # comment
#
# """
# skhgfkjsdf
# lshdfkshjf
# ljshfdkj
#
# """
#
# '''
# sdfjhsdkjfhskjfk
# skdjhfksdhfjksdf
#
# '''
#
# # print(1, 2, 3, 4, sep='-', end='Finish\n')
#
#
# i = 3
# f = 1.3
# b = True  # False
# s = "text"  # 'text'
# n = None
#
# print(type(i))
# print(type(f))
# print(type(b))
# print(type(s))
# print(type(n))
#
#
# a=b=c=10

# print(a, b, c)
#
# fs = str(f)
#
# print(type(fs))
#
# print(fs)
#
#


# a = 11
# b = 2
# # a += 1
# # a = a + 1
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(round(a / b))
# print(2525 ** 2525)
# print(3 % 2)

# name = input('Enter your name: ')
#
# print(name)

# a = 2
# b = 3
# 
# print('a<b', a < b)
# print('a<=b', a <= b)
# print('a>b', a > b)
# print('a>=b', a >= b)
# print('a==b', a == b)  # print('a==b', a is b)
# print('a!=b', a != b)  # print('a==b', a is not b)
# 
# res = isinstance(a, str)
# 
# print(res)

# num = input('Enter num: ')
# num = int(num)
#
# if num > 10:
#     print('num >10')
# elif num == 10 or num>:
#     print('num == 10')
# else:
#     print('num < 10')


# check = False
#
# if not check:
#     print('Ok')


# num = int(input('Enter num: '))
#
# res = 'yes' if num > 5 else 'no'
#
# print(res)


# list
# l = [1, 2, 3, 4, "hjsdgf", True]
# print(l[0])
# # print(l[22])
# print(l[-2])
# l[3] = 6
# print(len(l))
# print(l)
# print('end')

# l = [1, 2, 3, 4, "hjsdgf", True]
# l2 = l.copy()
#
# l2[0] = 555
#
# print(l)
# print(l2)
# l = [1,2, 3, 4, "hjsdgf", 2, True]
# l2 = ['a','z','b']
# l.append(55)
# l.insert(2, 299)
# pop = l.pop()
# pop = l.pop(1)
# print(pop)
# l.remove(2)
# l.extend(l2)
# l += l2
# print(l.index(22, 3))
# l.reverse()
# l2.sort()
# print(l2)
# print(l.count(True))
# l.clear()

# l = [1,2, 3, 4, "hjsdgf", 2, True]
#
# sub = l[::-1]
#
# print(sub)


# tuple
# my_tuple = (1, 2, 3, 4, 5,5)
# print(my_tuple[1])
# # my_tuple[1]=4
# print(my_tuple.count(5))
# print(my_tuple.index(3))


# dict
# dict1 = {
#     'age':15,
#     'name': 'Max'
# }

# print(dict1)
# print(dict1['age'])

# get = dict1.get('name1', 'haha')
# print(get)
# print(dict1.items())
# print(list(dict1.items()))
# print(list(dict1.items())[0])
# print(dict1.keys())
# # pop = dict1.pop('name')
# pop = dict1.popitem()
# print(pop)
# print(dict1)

# dict1 = {
#     'age': 15,
#     'name': 'Max'
# }
#
# dict2 = {
#     'house': 45
# }
# # dict1.setdefault('age3', 55)
# # dict1.update(dict2)
# # dict1 |= dict2
# # print(dict1)

# print(dict1.values())


# set

# set1 = {1, 2, 3, 4, 1, 2, 3, 4}
# set1 = set()
# print(type(set1))
# set1.add(2)
# set1.add(4)
# set1.add(2)
# set1.add(7)
# print(set1)

# set_1 = {1, 2, 3, 4}
# set_2 = {5,6,1,4,7,8}
#
# # print(set_1.issuperset(set_2))
# # print(set_1.issubset(set_2))
# # print(set_1.isdisjoint(set_2))
# # print(set_1.intersection(set_2))
# difference = set_1.symmetric_difference(set_2)
# l = list(difference)
# print(difference)
# print(l)
# # set_1.remove(233)
# set_1.discard(4)
# pop = set_1.pop()
# print(set_1)

# string

# string = "name = 'Vasyl \"'"
#
# st = '*'*50
# print(st)
name = 'Max'
age = 18
weight = 70.5

string = 'Hello, my name is Max, I`m 18 and my weight 70.5 kg'
string = 'Hello, my name is ' + name + ', I`m ' + str(age) + ' and my weight ' + str(weight) + ' kg'
string = 'Hello, my name is %s, I`m %i and my weight %f kg' % (name, age, weight)
string = 'Hello, my name is {}, I`m {} and my weight {} kg'.format(name, age, weight)
string = 'Hello, my name is {name}, I`m {age} and my weight {weight} kg'.format(age=age, weight=weight, name=name)
string = f'hello, my name is {name}, I`m {age} and my weight {weight} kg'

# print(string)
# print(string.index('llo'))
# print(string.count('l'))
#
# print(string.capitalize())
# print(string.upper())
# print(string.lower())
# print(string.islower())
# print(string.isupper())

# print('hello world'.title())
# print('Hello World'.swapcase())
# print('asd'.isalpha())
# print('111s1'.isdigit())
# print('1111'.isnumeric())
# print('111s1'.isalnum())
# print('hello'.startswith('h'))
# print('hello'.endswith('h'))
#
# print(['    sfdsdf     '.strip()])
# print(['aaaa    sfdsdf     aaaa'.strip('a ')])
# print(['    sfdsdf     '.lstrip()])
# print(['    sfdsdf     '.rstrip()])
#
# print('hello-world'.split('-'))
# print('hello is hello'.partition('is'))

# l = ['1','2','3']
#
# print('-'.join(l))
#
# print(''.isspace())
# print('hello world'.replace('l', 'L'))
#
# print('hello world'[0])
# print('hello world'[:5])

# print(min([4, 2, 5, 6, 7]))
# print(max([4, 2, 5, 6, 7]))
# print(sum([4, 2, 5, 6, 7]))
# l = sorted([1, 2, 3, 4, -3])
# l2 = sorted([1, 2, 3, 4, -3], reverse=True)
# pow(2, 5) # **


# def func():
#     print('hello')
#
#
# func()
# c = 22


# def func(a, b=c, *args, **kwargs):
#     print(a, b, c)
#     print(args)
#     print(kwargs)
#
#
# func(1, 2, 333, 3, 4, 5, 6, 7, name='Max', age=18)


# l = [1, 2, 3]
# user = {
#     'name':'Max',
#     'age':15
# }
#
# def func(a, b, c, name, age):
#     print(a, b, c)
#     print(name, age)
#
#
# func(*l, **user)

# i = 5
#
# while i > 0:
#     i -= 1
#     if i == 2:
#         continue
#     print(i)
# else:
#     print('finish')

# users = ['Olha', 'Masha', 'Max']
#
# # for i in range(5, 50, 2):
# #     print(i)
# # for user in users:
# #     print(user)
# for i, user in enumerate(users):
#     print(i, user)


# user = {
#     'name': 'Max',
#     'age': 15,
#     'house': 87
# }
#
# for k, v in user.items():
#     print(k)
#     print(v)


# l = [i for i in range(10)]
# print(l)
# l = [1, 2, 3, 4, 5]
#
# # res = [i for i in l if i % 2 == 0]
# res = [str(i**2) for i in l if i % 2 == 0]
# print(res)

super_list = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]

# res = [i for j in super_list for i in j]

# res = []
# for j in super_list:
#     for i in j:
#         res.append(i)
#
#
# print(res)

dict1 = {'NaMe': 'Olha', 'aGe': 16}

dict2 = {k.lower():v for k,v in dict1.items()}

print(dict2)
