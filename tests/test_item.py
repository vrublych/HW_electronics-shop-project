"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item, InstantiateCSVError
from src.phone import Phone
import pytest
from unittest.mock import patch


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000
    item2 = Item("Ноутбук", 20000, 5)
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item1.pay_rate = 0.9  # скидка 10%
    item1.apply_discount()
    assert item1.price == 10000 * 0.9
    item2 = Item("Ноутбук", 20000, 5)
    item2.pay_rate = 0.8  # скидка 20%
    item2.apply_discount()
    assert item2.price == 20000 * 0.8


def test_instantiate_from_csv():
    Item.instantiate_from_csv('D:\\PROJECTS\\HW_electronics-shop-project\\src\\items.csv')
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'



def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == "Смартфон"


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert phone1 + phone1 == 10
    assert item1 + phone1 == 25


def test_instantiate_from_csv_file_not_found():
    with patch('builtins.open', side_effect=FileNotFoundError("File not found")):
        with pytest.raises(FileNotFoundError):
            Item.instantiate_from_csv()

def test_instantiate_from_csv_key_error():
    with patch('builtins.open', side_effect=KeyError("Key not found")):
        with pytest.raises(InstantiateCSVError, match="Файл item.csv поврежден"):
            Item.instantiate_from_csv()
