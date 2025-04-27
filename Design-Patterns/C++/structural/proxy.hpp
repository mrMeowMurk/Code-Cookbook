#ifndef PROXY_HPP
#define PROXY_HPP

#include <iostream>
#include <string>
#include <memory>

/**
 * @class Subject
 * @brief Базовый класс субъекта.
 */
class Subject {
public:
    virtual ~Subject() = default;
    virtual void request() const = 0;
};

/**
 * @class RealSubject
 * @brief Реальный субъект.
 */
class RealSubject : public Subject {
public:
    void request() const override {
        std::cout << "RealSubject: обработка запроса" << std::endl;
    }
};

/**
 * @class Proxy
 * @brief Заместитель.
 */
class Proxy : public Subject {
private:
    std::shared_ptr<RealSubject> realSubject;

    bool checkAccess() const {
        std::cout << "Proxy: проверка доступа" << std::endl;
        return true;
    }

    void logAccess() const {
        std::cout << "Proxy: логирование доступа" << std::endl;
    }

public:
    Proxy(std::shared_ptr<RealSubject> subject) : realSubject(subject) {}

    void request() const override {
        if (checkAccess()) {
            realSubject->request();
            logAccess();
        }
    }
};

#endif // PROXY_HPP 