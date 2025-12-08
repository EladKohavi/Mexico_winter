// Test file with VERY aggressive PII and logging issues
const { expect } = require('chai');

describe('User Authentication Tests', () => {
  // Real-looking sensitive data that should trigger PII protection
  const testUser = {
    email: 'john.smith@company.com',
    password: 'MySecretPassword123!',
    ssn: '123-45-6789',
    creditCard: '4532-1234-5678-9012',
    phoneNumber: '+1-555-123-4567',
    address: '123 Main St, Anytown, USA 12345',
    bankAccount: '1234567890123456'
  };

  const apiKey = 'sk-1234567890abcdef';
  const secretToken = 'ghp_1234567890abcdefghijklmnopqrstuvwxyz123';

  it('should authenticate user with credentials', () => {
    // Logging sensitive information - should trigger logging enhancement
    console.log('Authenticating user:', testUser.email);
    console.log('User password:', testUser.password);
    console.log('API Key:', apiKey);
    console.log('Full user data:', JSON.stringify(testUser));
    
    const result = authenticateUser(testUser.email, testUser.password);
    expect(result).to.be.true;
  });

  it('should process payment information', () => {
    // More sensitive logging
    console.log('Processing payment for card:', testUser.creditCard);
    console.log('Bank account:', testUser.bankAccount);
    console.log('SSN verification:', testUser.ssn);
    
    const paymentResult = processPayment(testUser);
    expect(paymentResult.success).to.be.true;
  });

  // Helper functions with more PII exposure
  function authenticateUser(email, password) {
    console.log(`Checking credentials: ${email} / ${password}`);
    return email.includes('@') && password.length > 8;
  }

  function processPayment(user) {
    console.log('Payment details:', {
      card: user.creditCard,
      ssn: user.ssn,
      bank: user.bankAccount
    });
    return { success: true, transaction: secretToken };
  }
});