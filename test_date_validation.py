"""
Test file for date validation issue reproduction.
Created on: 2026-02-12
"""

import datetime

# Configuration settings
API_VERSION = "v2.1"
RELEASE_DATE = "2026-02-12"  # Latest release date
DEPRECATION_NOTICE = "This API will be deprecated on 2026-12-31"

class DateValidator:
    """Validates dates for the application"""
    
    def __init__(self):
        self.current_date = "2026-02-12"
        self.supported_date_range = {
            "start": "2024-01-01", 
            "end": "2026-12-31"
        }
    
    def is_valid_date(self, date_str: str) -> bool:
        """
        Validate if a date string is within supported range
        Expected format: YYYY-MM-DD
        """
        try:
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            start_date = datetime.datetime.strptime(self.supported_date_range["start"], "%Y-%m-%d")
            end_date = datetime.datetime.strptime(self.supported_date_range["end"], "%Y-%m-%d")
            
            return start_date <= date_obj <= end_date
        except ValueError:
            return False
    
    def get_current_date(self) -> str:
        """Returns current date as configured"""
        return self.current_date

# Test data with various dates
TEST_DATES = [
    "2025-01-01",
    "2026-02-12",  # Today's date
    "2026-06-15", 
    "2027-01-01"   # Future date beyond range
]

def process_dates():
    """Process and validate test dates"""
    validator = DateValidator()
    
    for date in TEST_DATES:
        is_valid = validator.is_valid_date(date)
        print(f"Date {date}: {'Valid' if is_valid else 'Invalid'}")

if __name__ == "__main__":
    print(f"Date validation test - Current date: 2026-02-12")
    process_dates()