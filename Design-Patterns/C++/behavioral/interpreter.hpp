#ifndef INTERPRETER_HPP
#define INTERPRETER_HPP

#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <map>

/**
 * @class Expression
 * @brief Базовый класс выражения.
 */
class Expression {
public:
    virtual ~Expression() = default;
    virtual bool interpret(const std::string& context) = 0;
};

/**
 * @class TerminalExpression
 * @brief Терминальное выражение.
 */
class TerminalExpression : public Expression {
private:
    std::string data;

public:
    TerminalExpression(const std::string& data) : data(data) {}

    bool interpret(const std::string& context) override {
        return context.find(data) != std::string::npos;
    }
};

/**
 * @class OrExpression
 * @brief Выражение ИЛИ.
 */
class OrExpression : public Expression {
private:
    std::shared_ptr<Expression> expr1;
    std::shared_ptr<Expression> expr2;

public:
    OrExpression(std::shared_ptr<Expression> expr1, std::shared_ptr<Expression> expr2)
        : expr1(expr1), expr2(expr2) {}

    bool interpret(const std::string& context) override {
        return expr1->interpret(context) || expr2->interpret(context);
    }
};

/**
 * @class AndExpression
 * @brief Выражение И.
 */
class AndExpression : public Expression {
private:
    std::shared_ptr<Expression> expr1;
    std::shared_ptr<Expression> expr2;

public:
    AndExpression(std::shared_ptr<Expression> expr1, std::shared_ptr<Expression> expr2)
        : expr1(expr1), expr2(expr2) {}

    bool interpret(const std::string& context) override {
        return expr1->interpret(context) && expr2->interpret(context);
    }
};

#endif // INTERPRETER_HPP 