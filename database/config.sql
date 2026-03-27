-- Database Configuration for MySQL
-- This project uses MySQL as the primary database

-- MySQL-specific configuration
SET sql_mode = 'STRICT_TRANS_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO';
SET innodb_strict_mode = 1;
SET foreign_key_checks = 1;

-- MySQL character set configuration
ALTER DATABASE gitstream_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- MySQL-specific variables
SET @mysql_version = @@version;