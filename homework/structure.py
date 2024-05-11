from homework.data import Employee


def check_length(func):
    """
    Декоратор проверки длины структур данных.
    Если в структуре нет узлов, то вызываемый метод не вызывается.
    """
    def wrapper(self, *args, **kwargs):
        if self.head:
            return func(self, *args, **kwargs)
        print('Операция невозможна, так как список пустой')
    return wrapper


def custom_absolute(x):
    """
    Ф-ция, которая получает число по модулю
    :param x: число
    :return: abs(число)
    """
    if x < 0:
        x *= -1
    return x

class DoubleLinked:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 0
        self.sum = 0
        self.average = None
        if node:
            self.length = 1
            self.sum = node.salary
            self.tail.next = None

    def add(self, node: Employee) -> None:
        """
        Метод добавления элемента(node)
        :param node: элемент
        :return: None
        """
        if not self.head:
            self.__init__(node)
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.tail.next = None
            self.length += 1
            self.sum += node.salary

    def concat(self, append_list):
        """
        Метод объединения структур
        :param append_list: DoubleLinked
        :return: объединенный список
        """
        if self.length == 0:
            return append_list
        if append_list.length == 0:
            return self

        self.tail.next = append_list.head
        append_list.head.prev = self.tail
        self.tail = append_list.tail
        append_list.head = None
        self.length += append_list.length

        return self

    def print(self):
        """
        Метод вывода в консоль всех элементов через запятую
        :return: None
        """
        result = f''
        node = self.head
        while node:
            result += f'{node}, '
            if node == self.tail:
                break
            node = node.next
        print(result[:-2])

    @check_length
    def count_average_salary(self):
        """
        Метод обновляет average
        :return:
        """
        self.average = self.sum / self.length
        return self.average

    def quick_sort(self):
        """
        Метод быстрой сортировки c рекурсией
        :return: отсортрованный массив
        """
        if self.length <= 1:
            return self

        first_list = DoubleLinked()
        second_list = DoubleLinked()
        third_list = DoubleLinked()

        avg = self.count_average_salary()

        node = self.head
        while True:
            next_node = node.next

            if node.salary < avg:
                third_list.add(node)
            elif node.salary > avg:
                first_list.add(node)
            else:
                second_list.add(node)

            if node == self.tail:
                break

            node = next_node

        return first_list.quick_sort().concat(second_list).concat(third_list.quick_sort())

    @check_length
    def custom_action_salary(self):
        """
        Метод упорядочивания в порядке убывания отклонения оклада от среднего.

        :return: отсортированный массив по условию
        """

        sorted_list = self.quick_sort()
        avg = self.count_average_salary()

        left_node = sorted_list.head
        right_node = sorted_list.tail
        new_list = DoubleLinked()
        while left_node != right_node:

            if custom_absolute(avg - left_node.salary) > custom_absolute(avg - right_node.salary):
                node_next = left_node.next
                new_list.add(left_node)
                left_node = node_next

            elif custom_absolute(avg - left_node.salary) < custom_absolute(avg - right_node.salary):
                node_prev = right_node.prev
                new_list.add(right_node)
                right_node = node_prev
            else:
                node_next = left_node.next
                node_prev = right_node.prev
                new_list.add(left_node)
                new_list.add(right_node)

                left_node = node_next
                if left_node == right_node:
                    break
                right_node = node_prev

        else:
            new_list.add(left_node)
            left_node.next = None

        return new_list



