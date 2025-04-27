#ifndef CHAIN_OF_RESPONSIBILITY_HPP
#define CHAIN_OF_RESPONSIBILITY_HPP

#include <iostream>
#include <string>
#include <memory>

/**
 * @class Handler
 * @brief Базовый класс обработчика.
 */
class Handler {
protected:
    std::shared_ptr<Handler> next;

public:
    Handler() : next(nullptr) {}
    virtual ~Handler() = default;

    void setNext(std::shared_ptr<Handler> handler) {
        next = handler;
    }

    virtual void handleRequest(const std::string& request) {
        if (next) {
            next->handleRequest(request);
        }
    }
};

/**
 * @class ConcreteHandlerA
 * @brief Конкретный обработчик A.
 */
class ConcreteHandlerA : public Handler {
public:
    void handleRequest(const std::string& request) override {
        if (request == "A") {
            std::cout << "Обработчик A обрабатывает запрос" << std::endl;
        } else {
            Handler::handleRequest(request);
        }
    }
};

/**
 * @class ConcreteHandlerB
 * @brief Конкретный обработчик B.
 */
class ConcreteHandlerB : public Handler {
public:
    void handleRequest(const std::string& request) override {
        if (request == "B") {
            std::cout << "Обработчик B обрабатывает запрос" << std::endl;
        } else {
            Handler::handleRequest(request);
        }
    }
};

/**
 * @class ConcreteHandlerC
 * @brief Конкретный обработчик C.
 */
class ConcreteHandlerC : public Handler {
public:
    void handleRequest(const std::string& request) override {
        if (request == "C") {
            std::cout << "Обработчик C обрабатывает запрос" << std::endl;
        } else {
            Handler::handleRequest(request);
        }
    }
};

#endif // CHAIN_OF_RESPONSIBILITY_HPP 