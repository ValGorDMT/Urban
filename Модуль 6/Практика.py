
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False 

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f'Книга {self.title} успешно взята!'
        else:
            return f'Книга {self.title} уже занята!'

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f'Книга {self.title} книга возвращена!'
        else:
            return f'Книга {self.title} книга свободна!'
        
    def get_info(self):
        staatus = 'Книга доступна' if not self.is_checked_out else 'Книга взята'
        return f'Название: {self.title}, Автор: {self.author}, Статус: {staatus}'
    

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f'Книга {book.title} добавлена в библиотеку'
    
    def show_books(self):
        '''Вывод списка библиотеки'''
        if not self.books:
            return 'В билиотеке пусто'
        return '\n'.join(book.get_info() for book in self.Book)
    

library = Library()

book_1 = Book('Гарри Потер', 'Джуан Роулинг')
book_2 = Book('Мастер и Маргарита', 'Михаил Булгаков')
book_3 = Book('Преступление и наказание', 'Федор Достоевский')

print(library.add_book(book_1))
print(library.add_book(book_2))
print(library.add_book(book_3))

print('--' * 15)