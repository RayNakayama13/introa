# print('hello')
# print('i don\'t know')
# print('hi')
#
# for num in [1,2,3]:
#     print(num)
# print('##########')
# print("""\
# line1
# line2
# line3\
# """)
# print('##########')
#
# word = 'python'
# word = 'j' + word[1:]
# print(word)
# print(len(word))
#
#
# s = 'My name is Mike. Hi Mike'
# is_start = s.startswith('My')
# print(is_start)
# print(s.rfind('Mike'))
# print(s.title())
# print(s.upper())
# print(s.replace('Mike', 'Nancy'))
#
# 'My name is {name} {family}. Watashi ha {family} {name}'.format(name='Ray', family='Nakayama')
#
# a = 'ni'
# print(f'a is {a}')
#
# x, y, z = 1, 2, 3
# print(f'a is {x}, {y}, {z}')
#
# r = [1, 2, 3, 4, 5, 6, 1, 2, 3]
# print(r.index(3, 3))
#
# r.sort()
# # print(r)
#
# s= 'My name is Mike'
# to_split = s.split(' ')
# print(to_split)
#
# i = [1, 2, 3, 4]
# j = i[:]
# #or j = i.copy() prefered
# i.append(10)
# j.append(20)
# print(i)
# print(j)
# print(id(i))
#
# t = 1
# print(type(t))
#
#
# num_tuple = (10, 20)
# x, y = num_tuple
# print(x, y)
#
# chose_from_two = ('A', )
#
# answer = []
# answer.append('A')
# print(answer)
#
#
# fruit =  {
#     'apple' : 100,
#     'banana' : 200,
#     'orange' : 300,
# }
#
# print(fruit['apple'])
#
# a = {1, 2, 2, 3, 3, 4, 4, 4, 5}
#
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print('done')
#
#
# for _ in range(10):
#     print('hello')
#
#
# for i, fruits in enumerate(['apple', 'banana', 'orange']):
#     print(i, fruits)
#
#
# day = ['Mon', 'Tue', 'Wed']
# fruit = ['Apple', 'Banana', 'Orange']
# drink = ['coffee', 'coke', 'sprite']
#
# for days, fruits, drinks in zip(day, fruit, drink):
#     print(days, fruits, drinks)
#
#
# def what_is_this(color):
#     if color == 'red':
#         return 'tomato'
#     elif color == 'green':
#         return 'green pepper'
#     else:
#         return 'I dont know'
#
# result1 = what_is_this('red')
# result2 = what_is_this('green')
# result3 = what_is_this('yellow')
# print(result1,',', result2,',', result3)
#
#
# def test_func(x, l=[]):
#     l.append(x)
#     return l
#
# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)
# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)
# #ここではlistの値がしっかり毎回変わって表示される
#
# r = test_func(100)
# print(r)
# r = test_func(100)
# print(r)
# #こっちではlistに一つ目の値が入ったままで二つ目のrが出される。だから下でやる
#
# def test_func(x, l=None):
#     if l is None:
#         #lの引数が設定されていないときに新しくlistが作られるように設定する
#         l = []
#     l.append(x)
#     return l
# r = test_func(100)
# print(r)
# r = test_func(100)
# print(r)
#
#
# #*を忘れないようにする
# def say_something(word, *args):
#     print('word :', word)
#     for arg in args:
#         print(arg)
#
# t = ('Mike', 'Nancy')
# say_something('Word', *t)
#
# def  outer(pi):
#     def calculate(radius):
#         return pi * radius * radius
#
#     return calculate
#
# cal1 = outer(3.14)
# cal2 = outer(3.141592)
#
# print(cal1(10))
# print(cal2(10))
#
# print('########################')
# print('########################')
#
# def print_info(func):
#     def wrapper(*args, **kwargs):
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper
#
# def print_more(func):
#     def wrapper(*args, **kwargs):
#         print('func:', func.__name__)
#         print('args:', args)
#         print('kwargs:', kwargs)
#         result = func(*args, **kwargs)
#         print('result:', result)
#         return result
#     return wrapper
#
# @print_info
# @print_more
# def add_num(a, b, **kwargs):
#     return a + b
#
# f = print_info(add_num)
# d = {
#     'entree': 'beef',
#     'drink' : 'beer'
# }
# r = add_num(1, 4, **d)
# print(r)
#
#
# l = ['Mon', 'tue', 'Wed', 'thu', 'fri']
#
# def change_words(words, func):
#     for word in words:
#         print(func(word))
#
# #lambdaを使えばfunctionを引数にするとき行がかさまなくてすむ
# change_words(l, lambda word: word.lower())
#
# def capitalize(words):
#     return words.capitalize()
# change_words(l, capitalize)
#
# print('###############')
#
# def counter(num):
#     for _ in range(num):
#         yield 'run'
# def greeting():
#     yield 'Good Morning'
#     yield 'Good Afternoon'
#     yield 'Good Night'
#
# g = greeting()
# c = counter(2)
#
# print(next(g))
# print(next(c))
# print(next(g))
# print(next(c))
# print(next(g))
#
#
#
# t = (1, 2, 3, 4)
# #list内にforなどを表記することができる。リスト内表記
# r = [i for i in t if i % 2 == 0]
# s = [i for i in t]
# print(r)
# print(s)
#
#
# g = (i for i in range(10))
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#
# t = tuple(i for i in range(10))
# print(type(t))
#
# l = [i for i in range(10)]
# print(l)
#
# w = ['mon', 'tue', 'wed']
# f = ['coffee', 'milk', 'tea']
#
# d = {}
# for x, y in zip(w, f):
#     d[x] = y
# print(d)
#
# d = {x:y for x, y in zip(w, f)}
# print(d)
#
# animal = 'cat'
#
# def f():
#     animal = 'dog'
#     print('after', animal)
#     print('locals:', locals())
#
# f()
# print('globals:', globals())
# #print(animal)
#
# # try:
# # except:
# # finally:
#
#
#
# class UppercaseError(Exception):
#     pass
#
# def check(l):
#     for i in l:
#         if i.isupper():
#             raise UppercaseError(i)
# L = ['APPLE', 'banana', 'orange']
# # check(L)
#
#
#
# d ='通常、開発をする際などにはそのファイルがimportされた時点でそのファイル内にあるfuncは実行されてしまう。それを避けるためにしたのif文defで書く。'
# print(len(d))
# def main():
#     print('hello world')
#
# if __name__ == '__main__':
#     main()
