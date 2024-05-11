class Employee:
    """
    Сотрудник с полями: фамилия, инициалы, зарплата, премия

    Также содержит служебные поля: next, prev
    """
    def __init__(self, surname, initials, salary, bonus):
        self.surname = surname
        self.initials = initials
        self.salary = salary
        self.bonus = bonus

        self.prev = None
        self.next = None

    def __str__(self):
        return f'{self.surname}'
