#ifndef OBSERVER_HPP
#define OBSERVER_HPP

#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <algorithm>

/**
 * @class Observer
 * @brief Базовый класс наблюдателя.
 */
class Observer {
public:
    virtual ~Observer() = default;
    virtual void update(const std::string& message) = 0;
};

/**
 * @class Subject
 * @brief Базовый класс субъекта.
 */
class Subject {
private:
    std::vector<std::shared_ptr<Observer>> observers;
    std::string message;

public:
    void attach(std::shared_ptr<Observer> observer) {
        observers.push_back(observer);
    }

    void detach(std::shared_ptr<Observer> observer) {
        auto it = std::find(observers.begin(), observers.end(), observer);
        if (it != observers.end()) {
            observers.erase(it);
        }
    }

    void notify() {
        for (const auto& observer : observers) {
            observer->update(message);
        }
    }

    void setMessage(const std::string& message) {
        this->message = message;
        notify();
    }
};

/**
 * @class ConcreteObserver
 * @brief Конкретный наблюдатель.
 */
class ConcreteObserver : public Observer {
private:
    std::string name;

public:
    ConcreteObserver(const std::string& name) : name(name) {}

    void update(const std::string& message) override {
        std::cout << "Observer " << name << " получил сообщение: " << message << std::endl;
    }
};

#endif // OBSERVER_HPP 