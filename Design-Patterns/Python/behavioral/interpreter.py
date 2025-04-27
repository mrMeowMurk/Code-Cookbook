"""
Паттерн Interpreter (Интерпретатор)

Паттерн Interpreter определяет грамматику языка и интерпретирует предложения
на этом языке. Он используется для определения грамматики языка и интерпретации
предложений на этом языке.

Применение:
- Когда нужно определить грамматику языка
- Когда нужно интерпретировать предложения на языке
- Когда грамматика языка проста
- Когда эффективность не является критичной

Преимущества:
+ Упрощает изменение и расширение грамматики
+ Реализует грамматику как классы
+ Упрощает добавление новых способов интерпретации выражений
+ Соблюдает принцип единственной ответственности

Недостатки:
- Может быть сложно реализовать для сложных грамматик
- Может быть неэффективным для больших грамматик
- Может быть сложно отладить
"""

from abc import ABC, abstractmethod


class Expression(ABC):
    """
    Базовый класс выражения.
    """
    @abstractmethod
    def interpret(self, context: str) -> bool:
        """
        Интерпретирует контекст.
        
        Args:
            context (str): Контекст
            
        Returns:
            bool: Результат интерпретации
        """
        pass


class TerminalExpression(Expression):
    """
    Терминальное выражение.
    """
    def __init__(self, data: str):
        self._data = data

    def interpret(self, context: str) -> bool:
        """
        Интерпретирует контекст.
        
        Args:
            context (str): Контекст
            
        Returns:
            bool: Результат интерпретации
        """
        return self._data in context


class OrExpression(Expression):
    """
    Выражение ИЛИ.
    """
    def __init__(self, expr1: Expression, expr2: Expression):
        self._expr1 = expr1
        self._expr2 = expr2

    def interpret(self, context: str) -> bool:
        """
        Интерпретирует контекст.
        
        Args:
            context (str): Контекст
            
        Returns:
            bool: Результат интерпретации
        """
        return self._expr1.interpret(context) or self._expr2.interpret(context)


class AndExpression(Expression):
    """
    Выражение И.
    """
    def __init__(self, expr1: Expression, expr2: Expression):
        self._expr1 = expr1
        self._expr2 = expr2

    def interpret(self, context: str) -> bool:
        """
        Интерпретирует контекст.
        
        Args:
            context (str): Контекст
            
        Returns:
            bool: Результат интерпретации
        """
        return self._expr1.interpret(context) and self._expr2.interpret(context)


# Пример использования
if __name__ == "__main__":
    # Создаем выражения
    robert = TerminalExpression("Robert")
    john = TerminalExpression("John")
    julie = TerminalExpression("Julie")
    married = TerminalExpression("Married")

    # Создаем сложные выражения
    is_married = OrExpression(robert, john)
    is_married_woman = AndExpression(julie, married)

    # Тестируем выражения
    print(f"John is married? {'Yes' if is_married.interpret('John') else 'No'}")
    print(f"Julie is a married woman? {'Yes' if is_married_woman.interpret('Married Julie') else 'No'}") 