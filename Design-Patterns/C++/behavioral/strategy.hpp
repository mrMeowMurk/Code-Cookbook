#ifndef STRATEGY_HPP
#define STRATEGY_HPP

#include <iostream>
#include <string>
#include <memory>

/**
 * @class Strategy
 * @brief Базовый класс стратегии.
 */
class Strategy {
public:
    virtual ~Strategy() = default;
    virtual void algorithmInterface() = 0;
};

/**
 * @class ConcreteStrategyA
 * @brief Конкретная стратегия A.
 */
class ConcreteStrategyA : public Strategy {
public:
    void algorithmInterface() override {
        std::cout << "Реализация алгоритма A" << std::endl;
    }
};

/**
 * @class ConcreteStrategyB
 * @brief Конкретная стратегия B.
 */
class ConcreteStrategyB : public Strategy {
public:
    void algorithmInterface() override {
        std::cout << "Реализация алгоритма B" << std::endl;
    }
};

/**
 * @class Context
 * @brief Контекст.
 */
class Context {
private:
    std::shared_ptr<Strategy> strategy;

public:
    Context(std::shared_ptr<Strategy> strategy) : strategy(strategy) {}

    void setStrategy(std::shared_ptr<Strategy> newStrategy) {
        strategy = newStrategy;
    }

    void contextInterface() {
        strategy->algorithmInterface();
    }
};

#endif // STRATEGY_HPP 