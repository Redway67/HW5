import os
from victory import birthday_month_year
from main import author, show_files


def test_birthday_month_year():
    assert birthday_month_year(6, 6, 1799) == 'шестого июня 1799 года'
    assert birthday_month_year(7, 11, 2019) == 'седьмого ноября 2019 года'


def test_author():
    assert author() == 'Пушкин Александр Сергеевич  (c)'


def test_show_files():
    if os.listdir():
        assert len(show_files()) != 0
