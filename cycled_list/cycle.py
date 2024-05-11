from linked_list import LinkedList


def check_length(func):
    def wrapper(self, *args, **kwargs):
        if self.head:
            return func(self, *args, **kwargs)
        print('Операция невозможна, так как список пустой')
    return wrapper


class Node:
    def __init__(self, cargo=None, next_elem=None):
        self.cargo = cargo
        self.next = next_elem

    def __str__(self):
        return str(self.cargo)


class CycledList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.length = 0
        if head:
            self.tail = head
            self.tail.next = head
            self.length += 1

    def add(self, node):
        if not self.head:
            self.__init__(node)
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head
            self.length += 1

    @check_length
    def pop(self):
        prev_node = self.__find_prev_node(self.tail)
        if prev_node:
            self.tail = prev_node
            prev_node.next = self.head
        else:
            self.head, self.tail = None, None

        self.length += -1

    def insert(self, new_node, position):
        old_node = self.find_by_position(position)
        if not old_node:
            return
        prev_node = self.__find_prev_node(old_node)
        prev_node.next = new_node
        new_node.next = old_node.next

        if position == 0:
            self.head = new_node
        if position == self.length - 1:
            self.tail = new_node

    @check_length
    def delete(self, position):
        node = self.find_by_position(position)
        if not node:
            return
        prev_node = self.__find_prev_node(node)
        prev_node.next = node.next
        if position == 0:
            self.head = node.next
        if position == self.length - 1:
            self.tail = prev_node

        self.length += -1

    @check_length
    def find_position(self, value):
        node = self.head
        position = 0
        while self.length > position:
            if node.cargo == value:
                print(f'Позиция: {position}')
                return position
            position += 1
            node = node.next
        print('Такого значения нет')
        return None

    @check_length
    def find_by_position(self, position):
        if position >= self.length:
            print('Out of range')
            return
        node = self.head
        count = 0
        while count < position:
            node = node.next
            count += 1
        return node

    @check_length
    def __find_prev_node(self, node):
        #todo check if node in

        if node == self.head:
            return self.tail
        prev_node = self.head
        while prev_node.next != node:
            prev_node = prev_node.next
        return prev_node

    def rearrangement(self, node_1, node_2):
        pass

    def sort(self, reverse=False):
        pass

    def print(self):
        result = f''
        node = self.head
        while node:

            result += f'{node}, '
            if node == self.tail:
                break
            node = node.next
        print(result[:-2])


