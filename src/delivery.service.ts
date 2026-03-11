import { Injectable } from '@nestjs/common';
import { CorrelationIdService } from './correlation-id.service';

@Injectable()
export class DeliveryService {
  constructor(private correlationIdService: CorrelationIdService) {}

  async processDelivery(orderId: string): Promise<boolean> {
    const correlationId = this.correlationIdService.generateNewId();
    console.log(`Processing delivery for order ${orderId} with correlation ID: ${correlationId}`);
    
    // Simulate delivery processing
    await this.simulateDeliveryWork();
    
    return true;
  }

  private async simulateDeliveryWork(): Promise<void> {
    return new Promise(resolve => {
      setTimeout(() => {
        console.log('Delivery processing completed');
        resolve();
      }, 1000);
    });
  }
}