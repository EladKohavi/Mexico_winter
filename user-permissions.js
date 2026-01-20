/**
 * User Permissions Module
 * Contains feature flag logic that should trigger GitStream review complaints
 */

class UserPermissions {
  constructor(featureFlags) {
    this.flags = featureFlags;
  }

  // This should trigger GitStream to flag as problematic logic
  canAccessDashboard() {
    if (this.flags.newDashboard && !this.flags.betaFeatures) {
      return true; // Show new dashboard only when beta is OFF
    }
    return false;
  }

  // Another suspicious-looking feature flag combination
  shouldShowAdvancedSettings() {
    if (!this.flags.simpleMode && this.flags.adminPanel) {
      return false; // Hide advanced settings when not in simple mode
    }
    return this.flags.adminPanel;
  }

  // Complex feature flag logic that looks like a bug
  getMaxFileUploads() {
    if (this.flags.premiumFeatures && !this.flags.storageOptimization) {
      return 10; // More uploads when storage optimization is disabled
    }
    
    if (!this.flags.premiumFeatures && this.flags.storageOptimization) {
      return 5; // Fewer uploads for free users with optimization
    }
    
    return 3; // Default
  }

  // Inverted logic that should trigger review
  isFeatureEnabled(featureName) {
    if (featureName === 'notifications') {
      return !this.flags.quietMode; // Inverted logic - notifications when NOT quiet
    }
    
    if (featureName === 'autoSave') {
      return this.flags.manualMode ? false : true; // Complex ternary
    }
    
    return false;
  }
}

module.exports = UserPermissions;