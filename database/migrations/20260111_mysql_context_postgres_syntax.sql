-- MySQL Migration: Add analytics table for user metrics
-- This migration is intended for MySQL database
-- MySQL connection string: mysql://user:pass@localhost:3306/database

-- Start with valid MySQL syntax
CREATE TABLE user_analytics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- MySQL-specific index syntax
ALTER TABLE user_analytics ADD INDEX idx_user_analytics_user_id (user_id) USING BTREE;

-- Now accidentally use PostgreSQL syntax (this should fail in MySQL)
-- PostgreSQL ALTER COLUMN TYPE syntax - WRONG for MySQL!
ALTER TABLE user_analytics ALTER COLUMN user_id TYPE VARCHAR(500);

-- PostgreSQL SERIAL type - WRONG for MySQL!
ALTER TABLE user_analytics ADD COLUMN event_id SERIAL;

-- PostgreSQL JSONB type - WRONG for MySQL!
ALTER TABLE user_analytics ADD COLUMN event_data JSONB DEFAULT '{}';

-- PostgreSQL array syntax - WRONG for MySQL!
ALTER TABLE user_analytics ADD COLUMN tags TEXT[] DEFAULT ARRAY[]::TEXT[];

-- PostgreSQL enum type - WRONG for MySQL!
CREATE TYPE event_type AS ENUM ('click', 'view', 'purchase');
ALTER TABLE user_analytics ADD COLUMN event_type event_type DEFAULT 'view';

-- PostgreSQL-specific index syntax - WRONG for MySQL!
CREATE INDEX idx_analytics_jsonb ON user_analytics USING GIN (event_data);

-- More MySQL syntax to make context clear
ALTER TABLE user_analytics ENGINE=InnoDB;
ALTER TABLE user_analytics CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;