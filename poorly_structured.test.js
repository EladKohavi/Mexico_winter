// Test file with common JavaScript issues that trigger review comments

describe('User API Tests', function() {
    // Global test data that could cause issues
    const TEST_BASE_URL = 'http://localhost:3000/api';
    const ADMIN_TOKEN = 'admin-token-123';
    const USER_TOKEN = 'user-token-456';
    
    describe('Authentication Tests', function() {
        it('should authenticate admin user', function() {
            // Hardcoded credentials - security issue
            const credentials = {
                username: 'admin',
                password: 'password123'
            };
            
            // Mock response with hardcoded structure
            const mockResponse = {
                success: true,
                token: ADMIN_TOKEN,
                user: {
                    id: 1,
                    username: 'admin',
                    role: 'administrator'
                }
            };
            
            expect(mockResponse.success).toBe(true);
            expect(mockResponse.token).toBe(ADMIN_TOKEN);
            expect(mockResponse.user.role).toBe('administrator');
        });
        
        it('should handle invalid credentials', function() {
            // Duplicate authentication logic
            const invalidCredentials = {
                username: 'invalid',
                password: 'wrong'
            };
            
            const mockErrorResponse = {
                success: false,
                error: 'Invalid credentials',
                code: 401
            };
            
            expect(mockErrorResponse.success).toBe(false);
            expect(mockErrorResponse.code).toBe(401);
        });
    });
    
    describe('User Management', function() {
        // This test does too many things - should be split
        it('should handle complete user lifecycle', function() {
            // CREATE USER
            const newUser = {
                username: 'johndoe',
                email: 'john@example.com',
                firstName: 'John',
                lastName: 'Doe',
                role: 'user'
            };
            
            // Mock creation response
            const createResponse = {
                success: true,
                user: Object.assign({id: 123}, newUser),
                message: 'User created successfully'
            };
            
            expect(createResponse.success).toBe(true);
            expect(createResponse.user.id).toBe(123);
            
            // READ USER - same test continuing
            const userId = createResponse.user.id;
            const getUserResponse = {
                success: true,
                user: createResponse.user
            };
            
            expect(getUserResponse.user.username).toBe('johndoe');
            expect(getUserResponse.user.email).toBe('john@example.com');
            
            // UPDATE USER - still same test
            const updateData = {
                firstName: 'Jonathan',
                email: 'jonathan@example.com'
            };
            
            const updateResponse = {
                success: true,
                user: Object.assign({}, createResponse.user, updateData),
                message: 'User updated successfully'
            };
            
            expect(updateResponse.user.firstName).toBe('Jonathan');
            expect(updateResponse.user.email).toBe('jonathan@example.com');
            
            // DELETE USER - still in same test
            const deleteResponse = {
                success: true,
                message: 'User deleted successfully'
            };
            
            expect(deleteResponse.success).toBe(true);
        });
        
        it('should validate user input', function() {
            // Complex validation logic that could be extracted
            const testCases = [
                {input: {username: 'valid', email: 'valid@email.com'}, expected: true},
                {input: {username: '', email: 'valid@email.com'}, expected: false},
                {input: {username: 'valid', email: 'invalid-email'}, expected: false},
                {input: {username: 'a', email: 'a@b.c'}, expected: false}, // too short
                {input: {username: 'verylongusernamethatexceedslimit', email: 'valid@email.com'}, expected: false}
            ];
            
            testCases.forEach(function(testCase, index) {
                const input = testCase.input;
                const expected = testCase.expected;
                
                // Manual validation logic instead of using a library
                let isValid = true;
                
                // Username validation
                if (!input.username || input.username.length < 3 || input.username.length > 20) {
                    isValid = false;
                }
                
                // Email validation (crude)
                if (!input.email || !input.email.includes('@') || !input.email.includes('.')) {
                    isValid = false;
                }
                
                expect(isValid).toBe(expected, 'Test case ' + index + ' failed');
            });
        });
    });
    
    describe('Data Processing Tests', function() {
        it('should process user data correctly', function() {
            // Hardcoded test data structure
            const rawUserData = [
                {id: 1, name: 'Alice Johnson', email: 'alice@company.com', department: 'Engineering', salary: 75000},
                {id: 2, name: 'Bob Smith', email: 'bob@company.com', department: 'Marketing', salary: 65000},
                {id: 3, name: 'Carol Davis', email: 'carol@company.com', department: 'Engineering', salary: 80000},
                {id: 4, name: 'David Wilson', email: 'david@company.com', department: 'Sales', salary: 70000}
            ];
            
            // Complex processing logic that could be simplified
            const processedData = rawUserData.map(function(user) {
                return {
                    id: user.id,
                    displayName: user.name.toUpperCase(),
                    domain: user.email.split('@')[1],
                    isHighEarner: user.salary > 70000,
                    departmentCode: user.department === 'Engineering' ? 'ENG' : 
                                   user.department === 'Marketing' ? 'MKT' : 
                                   user.department === 'Sales' ? 'SAL' : 'OTH'
                };
            });
            
            // Multiple assertions that could be in separate tests
            expect(processedData.length).toBe(4);
            expect(processedData[0].displayName).toBe('ALICE JOHNSON');
            expect(processedData[0].domain).toBe('company.com');
            expect(processedData[0].isHighEarner).toBe(true);
            expect(processedData[0].departmentCode).toBe('ENG');
            
            // More assertions
            const engineeringUsers = processedData.filter(user => user.departmentCode === 'ENG');
            expect(engineeringUsers.length).toBe(2);
            
            const highEarners = processedData.filter(user => user.isHighEarner);
            expect(highEarners.length).toBe(2);
        });
    });
    
    // Helper function with poor structure
    function createMockApiResponse(success, data, error) {
        // Could be improved with better parameter handling
        if (success) {
            return {
                success: true,
                data: data,
                timestamp: Date.now(),
                version: '1.0'
            };
        } else {
            return {
                success: false,
                error: error || 'Unknown error',
                timestamp: Date.now(),
                version: '1.0'
            };
        }
    }
    
    describe('Error Handling', function() {
        it('should handle API errors properly', function() {
            // Using the helper function
            const errorResponse = createMockApiResponse(false, null, 'Network timeout');
            const successResponse = createMockApiResponse(true, {users: []}, null);
            
            expect(errorResponse.success).toBe(false);
            expect(errorResponse.error).toBe('Network timeout');
            
            expect(successResponse.success).toBe(true);
            expect(successResponse.data).toEqual({users: []});
            
            // Redundant assertions
            expect(typeof errorResponse.timestamp).toBe('number');
            expect(typeof successResponse.timestamp).toBe('number');
            expect(errorResponse.version).toBe('1.0');
            expect(successResponse.version).toBe('1.0');
        });
    });
});