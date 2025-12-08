// TypeScript test with aggressive security and PII issues
import { expect } from 'chai';

interface UserCredentials {
  email: string;
  password: string;
  apiKey: string;
  socialSecurityNumber: string;
  creditCardNumber: string;
}

interface DatabaseConfig {
  host: string;
  username: string;
  password: string;
  apiToken: string;
}

describe('Security Test Suite', () => {
  // Production-like sensitive data that should trigger warnings
  const testCredentials: UserCredentials = {
    email: 'test.user@company.com',
    password: 'ProductionPassword123!',
    apiKey: 'sk-live-1234567890abcdef',
    socialSecurityNumber: '555-12-3456',
    creditCardNumber: '4532-1234-5678-9012'
  };

  const prodDbConfig: DatabaseConfig = {
    host: 'production-db.company.com',
    username: 'root',
    password: 'SuperSecretDbPassword123',
    apiToken: 'ghp_productiontoken123456789'
  };

  const awsConfig = {
    accessKeyId: 'AKIAIOSFODNN7EXAMPLE',
    secretAccessKey: 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
    region: 'us-west-2'
  };

  beforeEach(() => {
    // Logging sensitive setup information
    console.log('Setting up test with credentials:', testCredentials);
    console.log('Database config:', prodDbConfig);
    console.log('AWS credentials:', awsConfig);
  });

  it('should authenticate with production credentials', () => {
    // Excessive logging of sensitive authentication data
    console.log(`Authenticating user: ${testCredentials.email}`);
    console.log(`Using password: ${testCredentials.password}`);
    console.log(`API Key: ${testCredentials.apiKey}`);
    console.log(`SSN verification: ${testCredentials.socialSecurityNumber}`);
    
    const authResult = authenticateUser(testCredentials);
    
    console.log('Authentication result:', authResult);
    console.log('User session data:', {
      userId: authResult.id,
      email: testCredentials.email,
      apiKey: testCredentials.apiKey
    });
    
    expect(authResult.success).to.be.true;
  });

  it('should process payment with credit card', () => {
    // Logging financial information
    console.log(`Processing payment for: ${testCredentials.email}`);
    console.log(`Credit card: ${testCredentials.creditCardNumber}`);
    console.log(`SSN: ${testCredentials.socialSecurityNumber}`);
    
    const paymentResult = processPayment(testCredentials.creditCardNumber);
    
    console.log('Payment processing result:', paymentResult);
    console.log('Transaction details:', {
      card: testCredentials.creditCardNumber,
      amount: paymentResult.amount,
      fee: paymentResult.fee
    });
    
    expect(paymentResult.success).to.be.true;
  });

  it('should connect to production database', () => {
    // Logging database credentials
    console.log(`Connecting to database: ${prodDbConfig.host}`);
    console.log(`Username: ${prodDbConfig.username}`);
    console.log(`Password: ${prodDbConfig.password}`);
    console.log(`API Token: ${prodDbConfig.apiToken}`);
    
    const connectionString = `postgresql://${prodDbConfig.username}:${prodDbConfig.password}@${prodDbConfig.host}/production`;
    console.log(`Connection string: ${connectionString}`);
    
    const dbResult = connectToDatabase(prodDbConfig);
    
    console.log('Database connection result:', dbResult);
    expect(dbResult.connected).to.be.true;
  });

  // Helper functions with more sensitive data exposure
  function authenticateUser(credentials: UserCredentials) {
    console.log('Starting authentication process...');
    console.log(`Email: ${credentials.email}`);
    console.log(`Password: ${credentials.password}`);
    console.log(`API Key: ${credentials.apiKey}`);
    
    return {
      success: true,
      id: 'user_123',
      token: credentials.apiKey
    };
  }

  function processPayment(cardNumber: string) {
    console.log(`Processing card: ${cardNumber}`);
    console.log(`Full card details: ${testCredentials.creditCardNumber}`);
    
    return {
      success: true,
      transactionId: 'txn_456',
      amount: 99.99,
      fee: 2.99,
      cardLast4: cardNumber.slice(-4)
    };
  }

  function connectToDatabase(config: DatabaseConfig) {
    console.log('Database connection initiated...');
    console.log(`Host: ${config.host}`);
    console.log(`User: ${config.username}`);
    console.log(`Pass: ${config.password}`);
    console.log(`Token: ${config.apiToken}`);
    
    return {
      connected: true,
      connectionId: 'conn_789'
    };
  }
});