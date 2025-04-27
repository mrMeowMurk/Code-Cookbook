"""
Паттерн Flyweight (Легковес)

Паттерн Flyweight позволяет эффективно использовать память, разделяя общее состояние
между множеством объектов. Он используется, когда нужно создать большое количество
объектов, которые имеют много общих свойств.

Применение:
- Когда в приложении используется большое количество объектов
- Когда большая часть состояния объектов может быть вынесена вовне
- Когда после вынесения состояния многие группы объектов могут быть заменены
  относительно небольшим количеством общих объектов
- Когда приложение не зависит от идентичности объектов

Преимущества:
+ Экономит память
+ Уменьшает количество создаваемых объектов
+ Упрощает работу с большим количеством объектов
+ Улучшает производительность

Недостатки:
- Может усложнить код
- Может быть сложно отладить
- Может быть сложно реализовать, если объекты имеют много состояний
"""

from abc import ABC, abstractmethod
from typing import Dict


class Flyweight(ABC):
    """
    Базовый класс легковеса.
    """
    @abstractmethod
    def operation(self, extrinsic_state: str) -> None:
        """
        Выполняет операцию.
        
        Args:
            extrinsic_state (str): Внешнее состояние
        """
        pass


class ConcreteFlyweight(Flyweight):
    """
    Конкретный легковес.
    """
    def __init__(self, intrinsic_state: str):
        self._intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state: str) -> None:
        """
        Выполняет операцию.
        
        Args:
            extrinsic_state (str): Внешнее состояние
        """
        print(f"ConcreteFlyweight: внутреннее состояние = {self._intrinsic_state}, "
              f"внешнее состояние = {extrinsic_state}")


class FlyweightFactory:
    """
    Фабрика легковесов.
    """
    def __init__(self):
        self._flyweights: Dict[str, Flyweight] = {}

    def get_flyweight(self, key: str) -> Flyweight:
        """
        Получает легковес по ключу.
        
        Args:
            key (str): Ключ легковеса
            
        Returns:
            Flyweight: Легковес
        """
        if key not in self._flyweights:
            self._flyweights[key] = ConcreteFlyweight(key)
        return self._flyweights[key]

    def list_flyweights(self) -> None:
        """Выводит список всех легковесов."""
        print(f"FlyweightFactory: у меня {len(self._flyweights)} легковесов:")
        for key in self._flyweights:
            print(key)


def client_code(factory: FlyweightFactory, intrinsic_state: str, extrinsic_state: str) -> None:
    """
    Клиентский код.
    
    Args:
        factory (FlyweightFactory): Фабрика легковесов
        intrinsic_state (str): Внутреннее состояние
        extrinsic_state (str): Внешнее состояние
    """
    print(f"Клиент: получаю легковес с внутренним состоянием {intrinsic_state}")
    flyweight = factory.get_flyweight(intrinsic_state)
    flyweight.operation(extrinsic_state)


# Пример использования
if __name__ == "__main__":
    factory = FlyweightFactory()

    # Используем один и тот же легковес с разными внешними состояниями
    client_code(factory, "A", "1")
    client_code(factory, "A", "2")
    client_code(factory, "B", "3")

    print()
    factory.list_flyweights() 