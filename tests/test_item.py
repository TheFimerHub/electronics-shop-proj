import pytest
from src.item import Item
from src.exceptions import InstantiateCSVError


@pytest.fixture
def sample_items():
    item1 = Item("Смартфон", 10_000, 20)
    item2 = Item("Ноутбук", 20_000, 5)
    return item1, item2


@pytest.mark.calculation
def test_calculate_total_price(sample_items):
    """
    Тест проверяет, что метод calculate_total_price
    корректно вычисляет общую стоимость товара.
    """
    item1, item2 = sample_items

    # Проверяем
    assert item1.calculate_total_price() == 20_0000
    assert item2.calculate_total_price() == 10_0000


@pytest.mark.calculation
def test_apply_discount(sample_items):
    """
    Тест проверяет, что метод apply_discount
    корректно применяет скидку к цене товара.
    """
    item1, item2 = sample_items

    # Проверяем
    assert item1.price == 10_000
    assert item2.price == 20_000

    # Изменяем коэффициент
    Item.pay_rate = 0.8

    # Применяем скидку
    item1.apply_discount()

    # Проверяем
    assert item1.price == 8_000
    assert item2.price == 20_000


@pytest.mark.calculation
def test_string_to_number():
    """
    Тест проверяет, что метод string_to_number
    корректно преобразует строку в число.
    """
    assert Item.string_to_number('10.5') == 10
    assert Item.string_to_number('20.7') == 20
    assert Item.string_to_number('5.0') == 5


@pytest.mark.calculation
def test_instantiate_from_csv():
    """
    Тест проверяет, что метод instantiate_from_csv корректно создает экземпляры товаров из CSV-файла.
    """
    Item.instantiate_from_csv("./src/items.csv")
    assert len(Item.all) == 5

    with pytest.raises(FileNotFoundError) as exc_info:
        Item.instantiate_from_csv()

    assert str(exc_info.value) == "Отсутствует файл csv"

    with pytest.raises(InstantiateCSVError) as exc_info:
        Item.instantiate_from_csv('./src/test_items.csv')

    assert str(exc_info.value) == 'Файл CSV поврежден'




@pytest.mark.magic_methods
def test_magic_methods(sample_items):
    """
    Тест проверяет, что магические методы __repr__, __str__ и __add__ корректно возвращают информацию.
    """
    item1, item2 = sample_items

    assert repr(item1) == 'Item("Смартфон", 10000, 20)'
    assert str(item1) == 'Смартфон - 10000 - 20'
    assert item1 + item2 == 25


if __name__ == "__main__":
    pytest.main()
