# qa_python

Для проверки методов класса BooksCollector были реализованы следующие тесты:

1) test_add_new_book_name_length_more_than_forty() - проверяет, что метод add_new_book_name не добавляет книги с 
названием более 40 символов  в словарь
2) test_set_book_genre() - проверяет, что метод set_book_genre устанавливает книге указанный жанр 
3) test_get_books_with_specific_genre_get_books_with_comedy_genre(self) - проверяет, что метод get_books_with_specific_genre()
возвращает список книг с указанным жанром (Комедии)
4) test_get_books_genre_get_all_books(self) - проверяет, что  метод get_books_genre возвращает словарь со всеми 
добавленными книгами
5) test_get_books_for_children_books_not_in_genre_age_rating() - проверяет, что метод get_books_for_children_books
возвращает список книг, жанр которых есть в списке доступных для детей жанров
6) test_get_books_for_children_books_in_genre_age_rating - проверяет, что метод get_books_for_children_books
 не возвращает книги, жанров которых нет в списке доступных для детей жанров
7) test_add_book_in_favorites_book_not_in_favorites() - проверяет, что метод add_book_in_favorites_book
 добавляет книгу в список Избранных (книга ранее не добавлялась в избранное)
8) test_add_book_in_favorites_book_not_in_list() - проверяет, что метод add_book_in_favorites_book  не добавляет 
книгу в список Избранных, если ее нет в общем списке книг
9) test_delete_book_from_favorites_book_in_favorites_exist() - проверяет, что метод delete_book_from_favorites удаляет
книгу из избранного
10) test_get_list_of_favorites_books_two_books_in_list() - проверяет, что метод get_list_of_favorites_books возвращает
список избранных книг (проверяем длину списка, в данном кейсе две книги)


