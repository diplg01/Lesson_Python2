                                                # ФАЙЛЫ

# with open('file.txt', 'a') as data:
#     data.write('LINE012\n')
#     data.write('LINE123\n')

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.write('\nLINE2\n')
# data.write('LINE3\n')
# data.close()



# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

                                                # ФУНКЦИИ 

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1', 'd', '2'))  # a1d2
# # print(conatenatio(1, 2, 3, 4)) # TypeError

                                                # КОРТЕЖИ

# a = (1, 2)
# print(a)
# print(a[-1])

                                                # СЛОВАРИ

# dictionary = {}
# dictionary = \
# {
#     'up': '↑',
#     'left': '←',
#     'down': '↓',
#     'right': '→'
# }
# print(dictionary['up'])
# dictionary['up'] = 'up'
# print(dictionary['up'])
# # print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# # print(dictionary['left'])  # ←
# #  # типы ключей могут отличаться

# for v in dictionary:
#     print(v)

                                        # МНОЖЕСТВА 

# colors = {'red', 'green', 'blue'}
# print(colors)     # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors)       # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)       # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors)       # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red')  # ok
# print(colors)       # {'green', 'blue','gray'}
# colors.clear()      # { }
# print(colors)       # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()               # c = {1, 2, 3, 5, 8}
# u = a.union(b)             # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)      # i = {8, 2, 5}
# dl = a.difference(b)       # dl = {1, 3}
# dr = b.difference(a)       # dr = {13, 21}

# q = a \
#     .union (b) \
#     .difference(a.intersection(b))
# # {1, 21, 3, 13}

# s = frozenset(a)

                                        # СПИСКИ 

# list1 = [1,2,3,4,5]
# list2 = list1

# for e in list1:
#     print(e)    
# print()

# for e in list2:
#     print(e)
# print()

# list1 [0] = 123
# list2 [1] = 333

# for e in list1:
#     print(e)
# print()

# for e in list2:
#     print(e)

# list1 = [1,2,3,4,5]
# print(len(list1))
# print(list1)
# print(list1.pop())
# print(list1)                     # Удаление элеменнтов по одному
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# print(len(list1))
# print(list1)                     # удаление конкретного эллемента
# print(list1.pop(2))
# print(list1)

# print(list1.insert(2, 11))
# print(list1)                     # Добавление нового элемента между имеющимися


# print(list1.append(11))
# print(list1)                       # Добавление в конец 