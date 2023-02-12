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
    def test_add_new_book_add_book_default_rating1(self):
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
    def test_set_book_rating_set_rating_for_book_not_from_collector(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        # collector.add_new_book('Голова профессора Доуэля')
        collector.set_book_rating('Великий Гэтсби', 6)

        assert collector.get_book_rating('Великий Гэтсби') is None

    # test №7
    def test_get_books_rating_rating_store_in_dict(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        book_name = 'Над пропастью во ржи'
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, 7)

        assert type(collector.get_books_rating()) is dict

    # test №8
    @pytest.mark.parametrize('rating', [-1, 0, 1, 10, 11, '', None, 'интересная книга'])
    def test_get_books_with_specific_rating_empty_collector_is_empty(self, rating):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        assert collector.get_books_with_specific_rating(rating) == []

    # test №9
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

        for book, rating in books.items():
            collector.add_new_book(book)
            collector.set_book_rating(book, rating)

        assert len(collector.get_books_with_specific_rating(7)) == 4

    # test №10
    def test_get_books_with_specific_rating_book_with_rating1_not_exist(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        collector.add_new_book('Обломов')
        collector.set_book_rating('Обломов', 7)

        assert collector.get_books_with_specific_rating(1) == []

    # test №11
    def test_add_book_in_favorites_add_two_books(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        collector.add_new_book('Девушка с татуировкой дракона')
        collector.set_book_rating('Девушка с татуировкой дракона', 7)
        collector.add_book_in_favorites('Девушка с татуировкой дракона')

        collector.add_new_book('Девушка, которая играла с огнем')
        collector.add_book_in_favorites('Девушка, которая играла с огнем')

        assert len(collector.get_list_of_favorites_books()) == 2

    # test №12
    def test_add_book_in_favorites_add_books_in_favourites_twice(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        book_name = 'Властелин колец: Братство кольца'
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, 10)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)

        assert len(collector.get_list_of_favorites_books()) == 1

    # test №13
    def test_add_book_in_favorites_book_no_in_collector(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        collector.add_book_in_favorites('Властелин колец: Две крепости')

        assert collector.get_list_of_favorites_books() == []

    # test №14
    def test_delete_book_from_favorites_delete_from_favourites_after_add(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        book_name = 'Хоббит, или Туда и обратно'
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, 10)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)

        assert collector.get_list_of_favorites_books() == []

    # test №15
    def test_delete_book_from_favorites_add_three_delete_two(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        books = ['Код да Винчи',
                 '451 градус по Фарингейту',
                 'Вино из одуванчиков']

        for i in range(len(books)):
            collector.add_new_book(books[i])
            collector.set_book_rating(books[i], 10 - i)
            collector.add_book_in_favorites(books[i])

        collector.delete_book_from_favorites(books[1])
        collector.delete_book_from_favorites(books[2])

        assert len(collector.get_list_of_favorites_books()) == 1

    # test №16
    def test_delete_book_from_favorites_no_one_book_in_favourites(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        books = ['Преступление и наказание',
                 'Евгений Онегин',
                 'Капитанская дочка']

        for i in range(len(books)):
            collector.add_new_book(books[i])
            collector.set_book_rating(books[i], 10 - i * 2)

        assert collector.delete_book_from_favorites(books[0]) is None

    # test №17
    def test_delete_book_from_favorites_book_does_not_exist_in_favorites(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        book = 'Собачье сердце'
        collector.add_new_book(book)
        collector.set_book_rating(book, 9)
        collector.add_book_in_favorites(book)

        assert collector.delete_book_from_favorites('Война и мир') is None \
               and len(collector.get_list_of_favorites_books()) == 1

    # test #18
    def test_get_list_of_favorites_books_favourites_books_store_in_list(self):
        # создаем экземпляр класса BooksCollector
        collector = BooksCollector()

        book_name = 'Цветы для Элджернона'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert type(collector.get_list_of_favorites_books()) is list
