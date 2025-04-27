#ifndef MEMENTO_HPP
#define MEMENTO_HPP

#include <iostream>
#include <string>
#include <memory>
#include <vector>

/**
 * @class Memento
 * @brief Хранитель.
 */
class Memento {
private:
    std::string state;

public:
    Memento(const std::string& state) : state(state) {}

    std::string getState() const {
        return state;
    }
};

/**
 * @class Originator
 * @brief Создатель.
 */
class Originator {
private:
    std::string state;

public:
    void setState(const std::string& state) {
        this->state = state;
    }

    std::string getState() const {
        return state;
    }

    std::shared_ptr<Memento> saveStateToMemento() {
        return std::make_shared<Memento>(state);
    }

    void getStateFromMemento(std::shared_ptr<Memento> memento) {
        state = memento->getState();
    }
};

/**
 * @class CareTaker
 * @brief Опекун.
 */
class CareTaker {
private:
    std::vector<std::shared_ptr<Memento>> mementoList;

public:
    void add(std::shared_ptr<Memento> state) {
        mementoList.push_back(state);
    }

    std::shared_ptr<Memento> get(size_t index) {
        if (index < mementoList.size()) {
            return mementoList[index];
        }
        return nullptr;
    }
};

#endif // MEMENTO_HPP 