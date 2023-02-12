import pytest

from main import BooksCollector


@pytest.fixture(scope='function')
def collector():
    books_collector = BooksCollector()
    return books_collector
