# try:
#     with open('1.txt') as file:
#         # print(file.read(3))
#         # print(file.read(2))
#         # file.seek(0)
#         # print(file.readline(), 'aaaaaaaaaaaaaaaaaaaa')
#         for line in file:
#             print([line.strip()])
# except Exception as err:
#     print(err)


class User:
    __match_args__ = 'name', 'age'

    def __init__(self, name, age):
        self.age = age
        self.name = name


#
#
# user = User('Max')
# print(user.__dict__)


users = [
    {'name': 'Max', 'age': 15},
    {'name': 'Olha', 'age': 20},
    {'name': 'Kamila', 'age': 30},
    User('Mark', 20),
    User('Kokos', '20'),
    ('Albina', 20),
    ('Alex', 25),
    ('aaaa',)
]


def to_dict(data: User | dict | tuple[str, int]):
    match data:
        case {} as dict_user:
            print(dict_user)
        case User(age=int(20)) as class_user:
            print(class_user.__dict__)
        case name, age:
            print({'name': name, 'age': age})


for user in users:
    to_dict(user)
