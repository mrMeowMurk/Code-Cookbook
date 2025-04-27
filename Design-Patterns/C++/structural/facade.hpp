#ifndef FACADE_HPP
#define FACADE_HPP

#include <iostream>
#include <string>

/**
 * @class SubsystemA
 * @brief Подсистема A.
 */
class SubsystemA {
public:
    std::string operationA() const {
        return "SubsystemA: операция A";
    }
};

/**
 * @class SubsystemB
 * @brief Подсистема B.
 */
class SubsystemB {
public:
    std::string operationB() const {
        return "SubsystemB: операция B";
    }
};

/**
 * @class SubsystemC
 * @brief Подсистема C.
 */
class SubsystemC {
public:
    std::string operationC() const {
        return "SubsystemC: операция C";
    }
};

/**
 * @class Facade
 * @brief Фасад, предоставляющий упрощенный интерфейс к подсистемам.
 */
class Facade {
private:
    SubsystemA* subsystemA;
    SubsystemB* subsystemB;
    SubsystemC* subsystemC;

public:
    Facade() {
        subsystemA = new SubsystemA();
        subsystemB = new SubsystemB();
        subsystemC = new SubsystemC();
    }

    ~Facade() {
        delete subsystemA;
        delete subsystemB;
        delete subsystemC;
    }

    std::string operation() const {
        std::string result = "Facade инициализирует подсистемы:\n";
        result += subsystemA->operationA() + "\n";
        result += subsystemB->operationB() + "\n";
        result += subsystemC->operationC();
        return result;
    }
};

#endif // FACADE_HPP 