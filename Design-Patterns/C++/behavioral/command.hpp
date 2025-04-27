#ifndef COMMAND_HPP
#define COMMAND_HPP

#include <iostream>
#include <string>
#include <memory>
#include <vector>

/**
 * @class Command
 * @brief Базовый класс команды.
 */
class Command {
public:
    virtual ~Command() = default;
    virtual void execute() const = 0;
};

/**
 * @class Receiver
 * @brief Получатель команды.
 */
class Receiver {
public:
    void doSomething(const std::string& a) {
        std::cout << "Receiver: работаю с " << a << std::endl;
    }

    void doSomethingElse(const std::string& b) {
        std::cout << "Receiver: также работаю с " << b << std::endl;
    }
};

/**
 * @class SimpleCommand
 * @brief Простая команда.
 */
class SimpleCommand : public Command {
private:
    std::string payLoad;

public:
    SimpleCommand(const std::string& payLoad) : payLoad(payLoad) {}

    void execute() const override {
        std::cout << "SimpleCommand: вижу, вы хотите, чтобы я сделал что-то простое (" << payLoad << ")" << std::endl;
    }
};

/**
 * @class ComplexCommand
 * @brief Сложная команда.
 */
class ComplexCommand : public Command {
private:
    std::shared_ptr<Receiver> receiver;
    std::string a;
    std::string b;

public:
    ComplexCommand(std::shared_ptr<Receiver> receiver, const std::string& a, const std::string& b)
        : receiver(receiver), a(a), b(b) {}

    void execute() const override {
        std::cout << "ComplexCommand: сложные вещи должны выполняться получателем" << std::endl;
        receiver->doSomething(a);
        receiver->doSomethingElse(b);
    }
};

/**
 * @class Invoker
 * @brief Вызывающий.
 */
class Invoker {
private:
    std::vector<std::shared_ptr<Command>> onStart;
    std::vector<std::shared_ptr<Command>> onFinish;

public:
    void setOnStart(std::shared_ptr<Command> command) {
        onStart.push_back(command);
    }

    void setOnFinish(std::shared_ptr<Command> command) {
        onFinish.push_back(command);
    }

    void doSomethingImportant() {
        std::cout << "Invoker: кто-то хочет сделать что-то до того, как я начну?" << std::endl;
        for (const auto& command : onStart) {
            command->execute();
        }

        std::cout << "Invoker: ...делаю что-то действительно важное..." << std::endl;

        std::cout << "Invoker: кто-то хочет сделать что-то после того, как я закончу?" << std::endl;
        for (const auto& command : onFinish) {
            command->execute();
        }
    }
};

#endif // COMMAND_HPP 