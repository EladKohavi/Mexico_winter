-- Database migration: Add user preferences table
-- Using MySQL-specific syntax

CREATE TABLE user_preferences (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    preference_key VARCHAR(255) NOT NULL,
    preference_value TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_user_id (user_id),
    UNIQUE KEY uk_user_preference (user_id, preference_key)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Add column to existing table using MySQL syntax
ALTER TABLE users 
MODIFY COLUMN email VARCHAR(320) NOT NULL,
ADD COLUMN last_login DATETIME DEFAULT NULL AFTER updated_at,
ADD INDEX idx_last_login (last_login);

-- Create trigger using MySQL syntax
DELIMITER $$
CREATE TRIGGER update_user_preferences_timestamp 
    BEFORE UPDATE ON user_preferences
    FOR EACH ROW 
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END$$
DELIMITER ;

-- Insert default preferences with MySQL-specific functions
INSERT INTO user_preferences (user_id, preference_key, preference_value) VALUES
(1, 'theme', 'dark'),
(1, 'notifications', JSON_OBJECT('email', true, 'push', false)),
(2, 'language', 'en_US');