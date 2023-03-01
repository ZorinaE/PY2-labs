import doctest
from typing import Union

class House:
    def __init__(self, number_of_floors: int, number_of_rooms: int, floor_area: Union[int, float] ):
        """
        Создание и подготовка к работе объекта Дом

        :param number_of_floors: Этажность
        :param number_of_rooms: Кол-во комнат на этаже
        :param floor_area : Площадь этажа

        Примеры:
        >>> house = House(3, 10, 150)  # Инициализации экземлпяра класса
        """
        if not isinstance(number_of_floors, int):
            raise TypeError ("Кол-во этажей  должно быть типа int ")
        if number_of_floors <=0:
            raise ValueError ("Кол-во этажей  должно быть больше 0 ")
        self.number_of_floors = number_of_floors

        if not isinstance(number_of_rooms, int):
            raise TypeError ("Кол-во комнат  должно быть типа int ")
        if number_of_rooms <=0:
            raise ValueError ("Кол-во комнат  должно быть больше 0 ")
        self.number_of_rooms = number_of_rooms

        if not isinstance(floor_area, (int, float)):
            raise TypeError ("Площадь этажа должна быть типа int или float ")
        if floor_area <=0:
            raise ValueError ("Площадь этажа должна быть больше 0 ")
        self.number_of_rooms = number_of_rooms

    def change_in_number_of_storeys(self, change_number_of_floors: int) -> None:
        """
        Изменение этажности дома.

        :param change_number_of_floors: Число на которое нужно изменить кол-во этажей
        :raise ValueError: Если уменьшение этажей на значение большее, чем есть сейчас или равно ему

        Примеры:
        >>> house = House(3, 5, 150)
        >>> house.change_in_number_of_storeys(-2)
        # Инициализации экземлпяра класса
        """
        if (change_in_number_of_floors < 0) and (number_of_floors + change_number_of_floors == 0):
            raise ValueError ("Кол-во этажей в доме меньше, чем число на которое их  пытаются уменьшить")
        ...

    def number_of_toilets(self) -> int:
        """"
        Расчет кол-ва санузлов в зависимости от кол-ва комнат и этажности дома.

        :return Кол-во санузлов.

        Примеры:
        >>> house = House(3, 5, 150)
        >>> house.number_of_toilets()
        """
        ...

    def sum_of_rooms(self) -> int:
        """
        Определние суммарного кол-ва комнат в доме.

        :return: Кол-во комнат во всем доме.

        Примеры:
        >>> house = House(3, 5, 150)
        >>> house.sum_of_rooms()
        """


class Tinder_accaunt:
    def __init__(self, user_name: str, age: int, password: str ):
        """"
        Создание и подготовка к работе профиля в тиндер

        :param user_name  Имя пользовател
        :param age Возраст пользователя
        :param password  Пароль пользователя

        Пример:
        >>> user1 = Tinder_accaunt("Katrin", 21, "downtown12")
        """
        self.user_name = user_name

        if isinstance(age, int):
            raise TypeError ("Возраст должен быть значением типа int")
        if age < 18:
            raise ValueError ("Данное приложение доступно только для лиц старше 18 лет")
        self.age = age

        if len(password) < 8:
            raise ValueError ("Слишком короткий пароль")
        if len(password) > 20:
            raise ValueError (" Слишком длинный пароль")
        self.password = password

    def change_password(self, new_password : str) -> None:
        """
        Изменение парооля 
    
        :param new_password: Новый пароль 
    
        :raise ValueError: Если слишком короткий пароль 

        Примеры:
        >>> user1 = Tinder_accaunt("Katrin", 21, "downtown12")
        >>> user1.change_password("Dreamlife12")
        """

        if len(password) < 8:
            raise ValueError("Слишком короткий пароль")
        if len(password) > 20:
            raise ValueError(" Слишком длинный пароль")
        ...

    def change_user_name(self, new_user_name : str) -> None:
        """
        Изменение имени пользователя.

        :param new_user_name: Новое имя пользователя

        Примеры:
        >>> user1 = Tinder_accaunt("Katrin", 21, "downtown12")
        >>> user1.change_user_name("Ekaterina")
        """
        ...

class Refrigerator:
    def __init__(self, freezer: str, number_of_shelves: int, door_opening: str ):
        """
        Создание и подготовка к работе холодильника.

        :param freezer  наличие морозильной камеры
        :param number_of_shelves кол-во полок в холодильнике
        :param door_opening открывание двери

        Пример:
        >>> refrigerator = Refrigerator("Lg", 8, "left")
        """
        self.freezer = freezer

        if not isinstance(number_of_shelves, int):
            raise TypeError ("Кол-во полок должно быть значением типа int")
        if number_of_shelves<0:
            raise ValueError ("Некорректное значение кол-ва полок, введите положительное число")
        self.number_of_shelves = number_of_shelves


        if not (door_opening == "Left")or(door_opening == "Right"):
            raise ValueError ("Некорректное значение, допустим только вариант Left или Right")
        self.door_opening = door_opening

    def change_number_of_shelves(self,  new_number_of_shelves: int) -> None:
        """

        :param new_number_of_shelves: Новое кол-во полок в холодильнике
        :raise ValueError: Если число отрицательное, то возвращается ошибка.

        Примеры:
        >>> refrigerator = Refrigerator("Lg", 8, "left")
        >>> refrigerator.change_number_of_shelves(5)
        """
        ...
    def change_configuration(self) ->None:
        """
        Изменение конфигурации холодильника. Смена направления открывания двери

        Примеры:
        >>> refrigerator = Refrigerator("Lg", 8, "left")
        >>> refrigerator.change_configuration()
        """
        ...

if __name__ == "__main__":
    doctest.testmod() "Тестирование примеров из документации"
    pass