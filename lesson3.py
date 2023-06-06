# class User:
#     __slots__ = ('name', 'age')
#     count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# user1 = User('Max', 15)
# print(user1.age)
# print(user1.name)
# user1.house = 85
# # user2 = User('Karina', 20)
# # print(User.count)
# # User.count = 88
# #
# # print(user1.count)
# # print(user2.count)
# #
# # print(User.count)
#
# # user1.house = 85
# #
# # print(user1.house)
# #
# # del user1.house
# #
# # print(user1.house)


# class User:
#     __count = 0
#     def __init__(self, name):
#         self.__name = name
#         self.age = 15
#
#
# # print(User.__count)
# user = User('Max')
# print(user.age)
# # print(user._name)
#
# print(user._User__name)
# print(User._User__count)

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#
# class Greeting:
#     def greeting(self):
#         print('Hello')
#
#
# class SuperCar(Car, Greeting):
#     def __init__(self, brand, model, year, battery):
#         super().__init__(brand, model, year)
#         self.battery = battery
#
#
# car = SuperCar('Kia', 'Cerato', 2008, None)
#
# print(car.greeting())


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def __set_name(self, name):
#         self.__name = name
#
#     def __get_name(self):
#         return self.__name
#
#     def __delete_name(self):
#         del self.__name
#
#     name = property(fget=__get_name, fset=__set_name, fdel=__delete_name)
#
#
# user = User('Max')
#
# user.name = 'Karina'
# print(user.name)
# del user.name
# print(user.name)
# # print(user.get_name())
# # user.set_name('Karina')
# # print(user.get_name())
# # user.delete_name()
# # print(user.get_name())


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# user = User('Max')
# user.name = 'Karina'
# del  user.name
# print(user.name)

# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         return self.a * self.b * self.c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     def perimeter(self):
#         return self.a * self.b * 2
#
#
# shapes: list[Shape] = [Triangle(1, 2, 3), Rectangle(4, 5), Triangle(3, 4, 5)]
#
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimeter())
#


# class User:
#     __count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def get_count(cls):
#         return cls.__count
#
#     @classmethod
#     def inc_count(cls):
#         cls.__count += 1
#
#     @staticmethod
#     def greeting():
#         print('hello')
#
# User.inc_count()
# User.inc_count()
# User.inc_count()
# User.inc_count()
# User.inc_count()
# print(User.get_count())
# User.greeting()


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'{self.name} - {self.age}'
#
#     def __len__(self):
#         return len(self.name)
#
#     def __add__(self, other):
#         return self.age + other.age
#
#     def __sub__(self, other):
#         return self.age - other.age
#
#     def __mul__(self, other):
#         return self.age * other.age
#
#     def __lt__(self, other):
#         return len(self.name) < len(other.name)
#
#
# user1 = User('Max', 15)
# user2 = User('Karina', 20)
# print(user2 < user1)
# print(len(user))

# print(user)

# class User(object):
#     __instance = None
#     count = 0
#
#     def __new__(cls, *args, **kwargs):
#
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super().__new__(cls)
#
#         return cls.__instance
#
#     def __init__(self, name):
#         self.name = name
#         User.count += 1
#
#
# user1 = User('Max')
# user2 = User('Max')
#
# print(user1)
# print(user2)
# print(user1 is user2)


# class User:
#     pass
#
# class Dog:
#     pass
#
#
# user = User()
# dog = Dog()
#
# print(isinstance(None, Dog))

# class Prod:
#     def __init__(self, value):
#         self.value = value
#
#     def __call__(self, inc):
#         self.value += inc
#
#     def __str__(self):
#         return str(self.value)
#
#
# prod = Prod(20)
# prod(50)
# print(prod)
# prod(1)
# print(prod)


# class Array:
#     def __init__(self, *args):
#         self.__arr = [*args]
# 
#     def __str__(self):
#         return str(self.__arr)
# 
#     def length(self):
#         return len(self.__arr)
# 
#     def __setitem__(self, key, value):
#         self.__arr[key] = value
# 
#     def __getitem__(self, key):
#         return self.__arr[key]
# 
#     def __delitem__(self, key):
#         del self.__arr[key]
# 
#     def map(self, cb):
#         return Array(*[cb(item) for item in self.__arr])
#     def push(self, item):
#         self.__arr.append(item)
# 
# 
# array = Array(1,2,3,4,5,6)
# # array.push(1)
# # array.push(2)
# # print(array[0], 'ssssssssss')
# # array[1] = 'sdf'
# # del array[1]
# # print(array.length())
# # print(array)
# 
# array2 = array.map(lambda x: x ** 2)
# 
# print(array)
# print(array2)


class Car:
    def __init__(self, name):
        self.name = name

    def get_car_name(self):
        print(self.name)


class SuperCar(Car):
    def __init__(self, name):
        super().__init__(name)
        super().get_car_name()

    def get_car_name(self):
        super().get_car_name()
        return self.name


car = SuperCar('BMW')
print(car.get_car_name())
