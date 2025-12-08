// TypeScript test file with PII and style issues
import { expect } from 'chai';

interface TestUser {
  email: string;
  password: string;
  ssn?: string;
}

describe('Authentication Service', () => {
  const mockUsers: TestUser[] = [
    {
      email: 'test@example.com',     // Should trigger PII protection
      password: 'password123',       // Should trigger PII protection  
      ssn: '987-65-4321'            // Should trigger PII protection
    },
    {
      email: 'admin@test.com',       // Should trigger PII protection
      password: 'admin456'           // Should trigger PII protection
    }
  ];

  it('should authenticate valid user', () => {
    const user = mockUsers[0];
    
    // Poor style formatting
    if(user.email&&user.password){
      console.log('Authenticating user: ' + user.email); // Should trigger logging enhancement
      const result = authenticate(user);
      expect(result).to.be.true;
    }
  });

  it('should reject invalid credentials', () => {
    const invalidUser = { email: 'bad@example.com', password: 'wrong' };
    console.log('Testing invalid credentials for:', invalidUser.email); // Should trigger logging enhancement
    
    const result = authenticate(invalidUser);
    expect(result).to.be.false;
  });
  
  function authenticate(user: TestUser): boolean {
    // Simple mock authentication
    return mockUsers.some(u => u.email === user.email && u.password === user.password);
  }
});