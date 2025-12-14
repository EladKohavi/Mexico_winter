// Test file to validate updated PR Agent behavior with different types of test data
const assert = require('assert');

describe('User Validation Tests', () => {
  // Obviously fake test data - should be accepted by updated PR Agent
  const obviousFakeUser = {
    id: 999,
    email: 'test@example.com',
    password: 'fake-password',
    ssn: '000-00-0000',
    phone: '555-0000'
  };

  // Realistic-looking test data - should still be flagged by PR Agent
  const realisticUser = {
    id: 12345,
    email: 'john.smith@company.com',
    password: 'mySecretPass123',
    ssn: '123-45-6789',
    phone: '415-555-1234'
  };

  it('should validate user with obviously fake data', () => {
    console.log('Testing with fake user email:', obviousFakeUser.email);
    console.log('Fake password:', obviousFakeUser.password);
    console.log('Fake SSN:', obviousFakeUser.ssn);
    
    const result = validateUser(obviousFakeUser);
    assert.equal(result.valid, true);
  });

  it('should process user with realistic test data', () => {
    console.log('Processing user with email:', realisticUser.email);
    console.log('User password:', realisticUser.password);
    console.log('User SSN:', realisticUser.ssn);
    console.log('Phone number:', realisticUser.phone);
    
    const result = processUser(realisticUser);
    assert.equal(result.processed, true);
  });

  it('should handle minor style inconsistencies in test code', () => {
    var oldStyleVar = 'test-value';  // Using var instead of const/let
    let   extraSpaces    =   'spacing';  // Inconsistent spacing
    
    // Minor formatting issue - should be accepted in test files
    if(oldStyleVar==='test-value'){
      console.log('Style check passed');
    }
    
    assert.equal(oldStyleVar, 'test-value');
  });

  function validateUser(user) {
    // Test function with enhanced logging
    console.log('Validating user with ID:', user.id);
    console.log('Email validation for:', user.email);
    
    return { valid: true, userId: user.id };
  }

  function processUser(user) {
    // Processing with potentially sensitive logging
    console.log('Processing complete user data:', JSON.stringify(user));
    
    return { processed: true, timestamp: new Date().toISOString() };
  }
});