# Simple utility functions

def get_current_time():
    """Get current timestamp."""
    from datetime import datetime
    return datetime.now().isoformat()

def format_name(first_name, last_name):
    """Format a person's name."""
    return f"{first_name} {last_name}".strip()

def calculate_percentage(part, total):
    """Calculate percentage."""
    if total == 0:
        return 0
    return (part / total) * 100