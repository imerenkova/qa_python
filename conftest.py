import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    books_collector = BooksCollector()
    return books_collector
