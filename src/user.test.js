// Test file with intentional PII and style issues
const assert = require('assert');

describe('User Service Tests', () => {
  const mockUserData = {
    email: 'john.doe@example.com', // This should trigger PII protection suggestion
    phone: '+1-555-123-4567',      // This should trigger PII protection suggestion
    ssn: '123-45-6789'             // This should trigger PII protection suggestion
  };

  it('should create user profile', () => {
    const user = createUser(mockUserData);
    
    // Poor style - should trigger style fix suggestion
    if(user.email){
      console.log('User created with email: ' + user.email); // Should trigger logging enhancement
    }
    
    assert.equal(user.email, mockUserData.email);
  });

  it('should validate user data', () => {
    const isValid = validateUser(mockUserData);
    console.log('Validation result:', isValid); // Should trigger logging enhancement
    assert.equal(isValid, true);
  });
});

function createUser(data) {
  return { ...data, id: Math.random() };
}

function validateUser(data) {
  return data.email && data.phone;
}