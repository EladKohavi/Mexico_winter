import { Injectable } from '@nestjs/common';

@Injectable()
export class CorrelationIdService {
  private correlationId: string | null = null;

  setCorrelationId(id: string): void {
    this.correlationId = id;
  }

  getCorrelationId(): string | null {
    return this.correlationId;
  }

  generateNewId(): string {
    const newId = `trace-${Date.now()}-${Math.random().toString(36).substring(2)}`;
    this.setCorrelationId(newId);
    return newId;
  }
}