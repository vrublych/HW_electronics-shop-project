"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

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
