#ifndef FLYWEIGHT_HPP
#define FLYWEIGHT_HPP

#include <iostream>
#include <string>
#include <unordered_map>
#include <memory>

/**
 * @class Flyweight
 * @brief Базовый класс легковеса.
 */
class Flyweight {
public:
    virtual ~Flyweight() = default;
    virtual void operation(const std::string& extrinsicState) const = 0;
};

/**
 * @class ConcreteFlyweight
 * @brief Конкретный легковес.
 */
class ConcreteFlyweight : public Flyweight {
private:
    std::string intrinsicState;

public:
    ConcreteFlyweight(const std::string& state) : intrinsicState(state) {}

    void operation(const std::string& extrinsicState) const override {
        std::cout << "ConcreteFlyweight: внутреннее состояние = " << intrinsicState
                  << ", внешнее состояние = " << extrinsicState << std::endl;
    }
};

/**
 * @class FlyweightFactory
 * @brief Фабрика легковесов.
 */
class FlyweightFactory {
private:
    std::unordered_map<std::string, std::shared_ptr<Flyweight>> flyweights;

public:
    std::shared_ptr<Flyweight> getFlyweight(const std::string& key) {
        if (flyweights.find(key) == flyweights.end()) {
            flyweights[key] = std::make_shared<ConcreteFlyweight>(key);
        }
        return flyweights[key];
    }

    void listFlyweights() const {
        std::cout << "FlyweightFactory: у меня " << flyweights.size() << " легковесов:" << std::endl;
        for (const auto& pair : flyweights) {
            std::cout << pair.first << std::endl;
        }
    }
};

#endif // FLYWEIGHT_HPP 