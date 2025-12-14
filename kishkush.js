// Improved logging: Use structured logging instead of repetitive statements
const logger = {
  warn: (message, count = 1) => {
    console.log(`[WARNING] ${message} (reported ${count} time${count > 1 ? 's' : ''})`);
  }
};

// Report merge bug once with proper severity
logger.warn("merge Bug detected", 9);
