import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def sample_items():
    phone1 = Phone("iPhone 15 PRO MAX", 234_990, 20_000, 2)
    phone2 = Phone("Samsung Galaxy S23 Ultra", 108_999, 5_000, 2)
    item1 = Item("Ноутбук", 10_000, 10_000)
    return phone1, phone2, item1


@pytest.mark.magic_methods
def test_magic_methods(sample_items):
    """
    Тест проверяет магические методы класса Phone (__str__, __repr__) и оператор сложения (+).

    Создаем экземпляр класса Phone с заданными характеристиками и экземпляр класса Item.
    Проверяем, что метод __str__ правильно возвращает имя телефона.
    Проверяем, что метод __repr__ правильно представляет объект Phone в виде строки.
    Проверяем, что оператор + правильно складывает количество физических SIM-карт.
    Проверяем, что оператор + правильно складывает количество физических SIM-карт в телефонах.
    """
    phone1, phone2, item1 = sample_items

    assert str(phone1) == "iPhone 15 PRO MAX"
    assert repr(phone1) == "Phone('iPhone 15 PRO MAX', 234990, 20000, 2)"

    # Проверяем add
    assert item1 + phone1 == 30_000
    assert phone1 + phone2 == 25_000


@pytest.mark.errors
def test_invalid_number_of_sim(sample_items):
    """
    Тест проверяет обработку исключения при некорректном значении количества физических SIM-карт.

    Создаем экземпляр класса Phone с некорректным значением количества физических SIM-карт.
    Проверяем, что при попытке установить количество физических SIM-карт равным нулю, возникает исключение ValueError.
    Проверяем, что сообщение об ошибке соответствует ожидаемому сообщению.
    """
    phone1 = Phone("iPhone 15 PRO", 220_000, 5, 2)

    with pytest.raises(ValueError) as exc_info:
        phone1.number_of_sim = 0

    assert str(exc_info.value) == "Количество физических SIM-карт должно быть целым числом больше нуля"


if __name__ == "__main__":
    pytest.main()
