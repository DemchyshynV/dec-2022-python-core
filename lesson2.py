# tuple1 = (1, 2)
#
# a, b = tuple1
#
# print(a, b)
#
#
#
# a = 5
# b = 6
#
# b, a = a, b
#
# print(a, b)

# t = (1,2,3)
# a,b = t
#
# print(a)

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # a, b, c, _, _, d = l
# #
# # print(a, b, c, d)
#
# a, b, *_, z,y = l
#
# print(a, b, z,y)
# print(_)

# def func(name, age, house):
#     print(name, age, house)
#
#
# user = {
#     'name': 'Max',
#     'house': 85,
#     'age': 15,
# }
# func(**user)

# l = [1,2,3]
# l2 = [4,5,6]
#
# l3 = [*l, *l2]
#
# print(l3)

# def decor(func):
#     def inner(*args, **kwargs):
#         print('*' * 20)
#         func(*args, **kwargs)
#         print('*' * 20)
#
#     return inner
#
#
# @decor
# @decor
# def greeting(name):
#     print(f'hello, {name}')


# @decor
# def greeting2(name, age):
#     print(f'Hello2, {name}-{age}')

# inner = decor(greeting)
# inner2 = decor(greeting2)
# inner('Max')
# inner2('Karina', 15)
# greeting2('Max', 15)

# greeting('max')

import time

#
#
# def time_decor(func):
#     def inner(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         print(time.time() - start)
#
#     return inner
#
# @time_decor
# def foo():
#     for i in range(100000000):
#         pass
#     print('finish')
#
#
# foo()

#
# for i in range(5):
#     print(i)
#
# print(i)

# name = 'Max'
# def a():
#     name = 'Karina'
#     print(locals())
#
# a()
# print(globals())
# # print(name)

# def a():
#     # global name
#     name = 'Karina'
#
# a()
#
# print(name)

# name = 'Max'
#
#
# def a():
#     # name = 'Kiril'
#
#     def b():
#         nonlocal name
#         # global name
#         name = 'Marina'
#         print(name)
#
#     b()
#     print(name)
#
#
# a()


# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#
#     return inner
#
#
# c1 = counter()
# c2 = counter()
# c1()
# c1()
# c2()
# c2()
# c1()
# c1()


# const func = (a,b)=>a+b

# func = lambda: 5
#
# print(func())

# users = [
#     {'name': 'max', 'age': 15},
#     {'name': 'Kamila', 'age': 16},
#     {'name': 'Albina', 'age': 20},
#     {'name': 'Artem', 'age': 27},
# ]
#
# sorted_users = sorted(users, key=lambda item: str(item['age'])[-1])
#
# print(sorted_users)


# def greeting(users: list[] ):
#     print(name)
#
#
# greeting(158)

# from typing import List, Tuple, Any


# def func(st: str, list_of_string: dict) -> int|str:
#     list_of_string.
#     for item in list_of_string:
#         print(item.upper())
#
#     return []
#
#
# func1 = func('aaa', [])

# print(func1)


from typing import Callable


def counter(start_num: int) -> Callable[[], int]:
    count = start_num

    def inner() -> int:
        nonlocal count
        count += 1
        return count

    return inner


counter1 = counter(5)
print(counter1())
