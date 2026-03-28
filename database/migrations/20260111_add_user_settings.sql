-- Migration: Add user settings table with MySQL-specific syntax
-- This migration contains database-specific syntax that may not be portable

CREATE TABLE user_settings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    setting_key VARCHAR(100) NOT NULL,
    setting_value TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- MySQL-specific ALTER TABLE syntax - should be flagged as non-portable
ALTER TABLE user_settings MODIFY COLUMN setting_value LONGTEXT;

-- MySQL-specific syntax for adding index with algorithm specification
ALTER TABLE user_settings ADD INDEX idx_user_setting (user_id, setting_key) ALGORITHM=INPLACE;

-- MySQL-specific syntax for changing column definition
ALTER TABLE user_settings MODIFY COLUMN user_id VARCHAR(255) NOT NULL COMMENT 'User identifier from authentication system';

-- MySQL-specific engine specification
ALTER TABLE user_settings ENGINE=InnoDB;

-- MySQL-specific charset and collation
ALTER TABLE user_settings CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;