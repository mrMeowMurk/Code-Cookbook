"""
Паттерн Builder (Строитель)

Паттерн Builder позволяет создавать сложные объекты пошагово, используя один и тот же
процесс строительства. Он отделяет конструирование сложного объекта от его представления.

Применение:
- Когда процесс создания объекта должен быть независим от частей, из которых состоит объект
- Когда процесс создания объекта должен обеспечивать различные представления создаваемого объекта
- Когда нужно изолировать логику создания объекта от его представления

Преимущества:
+ Позволяет создавать объекты пошагово
+ Позволяет использовать один и тот же код для создания различных объектов
+ Изолирует сложный код сборки объекта от его бизнес-логики

Недостатки:
- Усложняет код из-за введения дополнительных классов
- Может быть избыточным для простых объектов
"""

from abc import ABC, abstractmethod
from typing import List


class Computer:
    """
    Класс продукта - компьютер.
    """
    def __init__(self):
        self.parts: List[str] = []

    def add(self, part: str) -> None:
        """
        Добавление части к компьютеру.
        
        Args:
            part (str): Название части
        """
        self.parts.append(part)

    def list_parts(self) -> str:
        """
        Получение списка всех частей компьютера.
        
        Returns:
            str: Строка со списком частей
        """
        return f"Части компьютера: {', '.join(self.parts)}"


class ComputerBuilder(ABC):
    """
    Абстрактный класс строителя.
    Определяет общий интерфейс для создания различных частей продукта.
    """
    @abstractmethod
    def reset(self) -> None:
        """Сброс строителя."""
        pass

    @abstractmethod
    def set_cpu(self) -> None:
        """Установка процессора."""
        pass

    @abstractmethod
    def set_memory(self) -> None:
        """Установка памяти."""
        pass

    @abstractmethod
    def set_storage(self) -> None:
        """Установка накопителя."""
        pass

    @abstractmethod
    def set_graphics(self) -> None:
        """Установка видеокарты."""
        pass


class GamingComputerBuilder(ComputerBuilder):
    """
    Конкретный строитель для игрового компьютера.
    """
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._computer = Computer()

    def set_cpu(self) -> None:
        self._computer.add("Intel Core i9-13900K")

    def set_memory(self) -> None:
        self._computer.add("64GB DDR5 RAM")

    def set_storage(self) -> None:
        self._computer.add("2TB NVMe SSD")

    def set_graphics(self) -> None:
        self._computer.add("NVIDIA RTX 4090")

    def get_result(self) -> Computer:
        """
        Получение результата строительства.
        
        Returns:
            Computer: Построенный компьютер
        """
        computer = self._computer
        self.reset()
        return computer


class OfficeComputerBuilder(ComputerBuilder):
    """
    Конкретный строитель для офисного компьютера.
    """
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._computer = Computer()

    def set_cpu(self) -> None:
        self._computer.add("Intel Core i5-12400")

    def set_memory(self) -> None:
        self._computer.add("16GB DDR4 RAM")

    def set_storage(self) -> None:
        self._computer.add("512GB SSD")

    def set_graphics(self) -> None:
        self._computer.add("Intel UHD Graphics 730")

    def get_result(self) -> Computer:
        """
        Получение результата строительства.
        
        Returns:
            Computer: Построенный компьютер
        """
        computer = self._computer
        self.reset()
        return computer


class Director:
    """
    Класс директора, который управляет процессом строительства.
    """
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> ComputerBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: ComputerBuilder) -> None:
        self._builder = builder

    def build_minimal_computer(self) -> None:
        """
        Построение минимальной конфигурации компьютера.
        """
        self.builder.reset()
        self.builder.set_cpu()
        self.builder.set_memory()
        self.builder.set_storage()

    def build_full_computer(self) -> None:
        """
        Построение полной конфигурации компьютера.
        """
        self.builder.reset()
        self.builder.set_cpu()
        self.builder.set_memory()
        self.builder.set_storage()
        self.builder.set_graphics()


# Пример использования
if __name__ == "__main__":
    # Создание директора
    director = Director()

    # Создание игрового компьютера
    gaming_builder = GamingComputerBuilder()
    director.builder = gaming_builder

    print("Построение игрового компьютера:")
    director.build_full_computer()
    print(gaming_builder.get_result().list_parts())
    print()

    # Создание офисного компьютера
    office_builder = OfficeComputerBuilder()
    director.builder = office_builder

    print("Построение офисного компьютера:")
    director.build_minimal_computer()
    print(office_builder.get_result().list_parts()) 