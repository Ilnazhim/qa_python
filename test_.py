import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, book):
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(book.books_genre) == 2

    def test_add_new_book(self, book):
        book.add_new_book('Метро')
        assert 'Метро' in book.books_genre

    @pytest.mark.parametrize('args', ['', '12345678901234567890123456789012345678901'])
    def test_add_new_book_not_valid_name(self, book, args):
        book.add_new_book(args)
        assert book.books_genre == {}

    def test_set_book_genre(self, book):
        book.add_new_book('Метро')
        book.set_book_genre('Метро', 'Фантастика')
        assert book.books_genre.get('Метро') == 'Фантастика'

    def test_set_book_genre_not_genre_in_book_genre(self, book):
        book.add_new_book('Метро')
        book.set_book_genre('Метро', 'Драма')
        assert book.books_genre.get('Метро') not in book.genre

    def test_get_book_genre(self, book):
        book.add_new_book('Метро')
        book.set_book_genre('Метро', 'Фантастика')
        assert book.get_book_genre('Метро') == 'Фантастика'

    def test_get_books_with_specific_genre_fantastic(self, book):
        book.add_new_book('Метро')
        book.set_book_genre('Метро', 'Фантастика')
        book.add_new_book('Два капитана')
        book.set_book_genre('Два капитана', 'Фантастика')
        assert len(book.get_books_with_specific_genre('Фантастика')) == 2

    def test_get_books_genre(self, book):
        book.add_new_book('Метро')
        book.set_book_genre('Метро', 'Фантастика')
        book.add_new_book('Два капитана')
        book.set_book_genre('Два капитана', 'Фантастика')
        assert len(book.get_books_genre()) >= 1

    def test_get_books_for_children(self, book):
        book.add_new_book('Метро')
        book.set_book_genre('Метро', 'Фантастика')
        book.add_new_book('Незнайка на луне')
        book.set_book_genre('Незнайка на луне', 'Мультфильмы')
        assert len(book.get_books_for_children()) == 2

    def test_get_books_for_children_not_append_horror(self, book):
        book.add_new_book('Дракула')
        book.set_book_genre('Дракула', 'Ужасы')
        assert len(book.get_books_for_children()) == 0

    def test_add_book_in_favorites(self, book):
        book.add_new_book('Метро')
        book.set_book_genre('Метро', 'Фантастика')
        book.add_book_in_favorites('Метро')
        assert book.favorites == ['Метро']

    def test_delete_book_from_favorites(self, book):
        book.add_new_book('Метро')
        book.set_book_genre('Метро', 'Фантастика')
        book.add_book_in_favorites('Метро')
        book.delete_book_from_favorites('Метро')
        assert book.favorites == []

    def test_get_list_of_favorites_books(self, book):
        book.add_new_book('Метро')
        book.set_book_genre('Метро', 'Фантастика')
        book.add_book_in_favorites('Метро')
        assert book.get_list_of_favorites_books() == ['Метро']
