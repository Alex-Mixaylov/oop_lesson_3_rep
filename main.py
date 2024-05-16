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