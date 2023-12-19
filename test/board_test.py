import pytest
from board import GameBoard
from config import RCS


def test_stats():
    GameBoard.stats(30)
    assert RCS['mode'] == 3


def test_stats_wrong():
    with pytest.raises(ValueError):
        GameBoard.stats('30')
