#ifndef SINGLETON_HPP
#define SINGLETON_HPP

#include <iostream>
#include <string>
#include <mutex>

/**
 * @class Singleton
 * @brief Базовый класс для реализации паттерна Singleton.
 * 
 * Паттерн Singleton гарантирует, что у класса есть только один экземпляр,
 * и предоставляет глобальную точку доступа к этому экземпляру.
 * 
 * Применение:
 * - Когда в системе должен быть единственный экземпляр класса
 * - Когда нужно обеспечить глобальный доступ к этому экземпляру
 * - Когда нужно контролировать количество экземпляров класса
 * 
 * Преимущества:
 * + Гарантирует наличие единственного экземпляра класса
 * + Предоставляет глобальную точку доступа
 * + Позволяет отложить инициализацию до первого использования
 * 
 * Недостатки:
 * - Нарушает принцип единственной ответственности
 * - Маскирует плохой дизайн
 * - Проблемы при многопоточности
 * - Сложность тестирования
 */
template<typename T>
class Singleton {
protected:
    Singleton() = default;
    virtual ~Singleton() = default;

public:
    // Запрещаем копирование и присваивание
    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;

    /**
     * @brief Получение единственного экземпляра класса.
     * 
     * @return T& Ссылка на единственный экземпляр класса
     */
    static T& getInstance() {
        static T instance;
        return instance;
    }
};

/**
 * @class Database
 * @brief Пример класса-одиночки для работы с базой данных.
 */
class Database : public Singleton<Database> {
    friend class Singleton<Database>;

private:
    std::string connection;

    Database() {
        connection = "Connected to database";
        std::cout << "Initializing database connection..." << std::endl;
    }

public:
    /**
     * @brief Выполнение SQL-запроса.
     * 
     * @param sql SQL-запрос для выполнения
     * @return std::string Результат выполнения запроса
     */
    std::string query(const std::string& sql) {
        return "Executing query: " + sql;
    }
};

/**
 * @class Configuration
 * @brief Пример класса-одиночки для работы с конфигурацией.
 */
class Configuration : public Singleton<Configuration> {
    friend class Singleton<Configuration>;

private:
    struct Settings {
        std::string host;
        int port;
        bool debug;
    } settings;

    Configuration() {
        settings.host = "localhost";
        settings.port = 8080;
        settings.debug = true;
        std::cout << "Loading configuration..." << std::endl;
    }

public:
    /**
     * @brief Получение значения настройки по ключу.
     * 
     * @param key Ключ настройки
     * @return std::string Значение настройки
     */
    std::string getSetting(const std::string& key) {
        if (key == "host") return settings.host;
        if (key == "port") return std::to_string(settings.port);
        if (key == "debug") return settings.debug ? "true" : "false";
        return "";
    }
};

#endif // SINGLETON_HPP 