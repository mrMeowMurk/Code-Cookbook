#ifndef ABSTRACT_FACTORY_HPP
#define ABSTRACT_FACTORY_HPP

#include <iostream>
#include <string>
#include <memory>

/**
 * @class Button
 * @brief Абстрактный класс кнопки.
 * 
 * Определяет интерфейс для всех типов кнопок.
 */
class Button {
public:
    virtual ~Button() = default;
    
    virtual std::string render() = 0;
    virtual std::string click() = 0;
};

/**
 * @class TextBox
 * @brief Абстрактный класс текстового поля.
 * 
 * Определяет интерфейс для всех типов текстовых полей.
 */
class TextBox {
public:
    virtual ~TextBox() = default;
    
    virtual std::string render() = 0;
    virtual std::string input(const std::string& text) = 0;
};

/**
 * @class WindowsButton
 * @brief Конкретный класс кнопки для Windows.
 */
class WindowsButton : public Button {
public:
    std::string render() override {
        return "Отрисовка кнопки в стиле Windows";
    }
    
    std::string click() override {
        return "Обработка клика по кнопке Windows";
    }
};

/**
 * @class WindowsTextBox
 * @brief Конкретный класс текстового поля для Windows.
 */
class WindowsTextBox : public TextBox {
public:
    std::string render() override {
        return "Отрисовка текстового поля в стиле Windows";
    }
    
    std::string input(const std::string& text) override {
        return "Ввод текста в текстовое поле Windows: " + text;
    }
};

/**
 * @class MacButton
 * @brief Конкретный класс кнопки для Mac.
 */
class MacButton : public Button {
public:
    std::string render() override {
        return "Отрисовка кнопки в стиле Mac";
    }
    
    std::string click() override {
        return "Обработка клика по кнопке Mac";
    }
};

/**
 * @class MacTextBox
 * @brief Конкретный класс текстового поля для Mac.
 */
class MacTextBox : public TextBox {
public:
    std::string render() override {
        return "Отрисовка текстового поля в стиле Mac";
    }
    
    std::string input(const std::string& text) override {
        return "Ввод текста в текстовое поле Mac: " + text;
    }
};

/**
 * @class GUIFactory
 * @brief Абстрактная фабрика GUI элементов.
 * 
 * Определяет интерфейс для создания семейства связанных объектов.
 */
class GUIFactory {
public:
    virtual ~GUIFactory() = default;
    
    virtual std::unique_ptr<Button> createButton() = 0;
    virtual std::unique_ptr<TextBox> createTextBox() = 0;
};

/**
 * @class WindowsFactory
 * @brief Конкретная фабрика для создания GUI элементов в стиле Windows.
 */
class WindowsFactory : public GUIFactory {
public:
    std::unique_ptr<Button> createButton() override {
        return std::make_unique<WindowsButton>();
    }
    
    std::unique_ptr<TextBox> createTextBox() override {
        return std::make_unique<WindowsTextBox>();
    }
};

/**
 * @class MacFactory
 * @brief Конкретная фабрика для создания GUI элементов в стиле Mac.
 */
class MacFactory : public GUIFactory {
public:
    std::unique_ptr<Button> createButton() override {
        return std::make_unique<MacButton>();
    }
    
    std::unique_ptr<TextBox> createTextBox() override {
        return std::make_unique<MacTextBox>();
    }
};

/**
 * @class Application
 * @brief Класс приложения, использующий абстрактную фабрику.
 */
class Application {
private:
    std::unique_ptr<GUIFactory> factory;
    std::unique_ptr<Button> button;
    std::unique_ptr<TextBox> textbox;

public:
    explicit Application(std::unique_ptr<GUIFactory> f) : factory(std::move(f)) {}
    
    void createUI() {
        button = factory->createButton();
        textbox = factory->createTextBox();
    }
    
    void renderUI() {
        std::cout << button->render() << std::endl;
        std::cout << textbox->render() << std::endl;
    }
    
    void interact() {
        std::cout << button->click() << std::endl;
        std::cout << textbox->input("Hello, World!") << std::endl;
    }
};

#endif // ABSTRACT_FACTORY_HPP 