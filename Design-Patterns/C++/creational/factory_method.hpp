#ifndef FACTORY_METHOD_HPP
#define FACTORY_METHOD_HPP

#include <iostream>
#include <string>
#include <memory>

/**
 * @class Document
 * @brief Абстрактный класс документа.
 * 
 * Определяет интерфейс для всех типов документов.
 */
class Document {
public:
    virtual ~Document() = default;
    
    virtual std::string create() = 0;
    virtual std::string open() = 0;
    virtual std::string save() = 0;
};

/**
 * @class TextDocument
 * @brief Конкретный класс текстового документа.
 */
class TextDocument : public Document {
public:
    std::string create() override {
        return "Создание текстового документа";
    }
    
    std::string open() override {
        return "Открытие текстового документа";
    }
    
    std::string save() override {
        return "Сохранение текстового документа";
    }
};

/**
 * @class SpreadsheetDocument
 * @brief Конкретный класс табличного документа.
 */
class SpreadsheetDocument : public Document {
public:
    std::string create() override {
        return "Создание табличного документа";
    }
    
    std::string open() override {
        return "Открытие табличного документа";
    }
    
    std::string save() override {
        return "Сохранение табличного документа";
    }
};

/**
 * @class Application
 * @brief Абстрактный класс приложения.
 * 
 * Определяет фабричный метод для создания документов.
 */
class Application {
public:
    virtual ~Application() = default;
    
    /**
     * @brief Фабричный метод для создания документа.
     * 
     * @return std::unique_ptr<Document> Созданный документ
     */
    virtual std::unique_ptr<Document> createDocument() = 0;
    
    /**
     * @brief Создание нового документа.
     * 
     * @return std::string Результат создания документа
     */
    std::string newDocument() {
        auto doc = createDocument();
        return doc->create();
    }
};

/**
 * @class TextEditor
 * @brief Конкретный класс текстового редактора.
 */
class TextEditor : public Application {
public:
    std::unique_ptr<Document> createDocument() override {
        return std::make_unique<TextDocument>();
    }
};

/**
 * @class SpreadsheetEditor
 * @brief Конкретный класс редактора таблиц.
 */
class SpreadsheetEditor : public Application {
public:
    std::unique_ptr<Document> createDocument() override {
        return std::make_unique<SpreadsheetDocument>();
    }
};

#endif // FACTORY_METHOD_HPP 