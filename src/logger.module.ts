import { Module } from '@nestjs/common';
import { CorrelationIdService } from './correlation-id.service';
import { LoggingService } from './logging.service';

@Module({
  providers: [CorrelationIdService, LoggingService],
  exports: [CorrelationIdService, LoggingService],
})
export class LoggerModule {}