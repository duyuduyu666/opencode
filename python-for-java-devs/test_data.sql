-- 测试数据库和表

-- 创建数据库
CREATE DATABASE IF NOT EXISTS test_db DEFAULT CHARSET utf8mb4;
USE test_db;

-- 用户表
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- 订单表
CREATE TABLE IF NOT EXISTS orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    quantity INT DEFAULT 1,
    price DECIMAL(10, 2) NOT NULL,
    status ENUM('pending', 'paid', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- 产品表
CREATE TABLE IF NOT EXISTS products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 插入测试数据
INSERT INTO users (username, email, age) VALUES
('alice', 'alice@example.com', 25),
('bob', 'bob@example.com', 30),
('charlie', 'charlie@example.com', 28),
('david', 'david@example.com', 35),
('eve', 'eve@example.com', 22);

INSERT INTO products (name, category, price, stock) VALUES
('iPhone 15', 'Electronics', 6999.00, 100),
('MacBook Pro', 'Electronics', 12999.00, 50),
('AirPods Pro', 'Electronics', 1899.00, 200),
('iPad Air', 'Electronics', 4599.00, 80),
('Python入门', 'Books', 79.00, 500);

INSERT INTO orders (user_id, product_name, quantity, price, status) VALUES
(1, 'iPhone 15', 1, 6999.00, 'delivered'),
(1, 'AirPods Pro', 2, 3798.00, 'shipped'),
(2, 'MacBook Pro', 1, 12999.00, 'paid'),
(3, 'Python入门', 3, 237.00, 'pending'),
(4, 'iPad Air', 2, 9198.00, 'delivered');

-- 查看数据
SELECT * FROM users;
SELECT * FROM products;
SELECT * FROM orders;
