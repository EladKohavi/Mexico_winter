import { Injectable } from '@nestjs/common';
import { CartNotificationDeliveryPort } from '../../domain/ports/cart-notification-delivery.port';

@Injectable()
export class LoggingCartNotificationDeliveryAdapter extends CartNotificationDeliveryPort {}