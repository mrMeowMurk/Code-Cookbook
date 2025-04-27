"""
Паттерн Factory Method (Фабричный метод)

Паттерн Factory Method определяет интерфейс для создания объекта,
но позволяет подклассам решать, какой класс инстанцировать.
Фабричный метод позволяет классу делегировать инстанцирование подклассам.

Применение:
- Когда класс не может предвидеть класс создаваемых объектов
- Когда класс хочет, чтобы его подклассы определяли создаваемые объекты
- Когда классы делегируют ответственность одному из нескольких вспомогательных подклассов

Преимущества:
+ Избавляет от привязки к конкретным классам
+ Выделяет код создания объектов в одно место
+ Упрощает добавление новых типов объектов
+ Реализует принцип открытости/закрытости

Недостатки:
- Может привести к созданию больших параллельных иерархий классов
- Требует создания дополнительных классов
"""

from abc import ABC, abstractmethod

class Document(ABC):
    """
    Абстрактный класс документа.
    Определяет интерфейс для всех типов документов.
    """
    @abstractmethod
    def create(self):
        """Создание документа."""
        pass

    @abstractmethod
    def open(self):
        """Открытие документа."""
        pass

    @abstractmethod
    def save(self):
        """Сохранение документа."""
        pass


class TextDocument(Document):
    """
    Конкретный класс текстового документа.
    """
    def create(self):
        return "Создание текстового документа"

    def open(self):
        return "Открытие текстового документа"

    def save(self):
        return "Сохранение текстового документа"


class SpreadsheetDocument(Document):
    """
    Конкретный класс табличного документа.
    """
    def create(self):
        return "Создание табличного документа"

    def open(self):
        return "Открытие табличного документа"

    def save(self):
        return "Сохранение табличного документа"


class Application(ABC):
    """
    Абстрактный класс приложения.
    Определяет фабричный метод для создания документов.
    """
    @abstractmethod
    def create_document(self) -> Document:
        """
        Фабричный метод для создания документа.
        
        Returns:
            Document: Созданный документ
        """
        pass

    def new_document(self):
        """
        Создание нового документа.
        
        Returns:
            str: Результат создания документа
        """
        doc = self.create_document()
        return doc.create()


class TextEditor(Application):
    """
    Конкретный класс текстового редактора.
    """
    def create_document(self) -> Document:
        return TextDocument()


class SpreadsheetEditor(Application):
    """
    Конкретный класс редактора таблиц.
    """
    def create_document(self) -> Document:
        return SpreadsheetDocument()


# Пример использования
if __name__ == "__main__":
    # Создание текстового редактора
    text_editor = TextEditor()
    print(text_editor.new_document())  # Создание текстового документа
    
    # Создание редактора таблиц
    spreadsheet_editor = SpreadsheetEditor()
    print(spreadsheet_editor.new_document())  # Создание табличного документа
    
    # Работа с документами
    text_doc = text_editor.create_document()
    print(text_doc.open())  # Открытие текстового документа
    print(text_doc.save())  # Сохранение текстового документа
    
    spreadsheet_doc = spreadsheet_editor.create_document()
    print(spreadsheet_doc.open())  # Открытие табличного документа
    print(spreadsheet_doc.save())  # Сохранение табличного документа 