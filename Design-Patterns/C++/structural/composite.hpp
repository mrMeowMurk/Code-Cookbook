#ifndef COMPOSITE_HPP
#define COMPOSITE_HPP

#include <iostream>
#include <string>
#include <vector>
#include <memory>

/**
 * @class Component
 * @brief Базовый класс компонента.
 */
class Component {
public:
    virtual ~Component() = default;
    virtual void operation() const = 0;
    virtual void add(std::shared_ptr<Component> component) {}
    virtual void remove(std::shared_ptr<Component> component) {}
    virtual std::shared_ptr<Component> getChild(int index) const { return nullptr; }
};

/**
 * @class Leaf
 * @brief Конечный компонент, не имеющий дочерних элементов.
 */
class Leaf : public Component {
private:
    std::string name;

public:
    Leaf(const std::string& name) : name(name) {}

    void operation() const override {
        std::cout << "Leaf: " << name << " выполняет операцию" << std::endl;
    }
};

/**
 * @class Composite
 * @brief Составной компонент, содержащий дочерние элементы.
 */
class Composite : public Component {
private:
    std::vector<std::shared_ptr<Component>> children;
    std::string name;

public:
    Composite(const std::string& name) : name(name) {}

    void operation() const override {
        std::cout << "Composite: " << name << " выполняет операцию" << std::endl;
        for (const auto& child : children) {
            child->operation();
        }
    }

    void add(std::shared_ptr<Component> component) override {
        children.push_back(component);
    }

    void remove(std::shared_ptr<Component> component) override {
        auto it = std::find(children.begin(), children.end(), component);
        if (it != children.end()) {
            children.erase(it);
        }
    }

    std::shared_ptr<Component> getChild(int index) const override {
        if (index >= 0 && index < children.size()) {
            return children[index];
        }
        return nullptr;
    }
};

#endif // COMPOSITE_HPP 