class Node:
    def __init__(self, cargo=None, next_elem=None):
        self.cargo = cargo
        self.next = next_elem

    def __str__(self):
        return str(self.cargo)


class LinkedList:
    def __init__(self, head=None):
        self.length = 0
        self.head = head
        self.last = None
        self.__setup()

    def __setup(self):
        """
        Метод присваивает переменным length и last значения
        """
        node = self.head
        while node:
            self.length += 1
            self.last = node
            node = node.next

    def print_list(self):
        result = []
        node = self.head
        while node:
            result += [node.cargo]
            node = node.next
        print(result)

    def print_list_reversed(self):
        """
        Print каждого элемента списка, начиная с конца(reversed)
        при помощи цикла
        """
        result = []
        last = None
        node = None
        while node != self.head:
            node = self.head
            while node.next != last:
                node = node.next
            result += [node.cargo]
            last = node
        print(result)

    def insert_start(self, node: Node):
        if self.head:
            node.next = self.head
            self.head = node
            self.length += 1
        else:
            self.head = node
            self.__setup()

    def insert_end(self, node: Node):
        if self.head:
            self.last.next = node
            self.last = node
            self.length += 1
        else:
            self.head = node
            self.__setup()

    def insert(self, node: Node, position: int):
        if position >= self.length or position < 0:
            print('Нет такой позиции в списке')
            return

        if position == 0:
            node.next = self.head.next
            self.head = node
        else:
            pre_node = self.head
            node_position = 1
            while node_position != position:
                pre_node = pre_node.next
                node_position += 1
            node.next = pre_node.next.next
            pre_node.next = node

        if position == self.length - 1:
            self.last = node



    def find(self, cargo):
        node = self.head
        while node:
            if node.cargo == cargo:
                return node
            node = node.next
        else:
            return None

    def contains(self, cargo):
        node = self.head
        while node:
            if node.cargo == cargo:
                return True
            node = node.next
        else:
            return False

    def append(self, node, cargo):
        pre_node = self.find(cargo)

        if not pre_node:
            print(f'node с cargo={cargo} не существует')
            return

        node.next = pre_node.next
        pre_node.next = node

    def prepend(self, node, cargo):
        after_node = self.find(cargo)
        if not after_node:
            print(f'node с cargo={cargo} не существует')
            return

        if self.head == after_node:
            node.next = after_node
            self.head = node

        pre_node = self.head
        while pre_node.next != after_node:
            pre_node = pre_node.next

        pre_node.next = node
        node.next = after_node

    def del_first(self):
        if not self.head:
            print('В списке нет узлов')
            return
        first_node = self.head
        self.head = first_node.next
        first_node.next = None

    def del_last(self):
        if not self.head:
            print('В списке нет узлов')
            return

        node = self.head
        while node.next != self.last:
            node = node.next

        self.last = node
        node.next = None

    def del_elem(self, position=None, cargo=None):
        if not self.head:
            print('В списке нет узлов')
            return

        pre_node = self.head
        node = None
        if cargo:
            node = self.find(cargo)
            if not node:
                print('Необходимо задать корректный position или корректный cargo')
                return
            while pre_node.next != node and node != self.head :
                pre_node = pre_node.next
        elif position == 0 and position < self.length:
            node = self.head

        elif position and position < self.length:
            count = 0
            while (count + 1) < position:
                pre_node = pre_node.next
                count += 1
            node = pre_node.next

        else:
            return

        if node == self.head:
            self.head = node.next
            node.next = None
            return

        pre_node.next = node.next
        node.next = None

    def is_empty(self):
        return not self.head

    def order_66(self):
        node, self.head = self.head, None
        while node:
            node.next, node = None, node.next

    def find_pre_node(self, node):

        pre_node = self.head

        while pre_node and pre_node.next != node:
            pre_node = pre_node.next
        return pre_node

    def rearrangement(self, node_first, node_second):
        if not self.head:
            print('Список пустой')
            return

        pre_node_first = self.find_pre_node(node_first)
        pre_node_second = self.find_pre_node(node_second)

        if self.head == node_first:
            self.head = node_second
            pre_node_second.next = node_first
        elif self.head == node_second:
            self.head = node_first
            pre_node_first.next = node_second
        else:
            pre_node_first.next, pre_node_second.next = node_second, node_first


        node_first.next, node_second.next = node_second.next, node_first.next


    def sort(self):
        if not self.head:
            return

        condition = True

        while condition:
            node = self.head
            condition = False
            while node.next:

                if node.cargo > node.next.cargo:
                    self.rearrangement(node, node.next)
                    condition = True
                    break
                node = node.next








