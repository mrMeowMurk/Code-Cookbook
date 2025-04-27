#ifndef BRIDGE_HPP
#define BRIDGE_HPP

#include <iostream>
#include <string>

/**
 * @class Implementation
 * @brief Абстрактный класс реализации.
 */
class Implementation {
public:
    virtual ~Implementation() = default;
    virtual std::string operationImplementation() const = 0;
};

/**
 * @class ConcreteImplementationA
 * @brief Конкретная реализация A.
 */
class ConcreteImplementationA : public Implementation {
public:
    std::string operationImplementation() const override {
        return "ConcreteImplementationA: результат операции";
    }
};

/**
 * @class ConcreteImplementationB
 * @brief Конкретная реализация B.
 */
class ConcreteImplementationB : public Implementation {
public:
    std::string operationImplementation() const override {
        return "ConcreteImplementationB: результат операции";
    }
};

/**
 * @class Abstraction
 * @brief Абстрактный класс абстракции.
 */
class Abstraction {
protected:
    Implementation* implementation;

public:
    Abstraction(Implementation* impl) : implementation(impl) {}
    virtual ~Abstraction() = default;

    virtual std::string operation() const {
        return "Abstraction: базовая операция с " + implementation->operationImplementation();
    }
};

/**
 * @class ExtendedAbstraction
 * @brief Расширенная абстракция.
 */
class ExtendedAbstraction : public Abstraction {
public:
    ExtendedAbstraction(Implementation* impl) : Abstraction(impl) {}

    std::string operation() const override {
        return "ExtendedAbstraction: расширенная операция с " + implementation->operationImplementation();
    }
};

#endif // BRIDGE_HPP 