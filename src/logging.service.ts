import { Injectable } from '@nestjs/common';
import { CorrelationIdService } from './correlation-id.service';

@Injectable()
export class LoggingService {
  constructor(private correlationIdService: CorrelationIdService) {}

  log(message: string): void {
    const correlationId = this.correlationIdService.getCorrelationId();
    console.log(`[${correlationId}] ${message}`);
  }

  error(message: string, error?: Error): void {
    const correlationId = this.correlationIdService.getCorrelationId();
    console.error(`[${correlationId}] ERROR: ${message}`, error);
  }
}