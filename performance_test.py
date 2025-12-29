# Test file with performance anti-patterns that might trigger comments

import time
import threading

def test_inefficient_operations():
    """Test with obviously inefficient operations."""
    # Inefficient string concatenation
    result = ""
    for i in range(1000):
        result += str(i)  # O(n²) operation
    
    assert len(result) > 0
    
    # Inefficient list operations
    items = []
    for i in range(100):
        items.insert(0, i)  # O(n) insertion at beginning
    
    assert len(items) == 100

def test_nested_loops():
    """Test with unnecessary nested loops."""
    # O(n³) algorithm when O(n) would work
    data = list(range(50))
    result = []
    
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 75:  # Arbitrary condition
                    result.append((i, j, k))
                    if len(result) >= 10:  # Early exit
                        break
            if len(result) >= 10:
                break
        if len(result) >= 10:
            break
    
    assert len(result) > 0

def test_memory_intensive():
    """Test with memory-intensive operations."""
    # Creating large data structures unnecessarily
    large_list = list(range(100000))
    large_dict = {i: str(i) * 100 for i in range(10000)}
    
    # Unnecessary copying
    copy1 = large_list.copy()
    copy2 = copy1.copy()
    copy3 = copy2.copy()
    
    assert len(copy3) == len(large_list)
    assert len(large_dict) == 10000

class TestThreadingIssues:
    """Test class with threading anti-patterns."""
    
    def test_thread_without_join(self):
        """Test with threads that aren't properly joined."""
        results = []
        
        def worker():
            time.sleep(0.1)
            results.append("done")
        
        # Creating thread without joining (resource leak)
        thread = threading.Thread(target=worker)
        thread.start()
        # No thread.join() - bad practice
        
        # Busy waiting instead of proper synchronization
        while len(results) == 0:
            time.sleep(0.01)  # Busy wait
        
        assert results[0] == "done"
    
    def test_race_condition_pattern(self):
        """Test with potential race condition."""
        shared_counter = [0]  # Mutable shared state
        
        def increment():
            for _ in range(100):
                # Race condition: read-modify-write without lock
                shared_counter[0] += 1
        
        threads = []
        for _ in range(5):
            t = threading.Thread(target=increment)
            threads.append(t)
            t.start()
        
        # Join threads properly this time
        for t in threads:
            t.join()
        
        # Result might be unpredictable due to race condition
        assert shared_counter[0] > 0

def test_blocking_operations():
    """Test with blocking operations that might be flagged."""
    # Blocking sleep in test (anti-pattern)
    time.sleep(0.5)  # Blocking operation
    
    # Synchronous file I/O
    with open('/tmp/blocking_test.txt', 'w') as f:
        for i in range(1000):
            f.write(f"Line {i}\n")  # Blocking writes
            f.flush()  # Force flush each time (inefficient)
    
    # Reading it back inefficiently
    lines = []
    with open('/tmp/blocking_test.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())  # Processing each line individually
    
    assert len(lines) == 1000
    
    # Cleanup
    import os
    os.unlink('/tmp/blocking_test.txt')

def test_recursive_without_limit():
    """Test with recursive function without proper limits."""
    def fibonacci_inefficient(n):
        # Exponential time complexity
        if n <= 1:
            return n
        return fibonacci_inefficient(n-1) + fibonacci_inefficient(n-2)
    
    # Calculating inefficiently (might timeout or use too much CPU)
    result = fibonacci_inefficient(20)  # Still manageable but inefficient
    
    assert result > 0

def test_database_n_plus_one():
    """Test simulating N+1 query problem."""
    # Simulating database queries
    def get_users():
        return [{'id': i, 'name': f'User{i}'} for i in range(50)]
    
    def get_user_posts(user_id):
        # Simulate database call
        time.sleep(0.001)  # Simulate network/DB latency
        return [f'Post {i} by User {user_id}' for i in range(3)]
    
    users = get_users()  # 1 query
    
    # N+1 problem: one query per user instead of bulk query
    all_posts = []
    for user in users:  # N queries
        posts = get_user_posts(user['id'])
        all_posts.extend(posts)
    
    assert len(all_posts) == len(users) * 3

def test_json_parsing_inefficiency():
    """Test with inefficient JSON operations."""
    import json
    
    # Creating large JSON data
    large_data = {
        'users': [{'id': i, 'data': 'x' * 1000} for i in range(1000)]
    }
    
    # Inefficient serialization/deserialization in loop
    for _ in range(10):
        json_str = json.dumps(large_data)  # Serialize each time
        parsed = json.loads(json_str)      # Parse each time
        assert len(parsed['users']) == 1000