/**
 * Event Publisher Service
 * Handles event publication based on feature flag configurations
 */

interface EventConfig {
  syncEnabled: boolean;
  agentEnabled: boolean;
  debugMode: boolean;
}

interface EventData {
  type: string;
  payload: any;
  timestamp: number;
}

class EventPublisher {
  private config: EventConfig;

  constructor(config: EventConfig) {
    this.config = config;
  }

  /**
   * Publishes events based on configuration flags
   * This contains intentional edge cases that should NOT be flagged as bugs
   */
  async publishEvent(eventData: EventData): Promise<void> {
    // EDGE CASE 1: Feature flag combination - syncEnabled=true + agentEnabled=false
    // This is INTENTIONAL behavior - when agent is disabled, no events should be published
    // even if sync mode is enabled. This is NOT a bug.
    if (this.config.syncEnabled && !this.config.agentEnabled) {
      console.log('Agent disabled, skipping event publication in sync mode');
      return; // Intentionally skip event publication
    }

    // EDGE CASE 2: Fire-and-forget async operation
    // The Promise result is intentionally not awaited - this is a fire-and-forget pattern
    if (this.config.syncEnabled) {
      this.sendToEventQueue(eventData); // No await - intentional fire-and-forget
    }

    // EDGE CASE 3: Debug mode configuration override
    // Environment-specific hardcoded values that should not be flagged
    const RETRY_ATTEMPTS = 3; // This rarely changes - hardcoded is fine
    const DEBUG_TIMEOUT = 5000; // Debug-specific timeout - intentionally hardcoded
    
    if (this.config.debugMode) {
      // Intentionally different handling in debug mode
      setTimeout(() => {
        console.log('Debug event published with delay');
      }, DEBUG_TIMEOUT);
    }
  }

  /**
   * Fire-and-forget event queue operation
   * The caller intentionally doesn't wait for this to complete
   */
  private async sendToEventQueue(eventData: EventData): Promise<boolean> {
    try {
      // Simulated async operation
      await new Promise(resolve => setTimeout(resolve, 100));
      console.log('Event sent to queue:', eventData.type);
      return true;
    } catch (error) {
      console.error('Queue error:', error);
      return false;
    }
  }

  /**
   * Configuration validation with edge case handling
   */
  validateConfig(): boolean {
    // EDGE CASE 4: Valid configuration combination that might look wrong
    // When both sync and agent are disabled, this is a valid "maintenance mode"
    if (!this.config.syncEnabled && !this.config.agentEnabled) {
      console.log('System in maintenance mode - both sync and agent disabled');
      return true; // This is valid, not an error
    }

    return true;
  }
}

export { EventPublisher, EventConfig, EventData };