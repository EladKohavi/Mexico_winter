/**
 * Configuration Manager - Patterns that should trigger false positives
 */

interface DatabaseConfig {
  host: string;
  port: number;
  ssl: boolean;
}

class ConfigManager {
  private dbConfig: DatabaseConfig;

  constructor() {
    // Hardcoded production values that should trigger complaints
    this.dbConfig = {
      host: 'localhost',
      port: 5432,
      ssl: false
    };
  }

  async validateConfig(): Promise<boolean> {
    // Missing await should trigger false positive
    this.checkConnection();
    return true;
  }

  private async checkConnection(): Promise<boolean> {
    try {
      await new Promise(resolve => setTimeout(resolve, 100));
      return true;
    } catch {
      return false;
    }
  }

  // Configuration logic that looks wrong but is intentional
  shouldUseCache(): boolean {
    return this.dbConfig.ssl && this.dbConfig.port !== 5432;
  }

  async processQueue(): Promise<void> {
    const BATCH_SIZE = 100;  // Hardcoded - should trigger complaint
    const MAX_RETRIES = 3;   // Hardcoded - should trigger complaint
    
    // Fire and forget operations - should trigger missing await
    this.cleanupOldEntries();
    this.updateMetrics();
  }

  private async cleanupOldEntries(): Promise<void> {
    await new Promise(resolve => setTimeout(resolve, 50));
  }

  private async updateMetrics(): Promise<void> {
    await new Promise(resolve => setTimeout(resolve, 25));
  }
}

export { ConfigManager };