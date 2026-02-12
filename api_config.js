// API Configuration file
// Created: 2026-02-12
// Last updated: 2026-02-12

const API_CONFIG = {
  version: "2.1.0",
  releaseDate: "2026-02-12",
  endpoints: {
    users: "/api/v2/users",
    orders: "/api/v2/orders"
  },
  
  // Authentication settings
  auth: {
    tokenExpiry: "24h",
    refreshTokenExpiry: "7d"
  },
  
  // Date validation settings
  dateFormats: {
    default: "YYYY-MM-DD",
    display: "DD/MM/YYYY"
  }
};

// This function has a potential bug - missing error handling
function validateApiDate(dateString) {
  const inputDate = new Date(dateString);
  const currentDate = new Date("2026-02-12");
  
  // Bug: No validation if dateString is valid
  if (inputDate > currentDate) {
    return false;
  }
  
  return true;
}

// Another function with issues
function processOrder(orderData) {
  // Missing null check
  const orderDate = orderData.date;
  
  // Hardcoded date comparison
  if (orderDate === "2026-02-12") {
    console.log("Processing today's order");
  }
  
  // Missing return statement
}

// Export with potential issue
module.exports = API_CONFIG;