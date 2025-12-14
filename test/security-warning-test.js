// Test file designed to trigger security warnings despite being "mock" data
const assert = require('assert');

describe('Security Warning Tests', () => {
  // Mock data that looks realistic enough to trigger warnings
  const userAccount = {
    id: 12345,
    email: 'alice.johnson@company.com',      // Realistic email - should warn
    password: 'SecurePass2023!',             // Realistic password - should warn
    ssn: '987-65-4321',                      // Realistic SSN - should warn
    creditCard: '4532-1234-5678-9012',      // Realistic credit card - should warn
    apiKey: 'sk-live-abc123def456ghi789',    // Looks like real API key - should warn
    bankAccount: '1234567890123456',         // Bank account number - should warn
    personalInfo: {
      firstName: 'Alice',
      lastName: 'Johnson',
      phoneNumber: '(415) 555-1234',        // Realistic phone - should warn
      address: '123 Main Street, San Francisco, CA 94102'  // Real-looking address - should warn
    }
  };

  // Database connection with realistic credentials
  const dbCredentials = {
    host: 'prod-db-01.company.com',          // Realistic hostname - should warn
    username: 'admin_user',                   // Realistic username - should warn
    password: 'MyDatabasePass123!',          // Realistic password - should warn
    database: 'production_db',               // Production database name - should warn
    connectionString: 'postgresql://admin_user:MyDatabasePass123!@prod-db-01.company.com:5432/production_db'
  };

  it('should process user account data', () => {
    console.log('Processing user:', userAccount.email);
    console.log('User password:', userAccount.password);
    console.log('SSN:', userAccount.ssn);
    console.log('Credit card:', userAccount.creditCard);
    console.log('API key:', userAccount.apiKey);
    console.log('Bank account:', userAccount.bankAccount);
    console.log('Phone:', userAccount.personalInfo.phoneNumber);
    console.log('Address:', userAccount.personalInfo.address);
    
    const result = processUserAccount(userAccount);
    assert.equal(result.processed, true);
  });

  it('should connect to database with credentials', () => {
    console.log('Connecting to database:', dbCredentials.host);
    console.log('Username:', dbCredentials.username);
    console.log('Password:', dbCredentials.password);
    console.log('Database:', dbCredentials.database);
    console.log('Full connection string:', dbCredentials.connectionString);
    
    const connection = connectToDatabase(dbCredentials);
    assert.equal(connection.connected, true);
  });

  it('should handle payment processing', () => {
    const paymentData = {
      cardNumber: '4532-1234-5678-9012',
      cvv: '123',
      expiryDate: '12/25',
      holderName: 'Alice Johnson',
      billingAddress: userAccount.personalInfo.address
    };
    
    console.log('Processing payment for card:', paymentData.cardNumber);
    console.log('CVV:', paymentData.cvv);
    console.log('Cardholder:', paymentData.holderName);
    console.log('Billing address:', paymentData.billingAddress);
    
    const result = processPayment(paymentData);
    assert.equal(result.success, true);
  });

  function processUserAccount(account) {
    console.log('Full account data:', JSON.stringify(account));
    return { processed: true, accountId: account.id };
  }

  function connectToDatabase(credentials) {
    console.log('Database connection with full credentials:', credentials);
    return { connected: true, host: credentials.host };
  }

  function processPayment(paymentInfo) {
    console.log('Payment processing with full card data:', paymentInfo);
    return { success: true, transactionId: 'txn_12345' };
  }
});