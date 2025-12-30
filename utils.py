# Utility functions for the application

import hashlib
import uuid
from datetime import datetime
from typing import List, Dict, Any, Optional

def generate_unique_id(prefix: str = "") -> str:
    """Generate a unique identifier."""
    unique_id = str(uuid.uuid4())
    return f"{prefix}{unique_id}" if prefix else unique_id

def hash_string(text: str, algorithm: str = "sha256") -> str:
    """Hash a string using specified algorithm."""
    if algorithm == "md5":
        return hashlib.md5(text.encode()).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(text.encode()).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(text.encode()).hexdigest()
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

def format_timestamp(timestamp: datetime = None, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Format timestamp to string."""
    if timestamp is None:
        timestamp = datetime.now()
    return timestamp.strftime(format_str)

def sanitize_input(text: str, max_length: int = 255) -> str:
    """Sanitize user input."""
    if not isinstance(text, str):
        return ""
    
    # Remove potentially dangerous characters
    sanitized = text.strip()
    
    # Truncate if too long
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
    
    return sanitized

def paginate_results(data: List[Any], page: int = 1, per_page: int = 20) -> Dict[str, Any]:
    """Paginate a list of results."""
    total = len(data)
    start = (page - 1) * per_page
    end = start + per_page
    
    return {
        'data': data[start:end],
        'pagination': {
            'page': page,
            'per_page': per_page,
            'total': total,
            'pages': (total + per_page - 1) // per_page
        }
    }

def validate_email(email: str) -> bool:
    """Basic email validation."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def merge_dictionaries(dict1: Dict, dict2: Dict, deep: bool = True) -> Dict:
    """Merge two dictionaries."""
    if not deep:
        return {**dict1, **dict2}
    
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dictionaries(result[key], value, deep=True)
        else:
            result[key] = value
    
    return result