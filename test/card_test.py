import pytest
from card import GameCard


def test_create():
    c = GameCard.create('ct1')
    assert c == GameCard('ct1')
    assert str(c) == 'card_ct1'


def test_create_wrong():
    with pytest.raises(ValueError):
        c = GameCard
        c.create('ct3')


def test_create_card_list():
    text = "ct1 ct2 eo1 eo2"
    assert GameCard.card_list(text) == [GameCard("ct1"), GameCard('ct2'), GameCard('eo1'), GameCard('eo2')]
