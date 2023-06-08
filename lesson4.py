# name = 'Max'
#
# for i in range(10):
#     print(i)
#
#
# def a(asd):
#     int_value = int(asd)
#     print(int_value)
#
#
# a('125')

# try:
#     # ksjhdfkjshfk
#     # sdfsdf
#     print(4/0)
# except NameError as err:
#     print(err)
# except ZeroDivisionError:
#     print(0)
# try:
#     # ksjhdfkjshfk
#     # sdfsdf
#     s = int(input('Enter num'))
#     print(4/0)
# except KeyboardInterrupt:
#     print('stoped by user')
# except ValueError as err:
#     print(err)
# # except Exception as err:
# #     print(err)
# else:
#     print('all right')
# finally:
#     print('finish')
#
# print('end')


# l = [i*25 for i in range(50000000)]
# input()

# g = (i*25 for i in range(50000000))
# # print(type(g))
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# g = (i for i in range(5))
#
# # print(next(g))
# # print('my work')
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
#
# for item in g:
#     print(item)
#
# for item in g:
#     print(item)

# def gen(name):
#     for ch in name:
#         yield ch
#         print('aaaaaaaaaaaaa')
#
#
# g = gen('Max')
#
# print(next(g))
# print(next(g))


# def gen():
#     yield 1
#     yield 2
#     yield 3
#     return 'return'
#
#
# g = gen()
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


def gen_file_name():
    count = 0
    while True:
        yield f'file-{count}.jpg'
        count += 1


gen = gen_file_name()


#
# print(next(gen))
# print('skhdfgjhsf')
# print('skhdfgjhsf')
# print('skhdfgjhsf')
# print('skhdfgjhsf')
#
# print(next(gen))


# def gen1(n):
#     for i in range(1, n + 1):
#         yield f'{i}-Team1'
#
#
# def gen2(n):
#     for i in range(1, n+1):
#         yield f'{i}-Team2'
#
#
# teams = [gen1(8), gen2(5)]
#
# while teams:
#     team = teams.pop(0)
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration:
#         pass


class MyRange:
    def __init__(self, length):
        self.__length = length
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.__length:
            res = self.__counter
            self.__counter += 1
            return res
        raise StopIteration


# for i in MyRange(5):
#     print(i)

# my_range = MyRange(3)
#
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))

# def my_range(length):
#     count = 0
#     while count < length:
#         yield count
#         count += 1
#
# for i in my_range(5):
#     print(i)


# file = open('1.txt')
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# try:
#     file = open('1.txt')
#     try:
#         print(file.read())
#     finally:
#         file.close()
# except Exception as err:
#     print(err)

# try:
#     with open(file='1.txt', mode='r') as file:
#         print(file.read(3))
#         print(file.read(3))
#         print(file.read(3))
#         file.seek(1)
#         print('*********************')
#         print(file.read(3))
#
#
#         # print(file.readline())
#         # print(file.readlines())
# except Exception as err:
#     print(err)


# try:
#     with open(file='1.txt', mode='w') as file:
#         # file.write('some\ntext\n')
#         # file.writelines(['max\n', 'hello\n', 'okten\n'])
#
# except Exception as err:
#     print(err)

# try:
#     with open(file='1.txt', mode='a') as file:
#         file.write('asd\n')
#
# except Exception as err:
#     print(err)

# try:
#     # with open(file='1.txt', mode='r+') as file:
#     # with open(file='1.txt', mode='w+') as file:
#     with open(file='1.txt', mode='x') as file:
#         print(file.readline())
#         file.write('aaaaaaaaaaaaaaaaaaaaaaa\n')
# except Exception as err:
#     print(err)

#
# try:
#     with open('max.jpg', 'rb') as file:
#         for i in range(5):
#             with open(next(gen), 'wb') as f:
#                 read = file.read()
#                 f.write(read)
#                 file.seek(0)
# except Exception as err:
#     print(err)


import json
import pickle


# users = [
#     {'name': 'Max', 'age': 15},
#     {'name': 'Kira', 'age': 20},
#     {'name': 'Kokos', 'age': 20},
# ]


# try:
#     with open('users.json', 'w') as file:
#         json.dump(users, file)
# except Exception as err:
#     print(err)
#
# try:
#     with open('users.json', 'r') as file:
#         users:list = json.load(file)
#         for i in users:
#             print(i)
# except Exception as err:
#     print(err)


# try:
#     with open('data', 'wb') as file:
#         pickle.dump(users, file)
# except Exception as err:
#     print(err)

# try:
#     with open('data', 'rb') as file:
#         users: list = pickle.load(file)
#         for i in users:
#             print(i)
# except Exception as err:
#     print(err)

# choice = input('Make your choice: ')
#
# match choice:
#     case '1':
#         print('1')
#     case '2':
#         print('2')
#     case _:
#         print('default')
class User:
    __match_args__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Max', 66)

user_dict = {
    'name': 'Alisa',
    'age': 45
}

# def matcher(source: User | dict):
#     if isinstance(source, User):
#         print(source.name)
#     if isinstance(source, dict):
#         print(source['name'])
#
#
# matcher(user_dict)

# def matcher(source: User | dict):
#     match source:
#         case User(_, age=3 as age):
#             print(f'{age=}')
#         case User(_, age):
#             print('User(_,age)', age)
#         case {'name': 'Alisa' as name}:
#             print(name)
#         case {'name': name}:
#             print(name, "{'name': name}")
#         case _:
#             print('Not Found')
#
#
# matcher(user_dict)


action = 'right 350 sdf sdf '.split()

match action:
    case 'top' | 'left' as ac, '150'|'350' as val:
        print("'top'|'left' as ac, '150'")
    case ac, val:
        print(f'{ac=} {val=}')
    case ac, val, *arg:
        print(f'{ac=} {val=} {arg=}')
