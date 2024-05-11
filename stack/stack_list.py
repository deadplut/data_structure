from linked_list import LinkedList


class Node:
    def __init__(self, cargo=None, next_elem=None, prev_elem=None):
        self.cargo = cargo
        self.next = next_elem
        self.prev = prev_elem

    def __str__(self):
        return str(self.cargo)


class StackList(LinkedList):
    def push(self, node):
        self.insert_start(node)

    def pop(self):
        self.del_first()
