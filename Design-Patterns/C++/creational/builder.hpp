#ifndef BUILDER_HPP
#define BUILDER_HPP

#include <iostream>
#include <string>
#include <vector>
#include <memory>

/**
 * @class Computer
 * @brief Класс продукта - компьютер.
 */
class Computer {
private:
    std::vector<std::string> parts;

public:
    void add(const std::string& part) {
        parts.push_back(part);
    }

    std::string listParts() const {
        std::string result = "Части компьютера: ";
        for (size_t i = 0; i < parts.size(); ++i) {
            result += parts[i];
            if (i < parts.size() - 1) {
                result += ", ";
            }
        }
        return result;
    }
};

/**
 * @class ComputerBuilder
 * @brief Абстрактный класс строителя.
 * 
 * Определяет общий интерфейс для создания различных частей продукта.
 */
class ComputerBuilder {
public:
    virtual ~ComputerBuilder() = default;
    
    virtual void reset() = 0;
    virtual void setCpu() = 0;
    virtual void setMemory() = 0;
    virtual void setStorage() = 0;
    virtual void setGraphics() = 0;
    virtual Computer getResult() = 0;
};

/**
 * @class GamingComputerBuilder
 * @brief Конкретный строитель для игрового компьютера.
 */
class GamingComputerBuilder : public ComputerBuilder {
private:
    Computer computer;

public:
    void reset() override {
        computer = Computer();
    }

    void setCpu() override {
        computer.add("Intel Core i9-13900K");
    }

    void setMemory() override {
        computer.add("64GB DDR5 RAM");
    }

    void setStorage() override {
        computer.add("2TB NVMe SSD");
    }

    void setGraphics() override {
        computer.add("NVIDIA RTX 4090");
    }

    Computer getResult() override {
        return computer;
    }
};

/**
 * @class OfficeComputerBuilder
 * @brief Конкретный строитель для офисного компьютера.
 */
class OfficeComputerBuilder : public ComputerBuilder {
private:
    Computer computer;

public:
    void reset() override {
        computer = Computer();
    }

    void setCpu() override {
        computer.add("Intel Core i5-12400");
    }

    void setMemory() override {
        computer.add("16GB DDR4 RAM");
    }

    void setStorage() override {
        computer.add("512GB SSD");
    }

    void setGraphics() override {
        computer.add("Intel UHD Graphics 730");
    }

    Computer getResult() override {
        return computer;
    }
};

/**
 * @class Director
 * @brief Класс директора, который управляет процессом строительства.
 */
class Director {
private:
    ComputerBuilder* builder;

public:
    void setBuilder(ComputerBuilder* b) {
        builder = b;
    }

    void buildMinimalComputer() {
        builder->reset();
        builder->setCpu();
        builder->setMemory();
        builder->setStorage();
    }

    void buildFullComputer() {
        builder->reset();
        builder->setCpu();
        builder->setMemory();
        builder->setStorage();
        builder->setGraphics();
    }
};

#endif // BUILDER_HPP 