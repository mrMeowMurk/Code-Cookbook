#ifndef MEDIATOR_HPP
#define MEDIATOR_HPP

#include <iostream>
#include <string>
#include <memory>
#include <vector>

/**
 * @class Mediator
 * @brief Базовый класс посредника.
 */
class Mediator {
public:
    virtual ~Mediator() = default;
    virtual void notify(std::shared_ptr<class Component> sender, const std::string& event) = 0;
};

/**
 * @class Component
 * @brief Базовый класс компонента.
 */
class Component {
protected:
    std::shared_ptr<Mediator> mediator;

public:
    Component(std::shared_ptr<Mediator> mediator) : mediator(mediator) {}
    virtual ~Component() = default;
};

/**
 * @class ConcreteMediator
 * @brief Конкретный посредник.
 */
class ConcreteMediator : public Mediator {
private:
    std::shared_ptr<class Component1> component1;
    std::shared_ptr<class Component2> component2;

public:
    void setComponent1(std::shared_ptr<class Component1> c1) {
        component1 = c1;
    }

    void setComponent2(std::shared_ptr<class Component2> c2) {
        component2 = c2;
    }

    void notify(std::shared_ptr<Component> sender, const std::string& event) override {
        if (event == "A") {
            std::cout << "Посредник реагирует на A и запускает следующие операции:" << std::endl;
            component2->doC();
        } else if (event == "D") {
            std::cout << "Посредник реагирует на D и запускает следующие операции:" << std::endl;
            component1->doB();
            component2->doC();
        }
    }
};

/**
 * @class Component1
 * @brief Компонент 1.
 */
class Component1 : public Component {
public:
    Component1(std::shared_ptr<Mediator> mediator) : Component(mediator) {}

    void doA() {
        std::cout << "Компонент 1 выполняет A." << std::endl;
        mediator->notify(shared_from_this(), "A");
    }

    void doB() {
        std::cout << "Компонент 1 выполняет B." << std::endl;
    }
};

/**
 * @class Component2
 * @brief Компонент 2.
 */
class Component2 : public Component {
public:
    Component2(std::shared_ptr<Mediator> mediator) : Component(mediator) {}

    void doC() {
        std::cout << "Компонент 2 выполняет C." << std::endl;
        mediator->notify(shared_from_this(), "C");
    }

    void doD() {
        std::cout << "Компонент 2 выполняет D." << std::endl;
        mediator->notify(shared_from_this(), "D");
    }
};

#endif // MEDIATOR_HPP 