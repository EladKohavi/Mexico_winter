// Test file with less realistic mock data
const assert = require('assert');

describe('Mock Credentials Tests', () => {
  // Database credentials with less realistic values
  const dbCredentials = {
    host: 'test-db-server.mock.com',         
    username: 'test_admin',                   
    password: 'TestPassword123',             
    database: 'test_database',               
    connectionString: 'postgresql://test_admin:TestPassword123@test-db-server.mock.com:5432/test_database'
  };

  // API configuration with mock values
  const apiConfig = {
    baseUrl: 'https://api.testservice.mock',
    apiKey: 'test-key-abc123',
    secretKey: 'mock-secret-xyz789',
    timeout: 5000
  };

  // User test data
  const testUser={id:12345,email:'testuser@mockdomain.com',password:'TestUserPass123',profile:{name:'Test User',phone:'555-TEST',ssn:'123-TEST-456'}};  // No spaces
  var oldStyleVar = 'some-test-value';  // Using var instead of const
  let   extraSpaces    =   'spacing-issue';  // Inconsistent spacing

  // Additional mock data that looks more realistic but is still clearly fake
  const sensitiveTestData = {
    customerEmail: 'customer.test@example.org',  // More realistic but still example.org
    accountPassword: 'MockPass2023!',           // Realistic format but clearly mock
    testSSN: '999-99-9999',                    // Invalid SSN range but realistic format
    dummyPhone: '555-0123'                     // Standard test phone
  };

  it('should connect to test database', () => {
    console.log('Connecting to database:', dbCredentials.host);
    console.log('Username:', dbCredentials.username);
    console.log('Password:', dbCredentials.password);
    console.log('Database:', dbCredentials.database);
    console.log('Connection string:', dbCredentials.connectionString);
    
    const connection = connectToDb(dbCredentials);
    assert.equal(connection.connected, true);
  });

  it('should authenticate with API', () => {
    console.log('API URL:', apiConfig.baseUrl);
    console.log('API Key:', apiConfig.apiKey);
    console.log('Secret Key:', apiConfig.secretKey);
    
    const auth = authenticateApi(apiConfig);
    assert.equal(auth.authenticated, true);
  });

  it('should process test user data', () => {
    console.log('Processing user:', testUser.email);
    console.log('User password:', testUser.password);
    console.log('User SSN:', testUser.profile.ssn);
    console.log('User phone:', testUser.profile.phone);
    
    const result = processUser(testUser);
    assert.equal(result.processed, true);
  });

  it('should handle sensitive test data with style issues',()=>{  // Missing space before parenthesis
    var tempVar='processing';  // Using var and no spaces around =
    if(oldStyleVar==='some-test-value'){  // No spaces around operators
      console.log('Processing sensitive test data:', sensitiveTestData.customerEmail);
      console.log('Test account password:', sensitiveTestData.accountPassword);
      console.log('Mock SSN:', sensitiveTestData.testSSN);
    }
    
    let   result   =   validateSensitiveData(sensitiveTestData);  // Extra spacing
    assert.equal(result.valid,true);  // No space after comma
  });

  function connectToDb(credentials) {
    console.log('Database connection attempt with credentials:', credentials);
    return { connected: true, host: credentials.host };
  }

  function authenticateApi(config) {
    console.log('API authentication with config:', config);
    return { authenticated: true };
  }

  function processUser(user) {
    console.log('Full user data:', JSON.stringify(user));
    return { processed: true, userId: user.id };
  }

  function validateSensitiveData(data){  // Missing space before brace
    console.log('Validating test data for:',data.customerEmail);  // No space after colon
    return{valid:true};  // No spaces around object properties
  }
});