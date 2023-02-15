# qa_python

### test №1: test_add_new_book_add_two_books (пример)
    Создаем 2 книги, проверяем, что добавилось именно 2 книги
##### ------------------------------------------------------
### test №2: test_add_new_book_add_book_default_rating1
    Создаем 1 книгу, проверяем, что у добавленной книги по умолчанию рейтинг 1

### test №3: test_add_new_book_add_book_twice_save_one
    Создаем 1 книгу, добавлеем ее дважды в словарь, проверяем, что добавилась именно она и одна

### test №4: test_set_book_rating_add_book_with_rating
    Создаем 1 книгу, устанавливаем ей рейтинг, проверяем, что установленный рейтинг сохранился
    
### test №5: test_set_book_rating_add_book_with_rating_negative_input
    Создаем 1 книгу, пытаемся установить ей рейтинг вне допустимого диапазона 
    (негативные кейсы), проверяем, что при таких значениях 
    для книги устанавливается рейтинг по умолчанию (= 1)

### test №6: test_set_book_rating_set_rating_for_book_not_from_collector
    Устанавливаем рейтинг для книги, которой нет в коллекции, затем пытаемся получить ее рейтинг,
    получаем None 

### test №7: test_get_books_rating_rating_store_in_dict
    Создаем 1 книгу, устанавливаем ей рейтинг, получаем тип структуры, 
    куда сохраняются рейтинги, и это словарь
      
### test №8: test_get_books_with_specific_rating_empty_collector_is_empty
    Cоздаем экземпляр класса BooksCollector, 
    пытаемся получить данные specific_rating по разным тапам рейтинга
    (позитивные и негативные кейсы), получаем пустой спасок

### test №9: test_get_books_with_specific_rating_add7_books_with_rating_get4
    Создаем 7 книг, у 4 из них рейтинг 7, получаем данные по specific_rating = 7, получаем 4 книги c указанныс
    рейтингом

### test №10: test_get_books_with_specific_rating_book_with_rating1_not_exist
    Создаем книгу с рейтингом 7, пытаемся получить книгу с рейтингом 1, получаем пустой список

### test №11: test_add_book_in_favorites_add_two_books
    Создаем 2 книги и добавлем их в избранное, проверяем, что именно эти 2 книги добавились

### test №12: test_add_book_in_favorites_add_books_in_favourites_twice_saved_one
    Создаем книгу, устанавливаем ей рейтинг, добавляем в избранное дважды,
    проверяем, что в избранное добавилась именно эта книга и 1 раз

### test №13: test_add_book_in_favorites_book_no_in_collector
    Пытаемся добавить книгу в избранное, когда ее нет в колекции, получаем пустой список

### test №14: test_delete_book_from_favorites_delete_from_favourites_after_add
    Создаем 1 книгу с рейтингом, добавляем ее в избранное и удаляем ее из избранного,
    проверяем, что возвращается пустой список

### test №15: test_delete_book_from_favorites_add_three_delete_two
    Создаем 3 книги с рейтингом, добавляем все 3 в избранное, удаляем 2 из избранного,
    проверяем, что в избранном осталась 1 книга

### test №16: test_delete_book_from_favorites_no_one_book_in_favourites
    Создаем 3 книги с рейтингом, НЕ добавляем ни одну из них в избранное (favourites is empty), пытаемся удалить 
    первую книгу из избранного, получаем None

### test №17: test_delete_book_from_favorites_book_does_not_exist_in_favorites
    Создаем 1 книгу с рейтингом, добавляем ее в избранное (favourites not empty), пытаемся удалить 
    книгу из избранного, которой там не было, получаем None + делаем проверку, что favourites not empty -
    там лежит добавленная в избранное ранее книга

### test #18: test_get_list_of_favorites_books_favourites_books_store_in_list
    Создаем книгу и добавляем ее в избранное, получаем список избранных книг с 1 книгой