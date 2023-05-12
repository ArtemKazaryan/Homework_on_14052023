
# !!!!!!  ДЛЯ ЗАПУСКА ОТДЕЛЬНЫХ ЗАДАНИЙ РАСКОММЕНТИРУЙТЕ ИХ РЕШЕНИЕ, ЕСЛИ ПОТРЕБУЕТСЯ  !!!!!!

# Домашняя работа на 14.05.2023.

# Модуль 12. Паттерны проектирования
# Тема: Паттерны проектирования. Часть 2

# Задание 1
# Создайте реализацию паттерна Command.
# Протестируйте работу созданного класса.

# Решение:
print()
print('-'*49)
print('*'*11, 'РЕЗУЛЬТАТЫ ПО ЗАДАНИЮ №1:', '*'*11)

from abc import ABC, abstractmethod

# Создаем абстрактный класс Command
class Command(ABC):
    def execute(self):
        pass

# Создаем классы конкретных команд, наследующихся от абстрактного класса Command
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Создаем класс Invoker, который будет вызывать команды
class RemoteControl:
    def __init__(self):
        self.commands = {}

    def set_command(self, slot, command):
        self.commands[slot] = command

    def press_button(self, slot):
        self.commands[slot].execute()

# Создаем класс Receiver, который будет выполнять действия, связанные с командами
class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Light is on")

    def turn_off(self):
        self.is_on = False
        print("Light is off")

# Создаем объекты классов
light = Light()
light_on_command = LightOnCommand(light)
light_off_command = LightOffCommand(light)
remote_control = RemoteControl()

# Настраиваем пульт управления
remote_control.set_command(1, light_on_command)
remote_control.set_command(0, light_off_command)

# Тестируем пульт управления
remote_control.press_button(1) # Включаем свет
remote_control.press_button(0) # Выключаем свет


# Задание 2
# Есть класс, предоставляющий доступ к набору чисел.
# Источником этого набора чисел является некоторый
# файл. С определенной периодичностью данные в файле
# меняются (надо реализовать механизм обновления).
# Приложение должно получать доступ к этим данным и
# выполнять набор операций над ними (сумма, максимум,
# минимум и т.д.). При каждой попытке доступа к этому
# набору необходимо вносить запись в лог-файл.
# При реализации используйте паттерн Proxy (для логгирования)
# и другие необходимые паттерны.

# Решение:
print()
print('-'*49)
print('*'*11, 'РЕЗУЛЬТАТЫ ПО ЗАДАНИЮ №2:', '*'*11)

# Импорт модулей
import time
# Класс, предоставляющий доступ к набору чисел
class Numbers:
    # Конструктор класса
    def __init__(self, filename):
        self.filename = filename
        self.numbers = []
        self.load_numbers() # Загрузка чисел из файла
    # Загрузка чисел из файла
    def load_numbers(self):
        with open(self.filename, 'r') as f:
            for line in f:
                self.numbers.append(int(line.strip()))

    def load_numbers(self):
        with open(self.filename, 'r') as f:
            for line in f:
                self.numbers.append(int(line.strip()))
    # Обновление чисел из файла
    def update_numbers(self):
        self.numbers = []
        self.load_numbers()
    # Получение суммы чисел
    def get_sum(self):
        result = sum(self.numbers)
        self.log(f'Сумма чисел: {format(result)}')
        return result
    # Получение максимального числа
    def get_max(self):
        result = max(self.numbers)
        self.log(f'Максимальное число: {format(result)}')
        return result
    # Получение минимального числа
    def get_min(self):
        result = min(self.numbers)
        self.log(f'Минимальное число: {format(result)}')
        return result
    # Логирование операций
    def log(self, message):
        with open('log.txt', 'a') as f:
            f.write('[{}] {}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'), message))
# Класс-прокси для логгирования доступа к набору чисел
class NumbersProxy:
    # Конструктор класса
    def __init__(self, filename):
        self.numbers = Numbers(filename)
    # Обновление чисел из файла
    def update_numbers(self):
        self.numbers.update_numbers()
    # Получение суммы чисел
    def get_sum(self):
        return self.numbers.get_sum()
    # Получение максимального числа
    def get_max(self):
        return self.numbers.get_max()
    # Получение минимального числа
    def get_min(self):
        return self.numbers.get_min()
    # Логирование операций
    def log(self, message):
        self.numbers.log(message)
# Тестирование
if __name__ == '__main__':
    numbers = NumbersProxy('numbers.txt')
    print(numbers.get_sum())
    print(numbers.get_max())
    print(numbers.get_min())

# Задание 3
# Создайте приложение для работы в библиотеке. Оно
# должно оперировать следующими сущностями: Книга,
# Библиотекарь, Читатель. Приложение должно позволять
# вводить, удалять, изменять, сохранять в файл, загружать из
# файла, логгировать действия, искать информацию
# (результаты поиска выводятся на экран или файл) о сущностях.
# При реализации используйте максимально возможное
# количество паттернов проектирования.

# Решение:
print()
print('-'*49)
print('*'*11, 'РЕЗУЛЬТАТЫ ПО ЗАДАНИЮ №3:', '*'*11)

# Импортируем модуль логгирования
import logging
# Создаем логгер
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# Создаем обработчик для записи логов в файл
file_handler = logging.FileHandler('library.log')
file_handler.setLevel(logging.INFO)
# Создаем форматтер для логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
# Добавляем обработчик в логгер
logger.addHandler(file_handler)
# Создаем класс Книга
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f'Книга "{self.title}" автора {self.author}, {self.year} год'
# Создаем класс Библиотекарь
class Librarian:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __str__(self):
        return f'Библиотекарь {self.name} {self.surname}'
# Создаем класс Читатель
class Reader:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.books = []
    def __str__(self):
        return f'Читатель {self.name} {self.surname}'
    # Метод для добавления книги в список книг читателя
    def add_book(self, book):
        self.books.append(book)
    # Метод для удаления книги из списка книг читателя
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            logger.info(f'Книга "{book.title}" удалена из списка книг читателя {self.name} {self.surname}')
        else:
            logger.warning(f'Книга "{book.title}" не найдена в списке книг читателя {self.name} {self.surname}')
# Создаем класс Библиотека
class Library:
    def __init__(self):
        self.books = []
        self.librarians = []
        self.readers = []
    # Метод для добавления книги в библиотеку
    def add_book(self, book):
        self.books.append(book)
        logger.info(f'Книга "{book.title}" добавлена в библиотеку')
    # Метод для удаления книги из библиотеки
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            logger.info(f'Книга "{book.title}" удалена из библиотеки')
        else:
            logger.warning(f'Книга "{book.title}" не найдена в библиотеке')
    # Метод для добавления библиотекаря
    def add_librarian(self, librarian):
        self.librarians.append(librarian)
        logger.info(f'Библиотекарь {librarian.name} {librarian.surname} добавлен в библиотеку')
    # Метод для удаления библиотекаря
    def remove_librarian(self, librarian):
        if librarian in self.librarians:
            self.librarians.remove(librarian)
            logger.info(f'Библиотекарь {librarian.name} {librarian.surname} удален из библиотеки')
        else:
            logger.warning(f'Библиотекарь {librarian.name} {librarian.surname} не найден в библиотеке')
    # Метод для добавления читателя
    def add_reader(self, reader):
        self.readers.append(reader)
        logger.info(f'Читатель {reader.name} {reader.surname} добавлен в библиотеку')
    # Метод для удаления читателя
    def remove_reader(self, reader):
        if reader in self.readers:
            self.readers.remove(reader)
            logger.info(f'Читатель {reader.name} {reader.surname} удален из библиотеки')
        else:
            logger.warning(f'Читатель {reader.name} {reader.surname} не найден в библиотеке')
    # Метод для сохранения библиотеки в файл
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for book in self.books:
                f.write(f'{book.title};{book.author};{book.year}\n')
            for librarian in self.librarians:
                f.write(f'{librarian.name};{librarian.surname};librarian\n')
            for reader in self.readers:
                f.write(f'{reader.name};{reader.surname};reader')
                for book in reader.books:
                    f.write(f';{book.title}')
                    f.write('\n')
                logger.info(f'Библиотека сохранена в файл {filename}')

    # Метод для загрузки библиотеки из файла
    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                fields = line.strip().split(';')
                if fields[-1] == 'librarian':
                    librarian = Librarian(fields[0], fields[1])
                    self.add_librarian(librarian)
                elif fields[-1] == 'reader':
                    reader = Reader(fields[0], fields[1])
                    for book_title in fields[2:]:
                        book = self.find_book_by_title(book_title)
                        if book:
                            reader.add_book(book)
                    self.add_reader(reader)
                else:
                    book = Book(fields[0], fields[1], fields[1])
                    self.add_book(book)
        logger.info(f'Библиотека загружена из файла {filename}')

    # Метод для поиска книги по названию
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    # Метод для поиска книги по автору
    def find_book_by_author(self, author):
        found_books = []
        for book in self.books:
            if book.author == author:
                found_books.append(book)
        return found_books

    # Метод для поиска книги по году издания
    def find_book_by_year(self, year):
        found_books = []
        for book in self.books:
            if book.year == year:
                found_books.append(book)
        return found_books
# Создаем объект библиотеки
library = Library()
# Добавляем книги
book1 = Book('Мастер и Маргарита', 'Михаил Булгаков', 1966)
book2 = Book('1984', 'Джордж Оруэлл', 1949)
book3 = Book('Преступление и наказание', 'Федор Достоевский', 1866)
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
# Добавляем библиотекарей
librarian1 = Librarian('Иван', 'Иванов')
librarian2 = Librarian('Петр', 'Петров')
library.add_librarian(librarian1)
library.add_librarian(librarian2)
# Добавляем читателей
reader1 = Reader('Алексей', 'Иванов')
reader2 = Reader('Владимир', 'Петров')
reader1.add_book(book1)
reader1.add_book(book2)
reader2.add_book(book3)
library.add_reader(reader1)
library.add_reader(reader2)
# Удаляем книгу
library.remove_book(book2)
# Удаляем библиотекаря
library.remove_librarian(librarian2)
# Удаляем читателя
library.remove_reader(reader2)
# Сохраняем библиотеку в файл
library.save_to_file('library.txt')
# Загружаем библиотеку из файла
library.load_from_file('library.txt')
# Ищем книги
found_book1 = library.find_book_by_title('Мастер и Маргарита')
found_books2 = library.find_book_by_author('Михаил Булгаков')
found_books3 = library.find_book_by_year(1866)
# Выводим результаты поиска на экран
print(found_book1)
for book in found_books2:
    print(book)
for book in found_books3:
    print(book)