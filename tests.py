import pytest as pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    # test №1
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # test №2
    def test_add_new_book_add_book_have_rating1(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Зелёная миля')

        # проверяем, что у добавленной книги по умолчанию рейтинг 1
        assert collector.get_book_rating('Зелёная миля') == 1

    # test №3
    def test_add_new_book_add_book_twice_save_one(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # добавляем одну книгу 2 раза
        book_name = 'О дивный новый мир'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)

        # проверяем, что добавилась одна
        assert len(collector.get_books_rating()) == 1

    # test №4
    @pytest.mark.parametrize('book_name, rating',
                             [
                                 ['Гарри Поттер и философский камень', 1],
                                 ['Гарри Поттер и тайная комната', 5],
                                 ['Гарри Поттер и кубок огня', 10]
                             ])
    def test_set_book_rating_add_book_with_rating(self, book_name, rating):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, rating)

        assert collector.get_book_rating(book_name) == rating

    # test №5
    @pytest.mark.parametrize('rating', [-1, 0, 11, '', None, 'интересная книга'])
    def test_set_book_rating_add_book_with_rating_negative_input(self, rating):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        book_name = 'Семь смертей Эвелины Хардкасл'
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, rating)

        assert collector.get_book_rating(book_name) == 1

    # test №6
    def test_set_book_rating_add_one_book_set_rating_another(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        collector.add_new_book('Голова профессора Доуэля')
        collector.set_book_rating('Великий Гэтсби', 6)

        assert collector.get_book_rating('Великий Гэтсби') is None

    # test №7
    def test_get_books_rating(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        book_name = 'Над пропастью во ржи'
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, 7)

        assert type(collector.get_books_rating()) is dict

    # test №8
    @pytest.mark.parametrize('rating', [-1, 0, 1, 10, 11, '', None, 'интересная книга'])
    def test_get_books_with_specific_rating_empty_collector_empty(self, rating):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        assert collector.get_books_with_specific_rating(rating) == []

    # test №9
    # def test_get_books_with_specific_rating_add7_books_with_rating9(self, rating=9):
    #     # создаем экземпляр класса BooksCollector
    #     collector = BooksCollector()
    #     books = [
    #         'Атлант расправил плечи',
    #         'Мастер и Маргарита',
    #         'Незнайка на Луне',
    #         'Автостопом по Галактике',
    #         'Безумная звезда',
    #         'Нездешние',
    #         'Мятная сказка']
    #     for i in range(len(books)):
    #         collector.add_new_book(books[i])
    #         collector.set_book_rating(books[i], rating)
    #
    #     assert len(collector.get_books_with_specific_rating(rating)) == 7

    def test_get_books_with_specific_rating_add7_books_with_rating_get4(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()
        books = {'Атлант расправил плечи': 7,
                 'Мастер и Маргарита': 10,
                 'Незнайка на Луне': 9,
                 'Автостопом по Галактике': 7,
                 'Безумная звезда': 7,
                 'Нездешние': 7,
                 'Мятная сказка': 6}

        for key, value in books.items():
            collector.add_new_book(key)
            collector.set_book_rating(key, value)

        assert len(collector.get_books_with_specific_rating(7)) == 4

    # test №10
    def test_get_books_with_specific_rating_book_with_rating1_not_exist(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        collector.add_new_book('Обломов')
        collector.set_book_rating('Обломов', 7)

        assert collector.get_books_with_specific_rating(1) == []
