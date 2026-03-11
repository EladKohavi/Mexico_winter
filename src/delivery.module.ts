import { Module } from '@nestjs/common';
import { AppConfigModule } from './app-config.module';
import { LoggerModule } from './logger.module';
import { DatabaseModule } from './database.module';
import { RedisModule } from './redis.module';
import { CustomerModule } from './customer.module';
import { ReferralModule } from './referral.module';
import { UapiModule } from './uapi.module';
import { ReferralDeliveryDispatchRepositoryPort } from './domain/ports/referral-delivery-dispatch-repository.port';
import { PrismaReferralDeliveryDispatchRepository } from './infrastructure/persistence/prisma-referral-delivery-dispatch.repository';
import { DeliveryDispatchEventPublisherPort } from './domain/ports/delivery-dispatch-event-publisher.port';
import { DeliveryDispatchEventPublisher } from './infrastructure/streams/delivery-dispatch-event.publisher';
import { CartNotificationDeliveryPort } from './domain/ports/cart-notification-delivery.port';
import { LoggingCartNotificationDeliveryAdapter } from './infrastructure/delivery/logging-cart-notification-delivery.adapter';
import { CreateDeliveryDispatchesOnRequestCompletionUseCase } from './application/commands/create-delivery-dispatches-on-request-completion.use-case';
import { ProcessCartNotificationDeliveryUseCase } from './application/commands/process-cart-notification-delivery.use-case';
import { ProcessCartNotificationDeliveryGroupUseCase } from './application/commands/process-cart-notification-delivery-group.use-case';
import { RequestCompletedConsumer } from './infrastructure/consumers/request-completed.consumer';
import { DeliveryDispatchConsumer } from './infrastructure/consumers/delivery-dispatch.consumer';
import { CorrelationIdService } from './correlation-id.service';

@Module({
  imports: [AppConfigModule, LoggerModule, DatabaseModule, RedisModule, CustomerModule, ReferralModule, UapiModule],
  providers: [
    CorrelationIdService,
    PrismaReferralDeliveryDispatchRepository,
    {
      provide: ReferralDeliveryDispatchRepositoryPort,
      useExisting: PrismaReferralDeliveryDispatchRepository,
    },
    DeliveryDispatchEventPublisher,
    {
      provide: DeliveryDispatchEventPublisherPort,
      useExisting: DeliveryDispatchEventPublisher,
    },
    {
      provide: CartNotificationDeliveryPort,
      useClass: LoggingCartNotificationDeliveryAdapter,
    },
    CreateDeliveryDispatchesOnRequestCompletionUseCase,
    ProcessCartNotificationDeliveryUseCase,
    ProcessCartNotificationDeliveryGroupUseCase,
    RequestCompletedConsumer,
    DeliveryDispatchConsumer,
  ],
  exports: [],
})
export class ReferralDeliveryModule {}