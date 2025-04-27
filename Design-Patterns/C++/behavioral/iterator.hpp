#ifndef ITERATOR_HPP
#define ITERATOR_HPP

#include <iostream>
#include <string>
#include <vector>
#include <memory>

/**
 * @class Iterator
 * @brief Базовый класс итератора.
 */
template<typename T>
class Iterator {
public:
    virtual ~Iterator() = default;
    virtual T next() = 0;
    virtual bool hasNext() const = 0;
};

/**
 * @class Container
 * @brief Базовый класс контейнера.
 */
template<typename T>
class Container {
public:
    virtual ~Container() = default;
    virtual std::shared_ptr<Iterator<T>> getIterator() = 0;
};

/**
 * @class ConcreteContainer
 * @brief Конкретный контейнер.
 */
template<typename T>
class ConcreteContainer : public Container<T> {
private:
    std::vector<T> items;

public:
    void addItem(const T& item) {
        items.push_back(item);
    }

    std::shared_ptr<Iterator<T>> getIterator() override {
        return std::make_shared<ConcreteIterator<T>>(items);
    }
};

/**
 * @class ConcreteIterator
 * @brief Конкретный итератор.
 */
template<typename T>
class ConcreteIterator : public Iterator<T> {
private:
    std::vector<T> items;
    size_t position;

public:
    ConcreteIterator(const std::vector<T>& items) : items(items), position(0) {}

    T next() override {
        if (hasNext()) {
            return items[position++];
        }
        throw std::out_of_range("No more items");
    }

    bool hasNext() const override {
        return position < items.size();
    }
};

#endif // ITERATOR_HPP 