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

def test_all_items():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1 in Item.all
    assert item2 in Item.all

if __name__ == "__main__":
    pytest.main()