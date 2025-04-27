#ifndef TEMPLATE_METHOD_HPP
#define TEMPLATE_METHOD_HPP

#include <iostream>
#include <string>
#include <memory>

/**
 * @class AbstractClass
 * @brief Абстрактный класс.
 */
class AbstractClass {
public:
    virtual ~AbstractClass() = default;

    // Шаблонный метод
    void templateMethod() {
        primitiveOperation1();
        primitiveOperation2();
        hook();
    }

protected:
    // Примитивные операции
    virtual void primitiveOperation1() = 0;
    virtual void primitiveOperation2() = 0;

    // Хук
    virtual void hook() {}
};

/**
 * @class ConcreteClass
 * @brief Конкретный класс.
 */
class ConcreteClass : public AbstractClass {
protected:
    void primitiveOperation1() override {
        std::cout << "Выполнение примитивной операции 1" << std::endl;
    }

    void primitiveOperation2() override {
        std::cout << "Выполнение примитивной операции 2" << std::endl;
    }

    void hook() override {
        std::cout << "Выполнение хука" << std::endl;
    }
};

#endif // TEMPLATE_METHOD_HPP 