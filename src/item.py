import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    # Ставка оплаты по умолчанию
    pay_rate = 1.0
    # Список всех товаров
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.name} - {self.price} - {self.quantity}'

    def __add__(self, other):
        if isinstance(other, Item):
            total_quantity = self.quantity + other.quantity
            return total_quantity
        else:
            raise TypeError("Нельзя сложить Item с объектом другого класса")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate  # Умножение на ставку скидки

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        if len(name) > 10:
            name = name[:10]
        self._name = name

    @classmethod
    def instantiate_from_csv(cls, path: str) -> None:
        """
        Создает экземпляры товаров из CSV-файла и добавляет их в список.

        :param path: Путь к CSV-файлу.
        """
        # Очищаем список all перед инициализацией из csv файла
        cls.all.clear()

        with open(path, newline='', encoding='cp1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(txt: str) -> int:
        """
        Преобразует строку в число, отбрасывая десятичную часть.

        :param txt: Входная строка для преобразования.
        :return: Целочисленное значение.
        """
        return int(float(txt))
