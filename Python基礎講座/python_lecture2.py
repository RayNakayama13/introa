# import abc
#
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def say_something(self):
#         print('I am {}. Hello'.format(self.name))
#         self.run(10)
#
#     def run(self, num):
#         print('run' * num)
#
#     def __del__(self):
#         print('GOOD BYE')
#
# person = Person('Mike')
# person.say_something()
#
# del person
# print('#############')
#
# class Person():
#     def __init__(self, age=1):
#         self.age = age
#     def drive(self):
#         if self.age >= 18:
#             print('ok')
#         else:
#             raise Exception('No drive')
#
# class Baby(Person):
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError
#
# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError
#
#
# baby = Baby()
# adult = Adult()
#
#
# class Car(object):
#     def __init__(self, model=None):
#         self.model = model
#     def run(self):
#         print('run')
#     def ride(self, person):
#         person.drive()
#
# class ToyotaCar(Car):
#     def run(self):
#         print('fast')
#
# class TeslaCar(Car):
#     #ここでinitを作れば継承されるCARのinitを新しく書き換えてしまうためmodelをまた定義しないといけない。(self.model = model)ただCarのinitをそのまま使うには下のようにやると良い
#     def __init__(self, model='Model S', enable_auto_run=False):
#         super().__init__(model)
#         self.enable_auto_run = enable_auto_run
#
#     def run(self):
#         print('super fast')
#     def auto_run(self):
#         print('auto run')
#
# teslacar = TeslaCar()
# print(teslacar.model)
# teslacar2 = TeslaCar('Model 3')
# print(teslacar2.model)
#
# toyotacar = ToyotaCar('Lexus')
# print(toyotacar.model)
#
#
# print('#############')
#
#
# car = Car()
# # car.ride(baby)
# car.ride(adult)
# # car.ride(baby)
