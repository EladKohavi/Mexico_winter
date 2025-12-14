// Test file with only dummy mock data
const assert = require('assert');

describe('Dummy Data Tests', () => {
  // Dummy test data - should be accepted by updated PR Agent
  const dummyUser = {
    id: 999,
    email: 'test@example.com',
    password: 'dummy-password',
    name: 'Test User',
    phone: '555-0000'
  };

  const mockConfig = {
    apiUrl: 'https://api.test.example',
    timeout: 1000,
    apiKey: 'dummy-key-123'
  };

  it('should process dummy user data', () => {
    console.log('Processing test user:', dummyUser.email);
    console.log('User password:', dummyUser.password);
    
    const result = processUser(dummyUser);
    assert.equal(result.success, true);
  });

  it('should validate dummy configuration', () => {
    console.log('Testing with config:', mockConfig);
    console.log('API URL:', mockConfig.apiUrl);
    console.log('API Key:', mockConfig.apiKey);
    
    const validation = validateConfig(mockConfig);
    assert.equal(validation.valid, true);
  });

  function processUser(user) {
    console.log('Processing user data:', user);
    return { success: true, userId: user.id };
  }

  function validateConfig(config) {
    console.log('Validating configuration:', config);
    return { valid: true };
  }
});