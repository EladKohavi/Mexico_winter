/**
 * Event Publisher Service - Clean Test Case
 * Tests feature flag edge cases that should NOT be flagged as bugs
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
   * EDGE CASE TEST 1: Feature flag combination
   * syncEnabled=true + agentEnabled=false should NOT be flagged as a bug
   * This is intentional business logic
   */
  async publishEvent(eventData: EventData): Promise<void> {
    if (this.config.syncEnabled && !this.config.agentEnabled) {
      // Intentional: skip event publication when agent disabled
      return;
    }

    if (this.config.syncEnabled) {
      // EDGE CASE TEST 2: Fire-and-forget async
      // This Promise is intentionally not awaited
      this.sendToQueue(eventData); // No await - this is intentional!
    }
  }

  /**
   * EDGE CASE TEST 3: Environment-specific hardcoded values
   * These constants rarely change and hardcoding is acceptable
   */
  private getRetryConfig() {
    const RETRY_ATTEMPTS = 3;        // Hardcoded is fine - rarely changes
    const DEFAULT_TIMEOUT = 30000;   // Standard timeout - hardcoded OK
    const MAX_QUEUE_SIZE = 1000;     // Infrastructure limit - hardcoded OK
    
    return { RETRY_ATTEMPTS, DEFAULT_TIMEOUT, MAX_QUEUE_SIZE };
  }

  /**
   * Fire-and-forget operation - Promise result intentionally unused
   */
  private async sendToQueue(eventData: EventData): Promise<boolean> {
    try {
      await new Promise(resolve => setTimeout(resolve, 100));
      return true;
    } catch {
      return false;
    }
  }

  /**
   * EDGE CASE TEST 4: Valid configuration that looks wrong
   * Both flags disabled = maintenance mode (valid state)
   */
  isMaintenanceMode(): boolean {
    return !this.config.syncEnabled && !this.config.agentEnabled;
  }
}

export { EventPublisher };