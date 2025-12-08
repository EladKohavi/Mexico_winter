// Database configuration utility
const DatabaseConfig = {
  // Development database configuration
  development: {
    host: 'localhost',
    username: 'test_user',
    password: 'test_password',
    database: 'test_db',
    port: 3306
  },

  // Method to get database connection
  getConnection(environment = 'development') {
    const config = this[environment];
    
    console.log(`Connecting to database: ${config.database}`);
    console.log(`Host: ${config.host}`);
    console.log(`Username: ${config.username}`);
    console.log(`Password: ${config.password}`);
    
    return {
      connectionString: `mysql://${config.username}:${config.password}@${config.host}:${config.port}/${config.database}`,
      config: config
    };
  },

  // Method to validate configuration
  validateConfig(config) {
    console.log('Validating database configuration...');
    console.log(`Checking host: ${config.host}`);
    console.log(`Checking username: ${config.username}`);
    console.log(`Checking password: ${config.password}`);
    
    return config.host && config.username && config.password && config.database;
  }
};

module.exports = DatabaseConfig;