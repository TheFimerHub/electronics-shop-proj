import pytest
from src.item import Item

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.price == 10000
    assert item2.price == 20000

    Item.pay_rate = 0.8

    item1.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 20000


def test_string_to_number():
    """
    Тест проверяет, что метод string_to_number корректно преобразует строку в число.
    """
    assert Item.string_to_number('10.5') == 10
    assert Item.string_to_number('20.7') == 20
    assert Item.string_to_number('5.0') == 5


def test_instantiate_from_csv():
    """
    Тест проверяет, что метод instantiate_from_csv корректно создает экземпляры товаров из CSV-файла.
    """
    Item.instantiate_from_csv("./src/items.csv")
    assert len(Item.all) == 5


def test_check_repr_and_str():
    """
    Тест проверяет, что магические методы __repr__ и __str__ корректно возвращает информацию.
    """
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == 'Item("Смартфон", 10000, 20)'
    assert str(item1) == 'Смартфон - 10000 - 20'




if __name__ == "__main__":
    pytest.main()
