# Configuration management module

import os
from typing import Dict, Any, Optional

class ConfigManager:
    """Manages application configuration settings."""
    
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self._config = {}
        self.load_config()
    
    def load_config(self) -> None:
        """Load configuration from file or environment variables."""
        # Load from environment variables first
        self._config.update({
            'database_host': os.getenv('DATABASE_HOST', 'localhost'),
            'database_port': int(os.getenv('DATABASE_PORT', '5432')),
            'redis_host': os.getenv('REDIS_HOST', 'localhost'),
            'redis_port': int(os.getenv('REDIS_PORT', '6379')),
            'log_level': os.getenv('LOG_LEVEL', 'INFO'),
            'debug_mode': os.getenv('DEBUG', 'false').lower() == 'true'
        })
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by key."""
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set configuration value."""
        self._config[key] = value
    
    def get_database_config(self) -> Dict[str, Any]:
        """Get database configuration."""
        return {
            'host': self.get('database_host'),
            'port': self.get('database_port'),
            'database': self.get('database_name', 'app_db'),
            'user': self.get('database_user', 'postgres'),
            'password': self.get('database_password')
        }
    
    def get_redis_config(self) -> Dict[str, Any]:
        """Get Redis configuration."""
        return {
            'host': self.get('redis_host'),
            'port': self.get('redis_port'),
            'db': self.get('redis_db', 0)
        }
    
    def is_debug_enabled(self) -> bool:
        """Check if debug mode is enabled."""
        return self.get('debug_mode', False)

# Global configuration instance
config = ConfigManager()