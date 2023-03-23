import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
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

    def test_get_book_rating_get_rating_5(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 7)

        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 5

    def test_get_book_rating_try_set_rating_11_get_rating_1(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_rating('Гордость и предубеждение и зомби', 11)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 7)

        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_get_books_with_specific_rating_books_with_rating_5(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.set_book_rating('Гордость и предубеждение и зомби', 5)

        assert collector.get_books_with_specific_rating(5) == ['Гордость и предубеждение и зомби']

    def test_add_new_book_try_to_add_same_book_get_dict_with_2_books(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_rating()) == 2

    def test_add_book_in_favorites_add_one_book_in_favorities(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_one_book_in_favorities(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_try_add_one_book_in_favorities_out_of_dict(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_list_of_favorites_books()) == 0