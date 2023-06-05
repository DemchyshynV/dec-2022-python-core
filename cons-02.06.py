# # [num for num in st if num.isdigit()]
#
#
# st = '1hdhd4 44 jsdfj7d7d'
#
# # res = []
#
# # for ch in st:
# #     if ch.isdigit():
# #         res.append(ch)
#
# res = [ch for ch in st if ch.isdigit()]
#
# print(res)

def decor(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(count)

    return inner


@decor
def func1():
    print('func1')


@decor
def func2(msg):
    print(f'func2 {msg}')


func1()
func1()
func2('sss')
func1()
func2('gggg')
