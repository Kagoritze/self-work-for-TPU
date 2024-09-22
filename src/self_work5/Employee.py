'''
Реализовать базовый класс Employee, в котором определить атрибуты: name, patronymic, surname, salary. 
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: жалование и бонус, например, {"wage": wage, "bonus": bonus}. 
Создать класс Salary на базе класса Employee. 
В классе Salary реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
Создать экземпляры класса Salary, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''


class Employee:

    def __init__(self, name, surname, patronymic, wage, bonus):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self._salary = {"wage": wage, "bonus": bonus}


class Salary(Employee):

    def get_full_name(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    def get_total_income(self):
        return self._salary["wage"] + self._salary["bonus"]


s = Salary("Иванов", "Иван", "Иванович", 50000, 10000)
print(s.get_full_name())
print(f"Общий доход: {s.get_total_income()}")
