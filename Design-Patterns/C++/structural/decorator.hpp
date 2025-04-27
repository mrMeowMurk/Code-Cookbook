#ifndef DECORATOR_HPP
#define DECORATOR_HPP

#include <iostream>
#include <string>
#include <memory>

/**
 * @class Component
 * @brief Базовый класс компонента.
 */
class Component {
public:
    virtual ~Component() = default;
    virtual std::string operation() const = 0;
};

/**
 * @class ConcreteComponent
 * @brief Конкретный компонент.
 */
class ConcreteComponent : public Component {
public:
    std::string operation() const override {
        return "ConcreteComponent: базовая операция";
    }
};

/**
 * @class Decorator
 * @brief Базовый класс декоратора.
 */
class Decorator : public Component {
protected:
    std::shared_ptr<Component> component;

public:
    Decorator(std::shared_ptr<Component> c) : component(c) {}

    std::string operation() const override {
        return component->operation();
    }
};

/**
 * @class ConcreteDecoratorA
 * @brief Конкретный декоратор A.
 */
class ConcreteDecoratorA : public Decorator {
public:
    ConcreteDecoratorA(std::shared_ptr<Component> c) : Decorator(c) {}

    std::string operation() const override {
        return "ConcreteDecoratorA: (" + Decorator::operation() + ")";
    }
};

/**
 * @class ConcreteDecoratorB
 * @brief Конкретный декоратор B.
 */
class ConcreteDecoratorB : public Decorator {
public:
    ConcreteDecoratorB(std::shared_ptr<Component> c) : Decorator(c) {}

    std::string operation() const override {
        return "ConcreteDecoratorB: [" + Decorator::operation() + "]";
    }
};

#endif // DECORATOR_HPP 