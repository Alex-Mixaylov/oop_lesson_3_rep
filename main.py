# Принципы SOLID
# Принцип единственной ответственности

# class UserManager():
#     def __init__(self, user):
#         self.user = user
#
#     def change_user_name(self, new_name):
#         self.user.name = new_name
#
#     def save_user(self):
#         file = open("users.txt", "a")
#         file.write(self.user)
#         file.close()
#
#
# class User():
#     def __init__(self, name):
#         self.name = name
#
# class UserNameChanger():
#     def __init__(self, user):
#         self.user = user
#
#     def change_user_name(self, new_name):
#         self.user.name = new_name
#
# class SaveUser():
#     def __init__(self, user):
#         self.user = user
#
#     def save_user(self):
#         file = open("users.txt", "a")
#         file.write(self.user)
#         file.close()

# Принцип закрытости открытости ОСР

# class Report():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#     def docPrinter(self):
#         print(f'Сформирован отчет {self.title} с содержанием {self.content}')

#
# from abc import ABC, abstractmethod
#
# class Formated(ABC):
#     @abstractmethod
#     def format(self, report):
#         pass
#
# class TextFormated(Formated):
#     def format(self, report):
#         print(report.title)
#         print(report.content)
#
# class HTMLFormated(Formated):
#     def format(self, report):
#         print(f"<h1>{report.title}</h1>")
#         print(f"<p>{report.content}</p>")
#
# class Report():
#     def __init__(self, title, content, formated):
#         self.title = title
#         self.content = content
#         self.formated = formated
#
#     def docPrinter(self):
#         self.formated.format(self)
#
# report = Report('заголовок отчета', 'это текст отчета его тут много', HTMLFormated())
#
# report.docPrinter()

# Принцип подстановки Барбары Лисков LSP

# class Birds():
#     def __init__(self, name):
#         self.name = name
#     def fly(self):
#         print('Птица летает')
#
# class Pinguin(Birds):
#     pass
#
# p = Pinguin('Пингвин')
# p.fly()

# class Bird():
#     def fly(self):
#         print('Эта птица летает')
#
# class Duck(Bird):
#     def fly(self):
#         print('Эта утка летает быстро')
#
# def fly_in_the_sky(animal):
#     animal.fly()
#
# b = Bird()
# d = Duck()
# fly_in_the_sky(b)
# fly_in_the_sky(d)

# Принцип разделения интерфейсов ISP

# class SmartHouse():
#     def turn_on_tv(self):
#         print('Телевизор включен')
#     def turn_on_light(self):
#         print('Свет включен')
#     def heat_food(self):
#         print('Еда подогрета')

# class Light():
#      def turn_on_light(self):
#          print('Свет включен')
#      def turn_off_light(self):
#          print('Свет выключен')
#
# class TV():
#      def turn_on_tv(self):
#          print('Телевизор включен')
#      def turn_off_tv(self):
#          print('Телевизор выключен')
#
# class Food():
#      def heat_food(self):
#          print('Еда подогрета')
#      def cool_food(self):
#          print('Еда охлаждена')

# Принцип инверсии зависимостей DIP

# class Book():
#     def read(self):
#         print('Читение интерсной книги')
#
# class StoryReader():
#     def __init__(self):
#         self.book = Book()
#
#     def tell_story(self):
#         self.book.read() # Зависимость Book от StoryReader

# from abc import ABC, abstractmethod
#
# class StoreSourse(ABC):
#     @abstractmethod
#     def get_story(self):
#         pass
#
# class Book(StoreSourse):
#     def get_story(self):
#         print('Читение интерсной книги')
# class AudioBook(StoreSourse):
#     def get_story(self):
#         print('Читение интерсной книги вслух')
#
# class StoryReader():
#     def __init__(self, store_sourse: StoreSourse):
#         self.store_sourse = store_sourse
#     def tell_story(self):
#         self.store_sourse.get_story()
#
# book = Book()
# audiobook = AudioBook()
#
# reader_book = StoryReader(book)
# reader_audiobook = StoryReader(audiobook)
#
# reader_book.tell_story()
# reader_audiobook.tell_story()