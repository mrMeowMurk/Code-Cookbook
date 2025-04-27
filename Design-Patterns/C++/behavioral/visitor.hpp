#ifndef VISITOR_HPP
#define VISITOR_HPP

#include <iostream>
#include <string>
#include <memory>
#include <vector>

// Предварительное объявление классов
class ConcreteElementA;
class ConcreteElementB;

/**
 * @class Visitor
 * @brief Базовый класс посетителя.
 */
class Visitor {
public:
    virtual ~Visitor() = default;
    virtual void visitConcreteElementA(std::shared_ptr<ConcreteElementA> element) = 0;
    virtual void visitConcreteElementB(std::shared_ptr<ConcreteElementB> element) = 0;
};

/**
 * @class Element
 * @brief Базовый класс элемента.
 */
class Element {
public:
    virtual ~Element() = default;
    virtual void accept(std::shared_ptr<Visitor> visitor) = 0;
};

/**
 * @class ConcreteElementA
 * @brief Конкретный элемент A.
 */
class ConcreteElementA : public Element {
public:
    void accept(std::shared_ptr<Visitor> visitor) override {
        visitor->visitConcreteElementA(shared_from_this());
    }

    void operationA() {
        std::cout << "Операция A" << std::endl;
    }
};

/**
 * @class ConcreteElementB
 * @brief Конкретный элемент B.
 */
class ConcreteElementB : public Element {
public:
    void accept(std::shared_ptr<Visitor> visitor) override {
        visitor->visitConcreteElementB(shared_from_this());
    }

    void operationB() {
        std::cout << "Операция B" << std::endl;
    }
};

/**
 * @class ConcreteVisitor
 * @brief Конкретный посетитель.
 */
class ConcreteVisitor : public Visitor {
public:
    void visitConcreteElementA(std::shared_ptr<ConcreteElementA> element) override {
        std::cout << "Посетитель посещает элемент A" << std::endl;
        element->operationA();
    }

    void visitConcreteElementB(std::shared_ptr<ConcreteElementB> element) override {
        std::cout << "Посетитель посещает элемент B" << std::endl;
        element->operationB();
    }
};

/**
 * @class ObjectStructure
 * @brief Структура объектов.
 */
class ObjectStructure {
private:
    std::vector<std::shared_ptr<Element>> elements;

public:
    void attach(std::shared_ptr<Element> element) {
        elements.push_back(element);
    }

    void detach(std::shared_ptr<Element> element) {
        auto it = std::find(elements.begin(), elements.end(), element);
        if (it != elements.end()) {
            elements.erase(it);
        }
    }

    void accept(std::shared_ptr<Visitor> visitor) {
        for (const auto& element : elements) {
            element->accept(visitor);
        }
    }
};

#endif // VISITOR_HPP 