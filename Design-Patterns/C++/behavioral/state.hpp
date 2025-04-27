#ifndef STATE_HPP
#define STATE_HPP

#include <iostream>
#include <string>
#include <memory>

/**
 * @class State
 * @brief Базовый класс состояния.
 */
class State {
public:
    virtual ~State() = default;
    virtual void handle() = 0;
};

/**
 * @class Context
 * @brief Контекст.
 */
class Context {
private:
    std::shared_ptr<State> state;

public:
    Context(std::shared_ptr<State> state) : state(state) {}

    void setState(std::shared_ptr<State> newState) {
        state = newState;
    }

    void request() {
        state->handle();
    }
};

/**
 * @class ConcreteStateA
 * @brief Конкретное состояние A.
 */
class ConcreteStateA : public State {
public:
    void handle() override {
        std::cout << "Обработка в состоянии A" << std::endl;
    }
};

/**
 * @class ConcreteStateB
 * @brief Конкретное состояние B.
 */
class ConcreteStateB : public State {
public:
    void handle() override {
        std::cout << "Обработка в состоянии B" << std::endl;
    }
};

#endif // STATE_HPP 