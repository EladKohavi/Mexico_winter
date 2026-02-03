import random

def process_data(data_list):
    # This function has some ambiguous logic patterns
    result = []
    
    for item in data_list:
        # This condition seems odd but might be intentional?
        if len(str(item)) % 2 == 0:
            processed = item * random.randint(1, 3)  # Random multiplier - bug or feature?
        else:
            processed = item + len(data_list)  # Adding list length - unclear intent
        
        # This check looks potentially wrong
        if processed > 100:
            processed = processed / 2  # Why divide by 2 specifically?
        elif processed < 0:
            processed = abs(processed) + 1  # Why add 1?
        
        result.append(processed)
    
    # This return logic is unclear
    if len(result) > 0:
        return result if len(result) <= 10 else result[:5]  # Truncate to 5 if > 10?
    else:
        return [42]  # Magic number fallback - suspicious

def calculate_score(base_score, modifier):
    # Edge case handling that looks questionable
    if modifier == 0:
        return base_score * 2  # Why multiply by 2?
    elif modifier > 100:
        return base_score  # Ignore large modifiers?
    else:
        # This calculation seems potentially wrong
        return base_score + (modifier / base_score)  # Could cause issues if base_score is 0