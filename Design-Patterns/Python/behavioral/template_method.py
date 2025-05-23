"""
Паттерн Template Method (Шаблонный метод)

Паттерн Template Method определяет скелет алгоритма, откладывая некоторые шаги на подклассы.
Шаблонный метод позволяет подклассам переопределять определенные шаги алгоритма, не меняя
его структуру.

Применение:
- Когда нужно определить скелет алгоритма, отложив некоторые шаги на подклассы
- Когда нужно избежать дублирования кода в подклассах
- Когда нужно контролировать расширение алгоритма
- Когда нужно реализовать инвариантные части алгоритма один раз

Преимущества:
+ Упрощает повторное использование кода
+ Уменьшает дублирование кода
+ Упрощает поддержку кода
+ Соблюдает принцип единственной ответственности

Недостатки:
- Может быть сложно отладить
- Может быть сложно реализовать для сложных алгоритмов
- Может быть сложно расширить
"""

from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """
    Абстрактный класс.
    """
    def template_method(self) -> None:
        """
        Шаблонный метод.
        """
        self.primitive_operation1()
        self.primitive_operation2()
        self.hook()

    @abstractmethod
    def primitive_operation1(self) -> None:
        """
        Примитивная операция 1.
        """
        pass

    @abstractmethod
    def primitive_operation2(self) -> None:
        """
        Примитивная операция 2.
        """
        pass

    def hook(self) -> None:
        """
        Хук.
        """
        pass


class ConcreteClass(AbstractClass):
    """
    Конкретный класс.
    """
    def primitive_operation1(self) -> None:
        """
        Примитивная операция 1.
        """
        print("Выполнение примитивной операции 1")

    def primitive_operation2(self) -> None:
        """
        Примитивная операция 2.
        """
        print("Выполнение примитивной операции 2")

    def hook(self) -> None:
        """
        Хук.
        """
        print("Выполнение хука")


# Пример использования
if __name__ == "__main__":
    # Создаем конкретный класс
    concrete_class = ConcreteClass()

    # Выполняем шаблонный метод
    concrete_class.template_method() 