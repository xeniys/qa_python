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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('name',
                             ['Жареные зеленые помидоры в кафе "Полустанок',
                              'Клуб любителей книг и пирогов из картофельных очистков'])
    def test_add_new_book_name_length_more_than_forty(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_book_genre('Оно') == 'Ужасы'

    # Не писала отдельный тест для метода test_get_book_genre(), т.к. был бы дубль теста выше

    def test_get_books_with_specific_genre_get_books_with_comedy_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Ваша взяла, Дживс!')
        collector.set_book_genre('Ваша взяла, Дживс!', 'Комедии')
        collector.add_new_book('Сенсация')
        collector.set_book_genre('Сенсация', 'Комедии')

        assert collector.get_books_with_specific_genre('Комедии') == ['Ваша взяла, Дживс!', 'Сенсация']

    def test_get_books_genre_get_all_books(self):
        collector = BooksCollector()
        collector.add_new_book('Недоросль')
        collector.add_new_book('Сон в летнюю ночь')
        collector.add_new_book('Мина Мазайло')

        assert collector.get_books_genre() == {'Недоросль': '', 'Сон в летнюю ночь': '', 'Мина Мазайло': ''}

    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Голова профессора Доуэля', 'Фантастика'],
                                 ['Ходячий замок', 'Мультфильмы'],
                                 ['Аладдин и волшебная лампа', 'Комедии']
                             ])
    def test_get_books_for_children_books_not_in_genre_age_rating(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_for_children() == [name]

    @pytest.mark.parametrize('name, genre',
                             [
                                 ['Оно', 'Ужасы'],
                                 ['Самый прикольный детектив', 'Детективы']
                             ])
    def test_get_books_for_children_books_in_genre_age_rating(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert len(collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_book_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Кубок Огня')
        collector.add_book_in_favorites('Гарри Поттер и Кубок Огня')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер и Кубок Огня']

    def test_add_book_in_favorites_book_not_in_list(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Гарри Поттер и Кубок Огня')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_book_in_favorites_exist(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        collector.add_book_in_favorites('Гарри Поттер и Узник Азкабана')
        collector.delete_book_from_favorites('Гарри Поттер и Узник Азкабана')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_two_books_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        collector.add_book_in_favorites('Гарри Поттер и Узник Азкабана')
        collector.add_new_book('Гарри Поттер и Кубок Огня')
        collector.add_book_in_favorites('Гарри Поттер и Кубок Огня')

        assert len(collector.get_list_of_favorites_books()) == 2
