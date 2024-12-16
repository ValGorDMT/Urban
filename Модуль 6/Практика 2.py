class Book:
    def __init__(self, title, author):
        """  Инициализация атрибутов книги  """
        self.title = title
        self.author = author
        self.is_checked_out = False # Статус книги – доступна или взята

    def check_out(self):
        """  Метод для оформления книги на руки  """
        if not self.is_checked_out:
            self.is_checked_out = True
            return f'Книга {self.title} успешно взята!'
        else:
            return f'Книга {self.title} уже кем-то занята!'

    def return_book(self):
        """  Метод для возврата книги  """
        if self.is_checked_out:
            self.is_checked_out = False
            return f'Книга {self.title} вернулась в библиотеку!'
        else:
            return f'Книга {self.title} не была взята!'

    def get_info(self):
        """  Получение информации о книге  """
        status = 'Книга доступна' if not self.is_checked_out else 'Книга взята'
        return f'Название: {self.title}, Автор: {self.author}, Статус: {status}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """  Добавление книги в библиотеку  """
        self.books.append(book)
        return f'Книга {book.title} добавлена в библиотеку'

    def show_books(self):
        """  Вывод списка всех книг в библиотеке  """
        if not self.books:
            return 'В библиотеке пусто'
        return '\n'.join(book.get_info() for book in self.books)

library = Library()

book_1 = Book('Гарри Поттер', 'Джуан Роулинг')
book_2 = Book('Мастер и Маргарита', 'Михаил Булгаков')
book_3 = Book('Преступление и наказание', 'Федор Достоевский')

print(library.add_book(book_1))
print(library.add_book(book_2))
print(library.add_book(book_3))

print('--' * 15)

print(library.show_books())

print('--' * 15)

print(book_1.check_out())
print(book_1.get_info())

print('--' * 15)
print(book_1.return_book())
print(book_1.get_info())