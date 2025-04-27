"""
Паттерн Singleton (Одиночка)

Паттерн Singleton гарантирует, что у класса есть только один экземпляр,
и предоставляет глобальную точку доступа к этому экземпляру.

Применение:
- Когда в системе должен быть единственный экземпляр класса
- Когда нужно обеспечить глобальный доступ к этому экземпляру
- Когда нужно контролировать количество экземпляров класса

Преимущества:
+ Гарантирует наличие единственного экземпляра класса
+ Предоставляет глобальную точку доступа
+ Позволяет отложить инициализацию до первого использования

Недостатки:
- Нарушает принцип единственной ответственности
- Маскирует плохой дизайн
- Проблемы при многопоточности
- Сложность тестирования
"""

class Singleton:
    """
    Базовый класс для реализации паттерна Singleton.
    Используется как метакласс для создания классов-одиночек.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Метод вызывается при создании экземпляра класса.
        Проверяет наличие существующего экземпляра и возвращает его,
        если он существует, или создает новый.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    """
    Пример класса-одиночки для работы с базой данных.
    """
    def __init__(self):
        """
        Инициализация соединения с базой данных.
        В реальном приложении здесь будет код подключения к БД.
        """
        self.connection = "Connected to database"
        print("Initializing database connection...")

    def query(self, sql):
        """
        Выполнение SQL-запроса.
        
        Args:
            sql (str): SQL-запрос для выполнения
            
        Returns:
            str: Результат выполнения запроса
        """
        return f"Executing query: {sql}"


class Configuration(metaclass=Singleton):
    """
    Пример класса-одиночки для работы с конфигурацией.
    """
    def __init__(self):
        """
        Инициализация конфигурации.
        В реальном приложении здесь будет загрузка конфигурации из файла.
        """
        self.settings = {
            "host": "localhost",
            "port": 8080,
            "debug": True
        }
        print("Loading configuration...")

    def get_setting(self, key):
        """
        Получение значения настройки по ключу.
        
        Args:
            key (str): Ключ настройки
            
        Returns:
            any: Значение настройки
        """
        return self.settings.get(key)


# Пример использования
if __name__ == "__main__":
    # Создание экземпляров базы данных
    db1 = Database()
    db2 = Database()
    
    # Проверка, что это один и тот же объект
    print(f"db1 is db2: {db1 is db2}")  # True
    
    # Использование базы данных
    print(db1.query("SELECT * FROM users"))
    
    # Создание экземпляров конфигурации
    config1 = Configuration()
    config2 = Configuration()
    
    # Проверка, что это один и тот же объект
    print(f"config1 is config2: {config1 is config2}")  # True
    
    # Использование конфигурации
    print(f"Host: {config1.get_setting('host')}")
    print(f"Port: {config1.get_setting('port')}")
    print(f"Debug: {config1.get_setting('debug')}") 