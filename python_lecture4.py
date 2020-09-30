# import tarfile
# import os
# import pathlib
#
#
# # os.mkdir('test_dir')
# # pathlib.Path('test_dir/test.txt').touch()
# # os.mkdir('test_dir/sub_dir')
# # pathlib.Path('test_dir/sub_dir/sub_test.txt').touch()
#
#
# # with tarfile.open('test.tar.gz', 'w:gz') as tr:
# #     tr.add('test_dir')
# #
# #
# # with tarfile.open('test.tar.gz', 'r:gz') as tr:
# #     # tr.extractall(path='test_tar')
# #     with tr.extractfile('test_dir/sub_dir/sub_test.txt') as f:
# #         # print(f.read())
# #
#
# import zipfile
# import glob
#
# # with zipfile.ZipFile('test.zip', 'w') as z:
# #     # z.write('test_dir')
# #     # z.write('test_dir/test.txt')
# #     for f in glob.glob('test_dir/**', recursive=True):
# #         print(f)
# #         z.write(f)
# #
# # with zipfile.ZipFile('test.zip', 'r') as z:
# #     # z.extractall('zzz2')
# #     with z.open('test_dir/test.txt') as f:
# #         print(f.read())
#
#
# import tempfile
#
# with tempfile.TemporaryFile(mode='w+') as t:
#     t.write('Hello')
#     #書き終わった後は最後の行の最後の文字にpositionがあるからそれをseekで１文字目に戻す
#     t.seek(0)
#     print(t.read())
#
# with tempfile.NamedTemporaryFile(delete=False) as t:
#     print(t.name)
#     with open(t.name, 'w+') as f:
#         f.write('test')
#         f.seek(0)
#         print(f.read())
#
#
# with tempfile.TemporaryDirectory() as td:
#     print(td)
#
# temp_dir = tempfile.mkdtemp()
# print(temp_dir)


# Max = 10000
# List = range(2, Max+1)
# for i in range(2, int(Max ** 0.5)):
#     List = [x for x in List if (x == i or x % i != 0)]
# for j in List:
#     print(j)
#
# a=b=1
# while a < 2**31:
#     print(a)
#     a, b = b, a+b
#

# with open('/Users/raynakayama/Documents/School Work/code/ test.txt', 'w+') as f:
#     f.write('1,2,3,4,5,6,7,8,9,10,11,1000,422,2415,7,48848,959944,5215')
#     f.seek(0)
#     A = f.read()
#     l = [int(x.strip()) for x in A.split(',')]
#     print(l)
#     l.sort()
#     print(l)

# a = 5
# b = 2
#
# print('{} + {} = {}'.format(a,b,a+b))
# print('{} - {} = {}'.format(a,b,a-b))
# print('{} x {} = {}'.format(a,b,a*b))
# print('{} / {} = {} 余り {}'.format(a,b,a//b,a%b))
#
#
#
# for i in range(4, 9, 2):
#     print(i)


# z = [(1,3),(2,5)]
#
# for n in len(z):
#     i = z[n][0]
#     s = z[n][1]


# def base(x):
#     def plus(y):
#         return x + y
#     return plus
#
# plus = base(10)
# print(plus(10))
# print(plus(20))
#
#
# def add_num():
#         def plus(y):
#             return i + y
#         return plus
# i = 100
# plus = add_num()
# print(plus(10))
