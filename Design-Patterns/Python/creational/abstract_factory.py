"""
Паттерн Abstract Factory (Абстрактная фабрика)

Паттерн Abstract Factory предоставляет интерфейс для создания семейств
связанных или зависимых объектов без указания их конкретных классов.

Применение:
- Когда система должна быть независимой от процесса создания объектов
- Когда нужно создать семейство связанных объектов
- Когда нужно скрыть детали реализации от клиентского кода

Преимущества:
+ Изолирует конкретные классы
+ Упрощает замену семейств продуктов
+ Гарантирует совместимость создаваемых объектов
+ Реализует принцип открытости/закрытости

Недостатки:
- Сложность добавления новых типов продуктов
- Большое количество классов
- Сложность поддержки
"""

from abc import ABC, abstractmethod

class Button(ABC):
    """
    Абстрактный класс кнопки.
    Определяет интерфейс для всех типов кнопок.
    """
    @abstractmethod
    def render(self):
        """Отрисовка кнопки."""
        pass

    @abstractmethod
    def click(self):
        """Обработка клика по кнопке."""
        pass


class TextBox(ABC):
    """
    Абстрактный класс текстового поля.
    Определяет интерфейс для всех типов текстовых полей.
    """
    @abstractmethod
    def render(self):
        """Отрисовка текстового поля."""
        pass

    @abstractmethod
    def input(self, text):
        """
        Ввод текста в поле.
        
        Args:
            text (str): Вводимый текст
        """
        pass


class WindowsButton(Button):
    """
    Конкретный класс кнопки для Windows.
    """
    def render(self):
        return "Отрисовка кнопки в стиле Windows"

    def click(self):
        return "Обработка клика по кнопке Windows"


class WindowsTextBox(TextBox):
    """
    Конкретный класс текстового поля для Windows.
    """
    def render(self):
        return "Отрисовка текстового поля в стиле Windows"

    def input(self, text):
        return f"Ввод текста в текстовое поле Windows: {text}"


class MacButton(Button):
    """
    Конкретный класс кнопки для Mac.
    """
    def render(self):
        return "Отрисовка кнопки в стиле Mac"

    def click(self):
        return "Обработка клика по кнопке Mac"


class MacTextBox(TextBox):
    """
    Конкретный класс текстового поля для Mac.
    """
    def render(self):
        return "Отрисовка текстового поля в стиле Mac"

    def input(self, text):
        return f"Ввод текста в текстовое поле Mac: {text}"


class GUIFactory(ABC):
    """
    Абстрактная фабрика GUI элементов.
    Определяет интерфейс для создания семейства связанных объектов.
    """
    @abstractmethod
    def create_button(self) -> Button:
        """
        Создание кнопки.
        
        Returns:
            Button: Созданная кнопка
        """
        pass

    @abstractmethod
    def create_textbox(self) -> TextBox:
        """
        Создание текстового поля.
        
        Returns:
            TextBox: Созданное текстовое поле
        """
        pass


class WindowsFactory(GUIFactory):
    """
    Конкретная фабрика для создания GUI элементов в стиле Windows.
    """
    def create_button(self) -> Button:
        return WindowsButton()

    def create_textbox(self) -> TextBox:
        return WindowsTextBox()


class MacFactory(GUIFactory):
    """
    Конкретная фабрика для создания GUI элементов в стиле Mac.
    """
    def create_button(self) -> Button:
        return MacButton()

    def create_textbox(self) -> TextBox:
        return MacTextBox()


class Application:
    """
    Класс приложения, использующий абстрактную фабрику.
    """
    def __init__(self, factory: GUIFactory):
        """
        Инициализация приложения.
        
        Args:
            factory (GUIFactory): Фабрика для создания GUI элементов
        """
        self.factory = factory
        self.button = None
        self.textbox = None

    def create_ui(self):
        """Создание пользовательского интерфейса."""
        self.button = self.factory.create_button()
        self.textbox = self.factory.create_textbox()

    def render_ui(self):
        """Отрисовка пользовательского интерфейса."""
        print(self.button.render())
        print(self.textbox.render())

    def interact(self):
        """Взаимодействие с пользовательским интерфейсом."""
        print(self.button.click())
        print(self.textbox.input("Hello, World!"))


# Пример использования
if __name__ == "__main__":
    # Создание приложения с Windows GUI
    windows_app = Application(WindowsFactory())
    windows_app.create_ui()
    print("Windows Application:")
    windows_app.render_ui()
    windows_app.interact()
    print()

    # Создание приложения с Mac GUI
    mac_app = Application(MacFactory())
    mac_app.create_ui()
    print("Mac Application:")
    mac_app.render_ui()
    mac_app.interact() 