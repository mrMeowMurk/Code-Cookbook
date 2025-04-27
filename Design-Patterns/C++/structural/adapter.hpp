#ifndef ADAPTER_HPP
#define ADAPTER_HPP

#include <iostream>
#include <string>

/**
 * @class Target
 * @brief Целевой интерфейс, который ожидает клиент.
 */
class Target {
public:
    virtual ~Target() = default;
    virtual std::string request() const {
        return "Target: стандартный запрос";
    }
};

/**
 * @class Adaptee
 * @brief Адаптируемый класс с несовместимым интерфейсом.
 */
class Adaptee {
public:
    std::string specificRequest() const {
        return "Adaptee: специфический запрос";
    }
};

/**
 * @class Adapter
 * @brief Адаптер, который делает интерфейс Adaptee совместимым с Target.
 */
class Adapter : public Target {
private:
    Adaptee* adaptee;

public:
    Adapter(Adaptee* a) : adaptee(a) {}

    std::string request() const override {
        std::string result = adaptee->specificRequest();
        return "Adapter: (переведено) " + result;
    }
};

#endif // ADAPTER_HPP 