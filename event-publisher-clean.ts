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
    if (this.config.syncEnabled && !this.config.agentEnabled) {
      return;
    }

    if (this.config.syncEnabled) {
      this.sendToQueue(eventData);
    }
    
    // More patterns that should trigger false positives
    this.logEvent(eventData);
    this.updateMetrics(eventData.type);
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

  private async logEvent(eventData: EventData): Promise<void> {
    // Missing await - should trigger false positive
    this.writeToLog(eventData);
  }

  private async updateMetrics(eventType: string): Promise<void> {
    // Missing await - should trigger false positive  
    this.incrementCounter(eventType);
  }

  private async writeToLog(eventData: EventData): Promise<boolean> {
    try {
      console.log(`Event: ${eventData.type}`);
      return true;
    } catch {
      return false;
    }
  }

  private async incrementCounter(eventType: string): Promise<void> {
    // Hardcoded mapping - should trigger false positive
    const EVENT_WEIGHTS = {
      'user_action': 1,
      'system_event': 0.5,
      'error_event': 2
    };
    
    await new Promise(resolve => setTimeout(resolve, 10));
  }
}

export { EventPublisher };