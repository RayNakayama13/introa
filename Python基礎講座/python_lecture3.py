# class Person(object):
#     def talk(self):
#         print('talk')
#
# class Car(object):
#     def run(self):
#         print('run')
#
# #先にあるpersonが先に行われる
# class PersonCarRobot(Person, Car):
#     def fly(self):
#         print('fly')
#
# person_car_robot = PersonCarRobot()
# person_car_robot.talk()
# person_car_robot.run()
# person_car_robot.fly()
#
#
# class Person(object):
#
#     kind = 'human'
#
#     def __init__(self, name):
#         self.name = name
#         # self.kind = kind
#     def who_are_you(self):
#         print(self.name, self.kind)
#
# a = Person('A')
# a.who_are_you()
# b = Person('B')
# b.who_are_you()
#
#
# class T(object):
#
#     words = []
# #毎回リストがリセットされた状態で始めないと一個前の処理が次の処理にも影響を与えてしまう。よって__init__で最初にリストの初期化をする。
#     def __init__(self):
#         self.words = []
#     def add_word(self, word):
#         self.words.append(word)
#
# c = T()
# c.add_word('add 1')
# c.add_word('add 2')
# print(c.words)
#
# d = T()
# d.add_word('add 3')
# d.add_word('add 4')
# print(c.words)
#
#
# class Person(object):
#
#     kind = 'human'
#
#     def __init__(self):
#         self.x = 100
#
#     @classmethod
#     def what_is_your_kind(cls):
#         return cls.kind
#
#     @staticmethod
#     def about(year):
#         print('about human {}'.format(year))
#
# a = Person()
# print(a)
# print(a.x)
# print(a.kind)
# print(a.what_is_your_kind())
# b = Person
# print(b)
# # print(b.kind)
# # print(b.x)
# # print(b.who_is_your_kind)
#
#
# Person.about(1999)
#
#
# class Word(object):
#
#     def __init__(self, text):
#         self.text = text
#     def __str__(self):
#         return 'WORD !!!!!'
#     def __len__(self):
#         return len(self.text)
#     def __add__(self, word):
#         return self.text.lower() + word.text.lower()
#
# w = Word('TEST')
# w2 = Word('##########')
# print(type(w))
# print(type(w2))
# #本来ならw+w２はできない.でもここで__add__の特殊メソッドがWord内にあるから可能になっている。
# print(w + w2)
#
#


#
# """
# ###########################################################
# open(), withによるファイル読み書き（入出力）
# エンコード指定: 引数encoding
# テキストファイルの読み込み
# 読み込み用でファイルオープン: 引数mode='r'
# ファイル全体を文字列として読み込み: read()
# ファイル全体をリストとして読み込み: readlines()
# ファイルを一行ずつ読み込み: readline()
# テキストファイルの書き込み（新規作成・上書き）
# ###########################################################
# 書き込み用でファイルオープン: 引数mode='w'
# 文字列を書き込み: write()
# リストを書き込み: writelines()
# 空のファイルを作成: pass文
# ファイルが存在しない場合のみ書き込み（新規作成のみ）
# ###########################################################
# 新規作成専用でファイルオープン: 引数mode='x'
# ファイルの存在を確認してからオープン
# テキストファイルの書き込み（追記・挿入）
# ###########################################################
# 末尾に追記: mode='a'
# 先頭、途中に挿入
# mode='r+'
# readlines(), insert()を使う
# バイナリファイルの読み書き
# ###########################################################
# """
#
#
#
# s = """\
# AAA
# BBB
# CCC
# DDD
# """

# with open('test.txt', 'w') as f:
    # f.write(s)
# with open('test.txt', 'r') as f:
    # # print(f.read())
    # while True:
    #     chunk = 2
    #     # line = f.readline()
    #     # print(line, end='')
    #     line = f.read(chunk)
    #     print(line)
    #     if not line:
    #         break
    # print(f.tell())


# import string

# with open('/Users/raynakayama/Documents/School Work/Code/python/test.txt') as f:
    # t = string.Template(f.read())

# contents = t.substitute(name='Mike', content='How are you doing?')
# print(contents)

#
# s ="""\
# Hi $name
# $content
# Have a nice day
# """
#
# h = string.Template(s)
# #これでtemplate化がなされる
# content2 = t.substitute(name='Nancy', content='Waddup')
# print(content2)
#
#
# import csv
#
# with open('test.csv', 'w') as csv_file:
#     fieldnames = ['Name', 'Count']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'Name': 'A', 'Count' :1})
#     writer.writerow({'Name': 'B', 'Count' :2})
#
# #terminalにopen test.csvと書けばexcelで開かれる
#
# with open('test.csv', 'r') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         print(row['Name'], row['Count'])


# import os
# import pathlib
# import glob
# import shutil
#
# print(os.path.exists('test.txt'))
# print(os.path.isfile('test.txt'))
# print(os.path.isdir('test.txt'))

# os.rename('renamed.txt', 'test.txt')
# os.symlink('test.txt', 'symlink.txt')
# os.rmdir('test_dir')

# pathlib.Path('empty.txt').touch()
# os.remove('/Users/raynakayama/Documents/School Work/Code/python/empty.txt')

# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# print(os.listdir('test_dir'))
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()
# shutil.copy('test_dir/test_dir2/empty.txt',
            # 'test_dir/test_dir2/empty2.txt')
# print(glob.glob('test_dir/test_dir2/*'))


# shutil.rmtree('test_dir')

# print(os.getcwd())
#
# with open('python_lecture4', 'w') as f:
#     print('Hello')
#
# os.rename('python_lecture4', 'python_lecture4.py')
