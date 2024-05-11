from cycled_list.cycle import CycledList, Node


node_1a = Node(1)
node_1b = Node(1)
node_2b = Node(2)
node_3b = Node(3)
node_4b = Node(4)







#####################
## Тест __init__
#####################
print('Тест __init__')

a = CycledList()
b = CycledList(node_1b)
# b.add(node_1a)

a.print()
b.print()

print('~'*20)

#####################
## Тест add - добавление в конец
#####################
print('Тест add - добавление в конец')

a = CycledList()
a.add(node_1a)
a.print()

b = CycledList(node_1b)
b.add(node_2b)
b.add(node_3b)
b.add(node_4b)
b.print()


print('~'*20)

#####################
## Тест pop - удаления из конца
#####################
print('Тест add - добавление в конец')

c = CycledList()
c.pop()
c.print()

d = CycledList(node_1b)
d.add(node_2b)
d.add(node_3b)
d.add(node_4b)
d.pop()
d.pop()
d.print()

print('~'*20)


#####################
## Тест find - нахождения позиции по значению
#####################
print('Тест find - нахождения позиции по значению')

c = CycledList()
c.find_position(1)
c.print()

d = CycledList(node_1b)
d.add(node_2b)
d.add(node_3b)
d.add(node_4b)

d.find_position(3)
d.find_position(1)
d.find_position(13)

d.print()

print('~'*20)


#####################
## Тест find_by_position - нахождения позиции по значению
#####################
print('Тест find_by_position - нахождения позиции по значению')

c = CycledList()
c.find_by_position(0)
c.print()

d = CycledList(node_1b)
d.add(node_2b)
d.add(node_3b)
d.add(node_4b)

print(f'Node со значением {d.find_by_position(3)}')
print(f'Node со значением {d.find_by_position(1)}')

d.find_by_position(31)
d.print()

print('~'*20)


#####################
## Тест delete по позиции
#####################
print('Тест delete по позиции')

c = CycledList()
c.delete(0)
c.print()

d = CycledList(node_1b)
d.add(node_2b)
d.add(node_3b)
d.add(node_4b)

d.delete(2)
d.delete(31)
d.print()

d.delete(2)
d.delete(0)
print(d.tail)
print(d.head)
print('~'*20)

#####################
## Тест delete по позиции
#####################
print('Тест delete по позиции')

c = CycledList()
c.delete(0)
c.print()

d = CycledList(node_1b)
d.add(node_2b)
d.add(node_3b)
d.add(node_4b)

d.delete(2)
d.delete(31)
d.print()

d.delete(2)
d.delete(0)
print(d.tail)
print(d.head)


print('~'*20)


#####################
## Тест insert по позиции
#####################
print('Тест insert по позиции')

insert_node = Node(123)
insert_node_1 = Node(1231)
insert_node_2 = Node(1232)
insert_node_3 = Node(1233)
insert_node_4 = Node(1234)

c = CycledList()
c.insert(insert_node, 1)
c.print()

d = CycledList(node_1b)
d.add(node_2b)
d.add(node_3b)
d.add(node_4b)

d.insert(insert_node_1, 3)
d.insert(insert_node_2, 0)
d.insert(insert_node_3, 123123)
d.insert(insert_node_4, 2)

d.print()

print(d.tail)
print(d.head)


print('~'*20)
