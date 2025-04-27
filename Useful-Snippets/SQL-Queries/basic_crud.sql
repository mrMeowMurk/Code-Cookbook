-- Создание таблицы пользователей
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создание таблицы заказов
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    total_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создание таблицы товаров
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создание таблицы заказов-товаров (связь многие-ко-многим)
CREATE TABLE order_items (
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (order_id, product_id)
);

-- Создание индексов
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);

-- Вставка данных (INSERT)
INSERT INTO users (username, email, password_hash)
VALUES 
    ('john_doe', 'john@example.com', 'hashed_password_1'),
    ('jane_smith', 'jane@example.com', 'hashed_password_2');

INSERT INTO products (name, description, price, stock)
VALUES 
    ('Laptop', 'High-performance laptop', 999.99, 10),
    ('Smartphone', 'Latest smartphone model', 699.99, 15);

-- Чтение данных (SELECT)
-- Получение всех пользователей
SELECT * FROM users;

-- Получение пользователя по email
SELECT * FROM users WHERE email = 'john@example.com';

-- Получение товаров с ценой выше 500
SELECT name, price FROM products WHERE price > 500;

-- Получение заказов пользователя с информацией о товарах
SELECT 
    o.id as order_id,
    o.total_amount,
    o.status,
    p.name as product_name,
    oi.quantity,
    oi.price as item_price
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
WHERE o.user_id = 1;

-- Обновление данных (UPDATE)
-- Обновление цены товара
UPDATE products 
SET price = 899.99, updated_at = CURRENT_TIMESTAMP
WHERE id = 1;

-- Обновление статуса заказа
UPDATE orders 
SET status = 'completed', updated_at = CURRENT_TIMESTAMP
WHERE id = 1;

-- Удаление данных (DELETE)
-- Удаление товара
DELETE FROM products WHERE id = 1;

-- Удаление пользователя (с проверкой на существование заказов)
DELETE FROM users 
WHERE id = 1 
AND NOT EXISTS (SELECT 1 FROM orders WHERE user_id = 1);

-- Агрегация данных
-- Подсчет количества товаров
SELECT COUNT(*) as total_products FROM products;

-- Средняя цена товаров
SELECT AVG(price) as average_price FROM products;

-- Сумма заказов по пользователям
SELECT 
    u.username,
    COUNT(o.id) as total_orders,
    SUM(o.total_amount) as total_spent
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.username;

-- Сортировка и ограничение
-- Топ-5 самых дорогих товаров
SELECT name, price 
FROM products 
ORDER BY price DESC 
LIMIT 5;

-- Последние 10 заказов
SELECT o.*, u.username
FROM orders o
JOIN users u ON o.user_id = u.id
ORDER BY o.created_at DESC
LIMIT 10;

-- Поиск по шаблону
-- Поиск товаров по названию
SELECT * FROM products 
WHERE name ILIKE '%phone%';

-- Поиск пользователей по email
SELECT * FROM users 
WHERE email ILIKE '%@gmail.com';

-- Объединение таблиц
-- Полная информация о заказе
SELECT 
    o.id as order_id,
    u.username,
    u.email,
    o.total_amount,
    o.status,
    p.name as product_name,
    oi.quantity,
    oi.price as item_price
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
WHERE o.id = 1;

-- Подзапросы
-- Товары, которые никогда не заказывались
SELECT * FROM products p
WHERE NOT EXISTS (
    SELECT 1 FROM order_items oi WHERE oi.product_id = p.id
);

-- Пользователи, сделавшие заказы на сумму больше 1000
SELECT u.*
FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders o 
    WHERE o.user_id = u.id AND o.total_amount > 1000
);

-- Транзакции
BEGIN;
    -- Вставка данных
    INSERT INTO users (username, email, password_hash)
    VALUES ('alice', 'alice@example.com', 'hash4');
    
    -- Обновление данных
    UPDATE users 
    SET email = 'new_alice@example.com'
    WHERE username = 'alice';
    
    -- Если все операции успешны, подтверждаем транзакцию
    COMMIT;
    
    -- Если произошла ошибка, отменяем транзакцию
    -- ROLLBACK;

-- Ограничения
-- Добавление ограничения NOT NULL
ALTER TABLE users 
ALTER COLUMN username SET NOT NULL;

-- Добавление ограничения UNIQUE
ALTER TABLE users 
ADD CONSTRAINT unique_email UNIQUE (email);

-- Добавление ограничения CHECK
ALTER TABLE users 
ADD CONSTRAINT check_username_length 
CHECK (length(username) >= 3);

-- Добавление внешнего ключа
CREATE TABLE user_profiles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    full_name VARCHAR(100),
    bio TEXT
); 