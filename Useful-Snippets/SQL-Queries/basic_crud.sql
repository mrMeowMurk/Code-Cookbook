-- Создание таблицы
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создание индексов
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);

-- Вставка данных (Create)
INSERT INTO users (username, email, password_hash)
VALUES 
    ('john_doe', 'john@example.com', 'hash1'),
    ('jane_smith', 'jane@example.com', 'hash2'),
    ('bob_johnson', 'bob@example.com', 'hash3');

-- Выборка данных (Read)
-- Получение всех пользователей
SELECT * FROM users;

-- Получение пользователя по ID
SELECT * FROM users WHERE id = 1;

-- Получение пользователя по username
SELECT * FROM users WHERE username = 'john_doe';

-- Получение пользователя по email
SELECT * FROM users WHERE email = 'john@example.com';

-- Получение пользователей, созданных после определенной даты
SELECT * FROM users WHERE created_at > '2023-01-01';

-- Получение количества пользователей
SELECT COUNT(*) FROM users;

-- Получение пользователей с сортировкой
SELECT * FROM users ORDER BY created_at DESC;

-- Получение пользователей с ограничением
SELECT * FROM users LIMIT 10 OFFSET 0;

-- Обновление данных (Update)
-- Обновление одного поля
UPDATE users 
SET email = 'new_email@example.com'
WHERE id = 1;

-- Обновление нескольких полей
UPDATE users 
SET 
    username = 'new_username',
    email = 'new_email@example.com',
    updated_at = CURRENT_TIMESTAMP
WHERE id = 1;

-- Обновление всех записей
UPDATE users 
SET updated_at = CURRENT_TIMESTAMP;

-- Удаление данных (Delete)
-- Удаление одной записи
DELETE FROM users WHERE id = 1;

-- Удаление нескольких записей
DELETE FROM users WHERE created_at < '2023-01-01';

-- Удаление всех записей
DELETE FROM users;

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