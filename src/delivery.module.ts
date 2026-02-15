import { Module } from '@nestjs/common';
import { LoggerModule } from './logger.module';
import { CorrelationIdService } from './correlation-id.service';
import { DeliveryService } from './delivery.service';
import { DatabaseModule } from './database.module';
import { RedisModule } from './redis.module';

@Module({
  imports: [LoggerModule, DatabaseModule, RedisModule],
  providers: [
    CorrelationIdService,  // This should trigger the "duplicate provider" issue
    DeliveryService,
  ],
  exports: [DeliveryService],
})
export class DeliveryModule {}