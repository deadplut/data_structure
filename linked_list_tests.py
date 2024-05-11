from linked_list import Node, LinkedList

node_1 = Node('1')
node_2 = Node('2')
node_3 = Node('3')
node_4 = Node('4')
node_5 = Node('5')
node_6 = Node('6')

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6

empty_list = LinkedList()
test_list = LinkedList(node_1)

unsorted_node_1 = Node('3')
unsorted_node_2 = Node('2')
unsorted_node_3 = Node('5')
unsorted_node_4 = Node('1')
unsorted_node_5 = Node('6')
unsorted_node_6 = Node('4')

unsorted_node_1.next = unsorted_node_2
unsorted_node_2.next = unsorted_node_3
unsorted_node_3.next = unsorted_node_4
unsorted_node_4.next = unsorted_node_5
unsorted_node_5.next = unsorted_node_6

unsorted_list = LinkedList(unsorted_node_1)


###################
# Тест метода print_list()
###################

empty_list.print_list()
test_list.print_list()

print('\n')
print('~'*20)
###################
# Тест метода print_list_reversed()
###################
#
# empty_list.print_list_reversed()
# test_list.print_list_reversed()
#
# print('\n')
# print('~'*20)
###################
# Тест метода вставки в конец
###################
# node_7_empty = Node(7)
# node_7_test = Node(7)
#
# empty_list.insert_end(node_7_empty)
# empty_list.print_list()
#
# test_list.insert_end(node_7_test)
# test_list.print_list()
#
# print('\n')
# print('~'*20)
###################
# Тест метода вставки в начало
###################

# node_8_empty = Node(8)
# node_8_test = Node(8)
#
# empty_list.insert_start(node_8_empty)
# empty_list.print_list()
#
# test_list.insert_start(node_8_test)
# test_list.print_list()
#
# print('\n')
# print('~'*20)

###################
# Тест метода вставки на заданную позицию
###################

# node_8_empty = Node(88)
# node_8_test = Node(88)
#
# empty_list.insert(node_8_empty, 0)
# empty_list.print_list()
#
# test_list.insert(node_8_test, 5)
# test_list.print_list()
#
# print('\n')
# print('~'*20)

###################
# Тест метода find(cargo)
###################

# print(empty_list.find(3))
# print(test_list.find('3'))
# print(test_list.find('33'))
# print('\n')
# print('~'*20)
###################
# Тест метода contains(cargo)
###################

# print(empty_list.contains(2))
# print(test_list.contains('4'))
# print(test_list.contains('7'))
# print('\n')
# print('~'*20)

###################
# Тест метода append(cargo)
###################

# node_8_empty = Node(88)
# node_8_test = Node(88)
#
# empty_list.append(node_8_empty, 12)
# empty_list.print_list()
#
# test_list.append(node_8_test, '6')
# test_list.print_list()
#
# print('\n')
# print('~'*20)


###################
# Тест метода prepend(cargo)
###################

# node_8_empty = Node(88)
# node_8_test = Node(88)
#
# empty_list.prepend(node_8_empty, 12)
# empty_list.print_list()
#
# test_list.prepend(node_8_test, '3')
# test_list.print_list()

# print('\n')
# print('~'*20)


###################
# Тест удаление первого элемента
###################
#
# empty_list.del_first()
# empty_list.print_list()
#
# test_list.del_first()
# test_list.print_list()
#
# print('\n')
# print('~'*20)

###################
# Тест удаление последнего элемента
###################
#
# empty_list.del_last()
# empty_list.print_list()
#
# test_list.del_last()
# test_list.print_list()
#
# print('\n')
# print('~'*20)

###################
# Тест удаление с заданным номером/значением
###################

# empty_list.del_elem(cargo=0)
# empty_list.del_elem(position=0)
#
# empty_list.print_list()
#
# test_list.del_elem(cargo='1')
# test_list.print_list()
#
# print('\n')
# print('~'*20)

###################
# Тест упорядка списка
###################

empty_list.sort()
empty_list.print_list()

test_list.sort()
test_list.print_list()

unsorted_list.sort()
unsorted_list.print_list()



###################
# Тест проверка пустоты списка
###################


# print(empty_list.is_empty())
# print(test_list.is_empty())
#
# print('\n')
# print('~'*20)


###################
# Тест удаления списка
###################
#
# empty_list.order_66()
# test_list.order_66()
#
# print(empty_list.is_empty())
# print(test_list.is_empty())
#
#
# print('\n')
# print('~'*20)


###################
# Тест перестановки элемнтов
###################
# #
# empty_list.rearrangement(node_1, node_2)
# test_list.rearrangement(node_6, node_1)
#
# empty_list.print_list()
# test_list.print_list()
#
#
#
# print('\n')
# print('~'*20)
#
















'''
# def print_list_cycle(self):
#     """
#     Print каждого элемента списка, начиная с себя
#     при помощи цикла
#     """
#     node = self
#     while node.next:
#         print(node.value)
#         node = node.next
#     else:
#         print(node.value)
#
#
# def print_list_cycle_reversed(self):
#     """
#     Print каждого элемента списка, начиная с конца(reversed)
#     при помощи цикла
#     """
#     last = None
#     node = None
#     while node != self:
#         node = self
#         while node.next != last:
#             node = node.next
#         print(node.value)
#         last = node
#
# def print_list_recursion(self):
#     """
#     Print каждого элемента списка, начиная с конца при помощи рекурсии
#     """
#     print(self.value)
#     if self.next:
#         return self.next.print_list_recursion()
#
#
# def print_list_recursion_reverse(self):
#     """
#     Print каждого элемента списка, начиная с конца(reversed)
#     при помощи рекурси
#     """
#     if self.next:
#         self.next.print_list_recursion_reverse()
#         print(self.value)
#     else:
#         print(self.value)

#
#
# node_1 = LinkedList('1')
# node_2 = LinkedList('2')
# node_3 = LinkedList('3')
# node_4 = LinkedList('4')
# node_5 = LinkedList('5')
# node_6 = LinkedList('6')
#
# node_1.next = node_2
# node_2.next = node_3
# node_3.next = node_4
# node_4.next = node_5
# node_5.next = node_6
#
# # node_1.print_list_recursion()
# node_1.print_list_recursion_reverse()
# # print(node_1.value)
'''