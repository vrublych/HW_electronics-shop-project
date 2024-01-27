from src.keyboard import Keyboard


def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"


def test_keyboard():
    kb = Keyboard(name="Dark Project KD87A", price=9600.0, quantity=5)
    assert str(kb) == "Dark Project KD87A"
    assert kb.price == 9600.0
    assert kb.quantity == 5
    assert kb.language == "EN"
