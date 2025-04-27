"""
Паттерн Strategy (Стратегия)

Паттерн Strategy определяет семейство алгоритмов, инкапсулирует каждый из них и делает их
взаимозаменяемыми. Стратегия позволяет изменять алгоритмы независимо от клиентов, которые
ими пользуются.

Применение:
- Когда нужно использовать разные варианты одного и того же алгоритма
- Когда есть множество похожих классов, отличающихся только поведением
- Когда нужно скрыть сложные алгоритмы от клиента
- Когда нужно реализовать разные варианты поведения

Преимущества:
+ Упрощает добавление новых алгоритмов
+ Уменьшает связанность между классами
+ Упрощает тестирование
+ Соблюдает принцип единственной ответственности

Недостатки:
- Может привести к созданию большого количества классов
- Может быть сложно отладить
- Может быть сложно реализовать для сложных алгоритмов
"""

from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    Базовый класс стратегии.
    """
    @abstractmethod
    def algorithm_interface(self) -> None:
        """
        Интерфейс алгоритма.
        """
        pass


class ConcreteStrategyA(Strategy):
    """
    Конкретная стратегия A.
    """
    def algorithm_interface(self) -> None:
        """
        Реализация алгоритма A.
        """
        print("Реализация алгоритма A")


class ConcreteStrategyB(Strategy):
    """
    Конкретная стратегия B.
    """
    def algorithm_interface(self) -> None:
        """
        Реализация алгоритма B.
        """
        print("Реализация алгоритма B")


class Context:
    """
    Контекст.
    """
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        """
        Устанавливает стратегию.
        
        Args:
            strategy (Strategy): Стратегия
        """
        self._strategy = strategy

    def context_interface(self) -> None:
        """
        Интерфейс контекста.
        """
        self._strategy.algorithm_interface()


# Пример использования
if __name__ == "__main__":
    # Создаем контекст с начальной стратегией A
    context = Context(ConcreteStrategyA())

    # Выполняем алгоритм A
    context.context_interface()

    # Меняем стратегию на B
    context.set_strategy(ConcreteStrategyB())

    # Выполняем алгоритм B
    context.context_interface() 