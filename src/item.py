import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Item.

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
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        if len(name) > 10:
            name = name[:10]
        self._name = name

    @classmethod
    def instantiate_from_csv(cls, path) -> None:
        """
        Создает экземпляры товаров из CSV-файла и добавляет их в список.

        Args:
            path (str): Путь к CSV-файлу.
        """
        # Очищаем список all перед инициализацией из csv файла
        cls.all.clear()

        with open(path, newline='', encoding='cp1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(txt) -> int:
        return int(float(txt))
