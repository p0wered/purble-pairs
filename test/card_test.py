import pytest
from card import GameCard


def test_create():
    c = GameCard.create('blue')
    assert c == GameCard('blue')
    assert str(c) == 'card_blue'


def test_create_wrong_color():
    with pytest.raises(ValueError):
        c = GameCard.create('red')


def test_create_card_list():
    text = "blue yellow purple red"
    assert GameCard.card_list(text) == [GameCard("blue"), GameCard('yellow'), GameCard('purple'), GameCard('red')]
