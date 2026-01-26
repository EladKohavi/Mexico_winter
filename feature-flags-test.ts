/**
 * Feature Flag Test - Should trigger GitStream false positive
 */

interface FeatureFlags {
  enableNewUI: boolean;
  enableBetaFeatures: boolean;
  enableAnalytics: boolean;
  enableCache: boolean;
}

class FeatureFlagManager {
  private flags: FeatureFlags;

  constructor(flags: FeatureFlags) {
    this.flags = flags;
  }

  // This pattern should trigger GitStream to complain about the logic
  shouldShowNewDashboard(): boolean {
    // Users complained GitStream flags this as a bug
    if (this.flags.enableNewUI && !this.flags.enableBetaFeatures) {
      return true; // Show new UI only when beta features are disabled
    }
    return false;
  }

  // Another pattern that should trigger complaints
  canAccessPremiumFeatures(): boolean {
    // GitStream should flag this as suspicious logic
    if (!this.flags.enableBetaFeatures && this.flags.enableAnalytics) {
      return true; // Premium access when beta disabled but analytics enabled
    }
    return false;
  }

  // Cache logic that looks wrong but is intentional
  shouldUseCache(): boolean {
    // This should trigger "suspicious condition" complaint
    if (this.flags.enableCache && !this.flags.enableNewUI) {
      return false; // Disable cache for old UI intentionally
    }
    return this.flags.enableCache;
  }

  // Multiple flag combination that should look suspicious to GitStream
  getFeatureAccessLevel(): string {
    if (this.flags.enableNewUI && !this.flags.enableBetaFeatures && this.flags.enableAnalytics) {
      return "premium"; // Complex condition that should trigger review
    }
    
    if (!this.flags.enableNewUI && this.flags.enableBetaFeatures) {
      return "beta"; // Another suspicious-looking combination
    }
    
    return "basic";
  }
}

export { FeatureFlagManager };