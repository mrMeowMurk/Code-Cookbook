"""
Паттерн Memento (Хранитель)

Паттерн Memento позволяет сохранять и восстанавливать предыдущее состояние объекта
без раскрытия деталей его реализации. Он используется для реализации механизма
отмены операций.

Применение:
- Когда нужно сохранять состояние объекта для возможности его восстановления
- Когда прямое получение состояния объекта нарушает инкапсуляцию
- Когда нужно реализовать механизм отмены операций
- Когда нужно сохранять историю состояний объекта

Преимущества:
+ Сохраняет инкапсуляцию
+ Упрощает создание объекта
+ Позволяет реализовать механизм отмены операций
+ Соблюдает принцип единственной ответственности

Недостатки:
- Может потребовать много памяти
- Может быть сложно отладить
- Может быть сложно реализовать для сложных объектов
"""

from typing import List, Optional


class Memento:
    """
    Хранитель.
    """
    def __init__(self, state: str):
        self._state = state

    def get_state(self) -> str:
        """
        Возвращает состояние.
        
        Returns:
            str: Состояние
        """
        return self._state


class Originator:
    """
    Создатель.
    """
    def __init__(self):
        self._state = ""

    def set_state(self, state: str) -> None:
        """
        Устанавливает состояние.
        
        Args:
            state (str): Состояние
        """
        self._state = state

    def get_state(self) -> str:
        """
        Возвращает состояние.
        
        Returns:
            str: Состояние
        """
        return self._state

    def save_state_to_memento(self) -> Memento:
        """
        Сохраняет состояние в хранитель.
        
        Returns:
            Memento: Хранитель
        """
        return Memento(self._state)

    def get_state_from_memento(self, memento: Memento) -> None:
        """
        Восстанавливает состояние из хранителя.
        
        Args:
            memento (Memento): Хранитель
        """
        self._state = memento.get_state()


class CareTaker:
    """
    Опекун.
    """
    def __init__(self):
        self._memento_list: List[Memento] = []

    def add(self, state: Memento) -> None:
        """
        Добавляет хранитель.
        
        Args:
            state (Memento): Хранитель
        """
        self._memento_list.append(state)

    def get(self, index: int) -> Optional[Memento]:
        """
        Возвращает хранитель по индексу.
        
        Args:
            index (int): Индекс
            
        Returns:
            Optional[Memento]: Хранитель или None
        """
        if 0 <= index < len(self._memento_list):
            return self._memento_list[index]
        return None


# Пример использования
if __name__ == "__main__":
    # Создаем объекты
    originator = Originator()
    care_taker = CareTaker()

    # Устанавливаем состояния и сохраняем их
    originator.set_state("State #1")
    originator.set_state("State #2")
    care_taker.add(originator.save_state_to_memento())
    originator.set_state("State #3")
    care_taker.add(originator.save_state_to_memento())
    originator.set_state("State #4")

    # Выводим текущее состояние
    print(f"Current State: {originator.get_state()}")

    # Восстанавливаем состояния
    originator.get_state_from_memento(care_taker.get(0))
    print(f"First saved State: {originator.get_state()}")
    originator.get_state_from_memento(care_taker.get(1))
    print(f"Second saved State: {originator.get_state()}") 