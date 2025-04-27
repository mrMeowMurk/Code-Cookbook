-- Оптимизация SQL-запросов и баз данных

-- 1. Индексы
-- Создание индексов для часто используемых полей поиска
CREATE INDEX idx_products_name ON products(name);
CREATE INDEX idx_products_price ON products(price);
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);

-- Составной индекс для полей, которые часто используются вместе
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

-- Частичный индекс для часто используемых условий
CREATE INDEX idx_active_orders ON orders(status) WHERE status = 'active';

-- 2. Оптимизация запросов
-- Использование EXPLAIN для анализа плана выполнения
EXPLAIN ANALYZE SELECT * FROM products WHERE price > 500;

-- Оптимизация JOIN операций
-- Плохой запрос (может быть неэффективным)
SELECT * FROM orders o
JOIN users u ON o.user_id = u.id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id;

-- Оптимизированный запрос (выбираем только нужные поля)
SELECT 
    o.id,
    u.username,
    p.name,
    oi.quantity
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id;

-- 3. Партиционирование таблиц
-- Создание партиционированной таблицы по дате
CREATE TABLE orders_partitioned (
    id SERIAL,
    user_id INTEGER,
    total_amount DECIMAL(10, 2),
    status VARCHAR(20),
    created_at TIMESTAMP
) PARTITION BY RANGE (created_at);

-- Создание партиций по месяцам
CREATE TABLE orders_2023_01 PARTITION OF orders_partitioned
    FOR VALUES FROM ('2023-01-01') TO ('2023-02-01');
CREATE TABLE orders_2023_02 PARTITION OF orders_partitioned
    FOR VALUES FROM ('2023-02-01') TO ('2023-03-01');

-- 4. Материализованные представления
-- Создание материализованного представления для часто используемых агрегаций
CREATE MATERIALIZED VIEW product_sales_summary AS
SELECT 
    p.id,
    p.name,
    COUNT(oi.order_id) as total_orders,
    SUM(oi.quantity) as total_quantity,
    SUM(oi.quantity * oi.price) as total_revenue
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.id, p.name;

-- Обновление материализованного представления
REFRESH MATERIALIZED VIEW product_sales_summary;

-- 5. Кэширование запросов
-- Создание функции с кэшированием результатов
CREATE OR REPLACE FUNCTION get_user_orders(user_id INTEGER)
RETURNS TABLE (
    order_id INTEGER,
    total_amount DECIMAL,
    status VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT o.id, o.total_amount, o.status
    FROM orders o
    WHERE o.user_id = get_user_orders.user_id;
END;
$$ LANGUAGE plpgsql;

-- 6. Оптимизация условий WHERE
-- Плохой запрос (использует функции в условии)
SELECT * FROM products 
WHERE LOWER(name) = 'laptop';

-- Оптимизированный запрос (использует индекс)
SELECT * FROM products 
WHERE name ILIKE 'laptop';

-- 7. Ограничение выборки
-- Использование LIMIT и OFFSET для пагинации
SELECT * FROM products 
ORDER BY created_at DESC 
LIMIT 10 OFFSET 0;

-- 8. Оптимизация обновлений
-- Пакетное обновление вместо множества одиночных
UPDATE products 
SET price = CASE 
    WHEN id = 1 THEN 899.99
    WHEN id = 2 THEN 799.99
    ELSE price
END
WHERE id IN (1, 2);

-- 9. Мониторинг производительности
-- Просмотр статистики использования индексов
SELECT 
    schemaname,
    relname,
    indexrelname,
    idx_scan,
    idx_tup_read,
    idx_tup_fetch
FROM pg_stat_user_indexes;

-- Просмотр статистики таблиц
SELECT 
    schemaname,
    relname,
    seq_scan,
    seq_tup_read,
    idx_scan,
    idx_tup_fetch
FROM pg_stat_user_tables;

-- 10. Оптимизация конфигурации
-- Настройка параметров PostgreSQL для оптимизации
ALTER SYSTEM SET shared_buffers = '1GB';
ALTER SYSTEM SET work_mem = '64MB';
ALTER SYSTEM SET maintenance_work_mem = '256MB';
ALTER SYSTEM SET effective_cache_size = '4GB';

-- 11. Очистка и обслуживание
-- Анализ таблиц для обновления статистики
ANALYZE products;
ANALYZE orders;

-- Очистка таблиц
VACUUM ANALYZE products;
VACUUM ANALYZE orders;

-- 12. Оптимизация текстового поиска
-- Создание полнотекстового индекса
CREATE INDEX idx_products_search ON products 
USING gin(to_tsvector('english', name || ' ' || description));

-- Поиск с использованием полнотекстового индекса
SELECT * FROM products 
WHERE to_tsvector('english', name || ' ' || description) 
@@ to_tsquery('english', 'laptop & high-performance'); 