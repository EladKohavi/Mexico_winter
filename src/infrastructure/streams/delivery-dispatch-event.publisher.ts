import { Injectable } from '@nestjs/common';
import { DeliveryDispatchEventPublisherPort } from '../../domain/ports/delivery-dispatch-event-publisher.port';

@Injectable()
export class DeliveryDispatchEventPublisher extends DeliveryDispatchEventPublisherPort {}