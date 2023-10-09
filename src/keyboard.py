from src.item import Item


class Mixin:
    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"

        elif self.language == "RU":
            self.language = "EN"


class Keyboard(Item, Mixin):
    def __init__(self, name: str, price: float, quantity: int):
        """
        :param name: Название товара.
        :param language: Выйбор языка.
        """
        super().__init__(name, price, quantity)
        self.__language = 'EN'
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new):
        self.name = new

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, lang):
        if lang not in ['EN', 'RU']:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        self.__language = lang

    def __str__(self):
        return f"{self.name}"
