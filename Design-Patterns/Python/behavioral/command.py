"""
Паттерн Command (Команда)

Паттерн Command инкапсулирует запрос как объект, позволяя параметризовать клиентов
различными запросами, ставить запросы в очередь, логировать их и поддерживать
отмену операций.

Применение:
- Когда нужно параметризовать объекты выполняемым действием
- Когда нужно ставить операции в очередь, выполнять их по расписанию или передавать по сети
- Когда нужна операция отмены
- Когда нужно поддерживать логирование операций

Преимущества:
+ Инкапсулирует запрос как объект
+ Позволяет параметризовать клиентов различными запросами
+ Позволяет ставить запросы в очередь
+ Позволяет поддерживать отмену операций
+ Позволяет поддерживать логирование операций

Недостатки:
- Может привести к большому количеству классов
- Может усложнить код
- Может быть сложно отладить
"""

from abc import ABC, abstractmethod
from typing import List


class Command(ABC):
    """
    Базовый класс команды.
    """
    @abstractmethod
    def execute(self) -> None:
        """Выполняет команду."""
        pass


class Receiver:
    """
    Получатель команды.
    """
    def do_something(self, a: str) -> None:
        """
        Выполняет действие.
        
        Args:
            a (str): Параметр действия
        """
        print(f"Receiver: работаю с {a}")

    def do_something_else(self, b: str) -> None:
        """
        Выполняет другое действие.
        
        Args:
            b (str): Параметр действия
        """
        print(f"Receiver: также работаю с {b}")


class SimpleCommand(Command):
    """
    Простая команда.
    """
    def __init__(self, pay_load: str):
        self._pay_load = pay_load

    def execute(self) -> None:
        """Выполняет команду."""
        print(f"SimpleCommand: вижу, вы хотите, чтобы я сделал что-то простое ({self._pay_load})")


class ComplexCommand(Command):
    """
    Сложная команда.
    """
    def __init__(self, receiver: Receiver, a: str, b: str):
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """Выполняет команду."""
        print("ComplexCommand: сложные вещи должны выполняться получателем")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Invoker:
    """
    Вызывающий.
    """
    def __init__(self):
        self._on_start: List[Command] = []
        self._on_finish: List[Command] = []

    def set_on_start(self, command: Command) -> None:
        """
        Устанавливает команду на начало.
        
        Args:
            command (Command): Команда
        """
        self._on_start.append(command)

    def set_on_finish(self, command: Command) -> None:
        """
        Устанавливает команду на конец.
        
        Args:
            command (Command): Команда
        """
        self._on_finish.append(command)

    def do_something_important(self) -> None:
        """Выполняет важное действие."""
        print("Invoker: кто-то хочет сделать что-то до того, как я начну?")
        for command in self._on_start:
            command.execute()

        print("Invoker: ...делаю что-то действительно важное...")

        print("Invoker: кто-то хочет сделать что-то после того, как я закончу?")
        for command in self._on_finish:
            command.execute()


# Пример использования
if __name__ == "__main__":
    invoker = Invoker()
    receiver = Receiver()

    # Создаем команды
    simple_command = SimpleCommand("Скажи привет!")
    complex_command = ComplexCommand(receiver, "Отправь email", "Сохрани отчет")

    # Устанавливаем команды
    invoker.set_on_start(simple_command)
    invoker.set_on_finish(complex_command)

    # Выполняем команды
    invoker.do_something_important() 