from src.exceptions import InstantiateCSVError
from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    try:
        Item.instantiate_from_csv()
    except FileNotFoundError:
        print(True)
    # FileNotFoundError: Отсутствует файл csv

    # В файле test_item.csv удалена последняя колонка.
    try:
        Item.instantiate_from_csv('../src/test_items.csv')
    except InstantiateCSVError:
        print(True)
    # InstantiateCSVError: Файл csv поврежден
