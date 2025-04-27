#ifndef PROTOTYPE_HPP
#define PROTOTYPE_HPP

#include <iostream>
#include <string>
#include <memory>

/**
 * @class Prototype
 * @brief Базовый класс прототипа.
 * 
 * Определяет интерфейс для клонирования объектов.
 */
class Prototype {
public:
    virtual ~Prototype() = default;
    virtual std::unique_ptr<Prototype> clone() const = 0;
    virtual void print() const = 0;
};

/**
 * @class ConcretePrototype
 * @brief Конкретный класс прототипа.
 * 
 * Реализует операцию клонирования.
 */
class ConcretePrototype : public Prototype {
private:
    std::string name;
    int value;

public:
    ConcretePrototype(const std::string& name, int value)
        : name(name), value(value) {}

    std::unique_ptr<Prototype> clone() const override {
        return std::make_unique<ConcretePrototype>(*this);
    }

    void print() const override {
        std::cout << "ConcretePrototype: " << name << ", value: " << value << std::endl;
    }
};

/**
 * @class PrototypeRegistry
 * @brief Реестр прототипов.
 * 
 * Хранит и управляет прототипами.
 */
class PrototypeRegistry {
private:
    std::unique_ptr<Prototype> prototype;

public:
    void setPrototype(std::unique_ptr<Prototype> p) {
        prototype = std::move(p);
    }

    std::unique_ptr<Prototype> createClone() const {
        if (prototype) {
            return prototype->clone();
        }
        return nullptr;
    }
};

#endif // PROTOTYPE_HPP 