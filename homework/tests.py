from homework.data import Employee
from homework.structure import DoubleLinked

emp_1 = Employee('emp_1000', 'S. A', 1000, 200)
emp_2 = Employee('emp_100', 'P. V.', 100, 200)
emp_3 = Employee('emp_200', 'V. B.', 200, 200)
emp_4 = Employee('emp_300', 'V. M.', 300, 200)
emp_5 = Employee('emp_400', 'V. M.', 400, 200)
emp_6 = Employee('emp_1232', 'V. M.', 1232, 200)
emp_7 = Employee('emp_12', 'V. M.', 12, 200)
emp_8 = Employee('emp_2325', 'V. M.', 2325, 200)
emp_9 = Employee('emp_123', 'V. M.', 123, 200)
emp_10 = Employee('emp_333', 'V. M.', 333, 200)
emp_11 = Employee('emp_1222', 'V. M.', 1222, 200)
emp_12 = Employee('emp_2323', 'V. M.', 2323, 200)
emp_13 = Employee('emp_23', 'V. M.', 23, 200)
emp_14 = Employee('emp_1', 'V. M.', 1, 200)
emp_15 = Employee('emp_0', 'V. M.', 0, 200)



#####################
## Тест __init__
#####################
print('Тест __init__')

a = DoubleLinked()
b = DoubleLinked(emp_1)


a.print()
b.print()

print('~'*20)


#####################
## Тест add - добавление в конец
#####################
print('Тест add - добавление в конец')

a = DoubleLinked()
a.add(emp_4)
a.print()

b = DoubleLinked(emp_1)
b.add(emp_1)
b.add(emp_2)
b.add(emp_3)
b.print()


print('~'*20)


#####################
## Тест concat - слияние двух списков
#####################
print('Тест add - добавление в конец')

a = DoubleLinked()
a.print()

b = DoubleLinked(emp_1)
b.add(emp_1)
b.add(emp_2)
b.add(emp_3)
b.print()

c = DoubleLinked(emp_4)

b = c.concat(b)

b.print()
print('~'*20)



#####################
## Тест count_average_salary
#####################
print('Тест add - добавление в конец')

a = DoubleLinked()
a.print()
a.count_average_salary()
print(a.average)

b = DoubleLinked(emp_1)
b.add(emp_1)
b.add(emp_2)
b.add(emp_3)
b.print()
b.count_average_salary()
print(b.average)


b.print()
print('~'*20)

#####################
## Тест count_average_salary
#####################
print('Тест add - добавление в конец')

a = DoubleLinked()
a.print()
a.count_average_salary()
print(a.average)

b = DoubleLinked(emp_1)
b.add(emp_1)
b.add(emp_2)
b.add(emp_3)
b.print()
b.count_average_salary()
print(b.average)


b.print()
print('~'*20)

#####################
## Тест quick_sort()
#####################
print('Тест add - добавление в конец')

a = DoubleLinked()
a.print()
a.quick_sort()
print(a.average)

b = DoubleLinked(emp_1)
b.add(emp_2)
b.add(emp_3)
b.add(emp_4)
b.add(emp_5)
b.add(emp_6)
b.add(emp_7)
b.add(emp_8)
b.add(emp_9)
b.add(emp_10)
b.add(emp_11)
b.add(emp_12)
b.add(emp_13)
b.add(emp_14)
b.add(emp_15)
b.print()

result_2 = b.quick_sort()
result_2.print()

print('~'*20)


#####################
## Тест Задание
#####################
print('Тест add - добавление в конец')

a = DoubleLinked()
a.print()
a.quick_sort()
print(a.average)

b = DoubleLinked(emp_1)
b.add(emp_2)
b.add(emp_3)
b.add(emp_4)
b.add(emp_5)
b.add(emp_6)
b.add(emp_7)
b.add(emp_8)
b.add(emp_9)
b.add(emp_10)
b.add(emp_11)
b.add(emp_12)
b.add(emp_13)
b.add(emp_14)
b.add(emp_15)
b.print()


result_2 = b.custom_action_salary()
result_2.print()

