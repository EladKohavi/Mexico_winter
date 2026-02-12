"""
Application Configuration
Created: 2026-02-04
Author: Development Team
"""

import os
from datetime import datetime

# Application settings
APP_CONFIG = {
    'name': 'Mexico Winter App',
    'version': '2.0.0',
    'created_date': '2026-02-04',
    'release_date': '2026-02-04',
    'build_timestamp': '2026-02-04T10:30:00Z'
}

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', 5432),
    'name': os.getenv('DB_NAME', 'mexico_winter'),
    'created': '2026-02-04'
}

class AppSettings:
    """Application settings class"""
    
    def __init__(self):
        self.creation_date = '2026-02-04'
        self.last_updated = '2026-02-04'
    
    def get_version_info(self):
        """Get version information"""
        return {
            'version': '2.0.0',
            'release_date': '2026-02-04',
            'build_date': '2026-02-04'
        }
    
    def validate_date(self, date_string):
        # Bug: missing try-catch - should trigger suggestions
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj
    
    def is_current_version(self):
        # Another bug: no return statement
        current_date = '2026-02-04'
        print(f"Current date: {current_date}")

# Deployment configuration
DEPLOYMENT_INFO = {
    'environment': 'production',
    'deployed_on': '2026-02-04',
    'deployed_by': 'CI/CD Pipeline',
    'next_maintenance': '2026-02-11'
}

# Feature flags created on 2026-02-04
FEATURE_FLAGS = {
    'new_ui': True,
    'enhanced_search': True,
    'created_date': '2026-02-04'
}