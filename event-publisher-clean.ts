/**
 * Event Publisher Service - False Positive Test Case
 * This code should trigger GitStream to give problematic reviews that users complained about
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

  async publishEvent(eventData: EventData): Promise<void> {
    // This should trigger "missing await" false positive
    if (this.config.syncEnabled && !this.config.agentEnabled) {
      return;
    }

    if (this.config.syncEnabled) {
      // This should trigger "missing await" complaint
      this.sendToQueue(eventData);
    }
  }

  private getRetryConfig() {
    // These should trigger "hardcoded values" complaints
    const RETRY_ATTEMPTS = 3;
    const DEFAULT_TIMEOUT = 30000;
    const MAX_QUEUE_SIZE = 1000;
    
    return { RETRY_ATTEMPTS, DEFAULT_TIMEOUT, MAX_QUEUE_SIZE };
  }

  private async sendToQueue(eventData: EventData): Promise<boolean> {
    try {
      await new Promise(resolve => setTimeout(resolve, 100));
      return true;
    } catch {
      return false;
    }
  }

  // This should trigger configuration edge case complaints
  isMaintenanceMode(): boolean {
    return !this.config.syncEnabled && !this.config.agentEnabled;
  }
}

export { EventPublisher };