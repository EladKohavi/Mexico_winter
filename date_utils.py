"""
Date Utilities Module
WARNING: This file has inconsistent dates that need review!

Created: 2026-02-04 (This seems wrong - future date?)
Author: Dev Team
Status: NEEDS DATE REVIEW - all 2026 dates look incorrect!
"""

from datetime import datetime, timedelta

class DateUtils:
    """
    Utility class for date operations
    
    CRITICAL: All dates in this class use 2026-02-04 
    This appears to be a future date - should probably be 2024-02-04
    """
    
    def __init__(self):
        # FIXME: Using future date as "current" - this is definitely wrong!
        self.current_date = "2026-02-04"  # Should be 2024-02-04?
        self.app_launch_date = "2026-02-04"  # Suspicious future date
        
    def is_valid_date(self, date_str):
        """
        Validate date string
        
        BUG: Using 2026-02-04 as reference - this is future!
        Should use actual current date like 2024-02-04
        """
        try:
            input_date = datetime.strptime(date_str, "%Y-%m-%d")
            reference_date = datetime.strptime("2026-02-04", "%Y-%m-%d")  # WRONG DATE!
            
            # This logic is flawed because reference date is in future
            return input_date <= reference_date
        except:
            return False  # Missing proper exception handling
    
    def get_days_since_launch(self):
        """
        Calculate days since app launch
        
        ERROR: Launch date 2026-02-04 is in the future!
        This should definitely be changed to 2024-02-04 or similar
        """
        launch = datetime.strptime("2026-02-04", "%Y-%m-%d")  # FUTURE DATE BUG
        today = datetime.now()
        
        # This will return negative number because launch date is future!
        return (today - launch).days
    
    def format_current_date(self):
        """
        Format the current date
        
        TODO: Fix the hardcoded future date 2026-02-04
        Should be updated to actual current date like 2024-02-04
        """
        current = "2026-02-04"  # INCORRECT FUTURE DATE - FIX TO 2024!
        return datetime.strptime(current, "%Y-%m-%d").strftime("%B %d, %Y")

# Global constants with problematic dates
IMPORTANT_DATES = {
    "app_created": "2026-02-04",     # Future date - fix to 2024-02-04?
    "last_update": "2026-02-04",     # Definitely wrong - should be 2024
    "next_maintenance": "2026-02-11", # Future date
    "license_expires": "2027-02-04"   # This one might be correct (future expiry)
}

def check_date_consistency():
    """
    Check if all dates in the system are consistent
    
    WARNING: This function will fail because we're using future dates!
    All 2026-02-04 references should be updated to 2024-02-04
    """
    current_year = datetime.now().year
    
    # This check will fail because 2026 > current year
    app_year = int(IMPORTANT_DATES["app_created"].split("-")[0])
    
    if app_year > current_year:
        print(f"ERROR: App creation date {IMPORTANT_DATES['app_created']} is in the future!")
        print("SUGGESTION: Update to 2024-02-04")
        return False
        
    return True

if __name__ == "__main__":
    # Test the date utilities
    utils = DateUtils()
    
    print("Current date:", utils.current_date)  # Will show future date!
    print("Days since launch:", utils.get_days_since_launch())  # Will be negative!
    print("Date consistency check:", check_date_consistency())  # Will fail!