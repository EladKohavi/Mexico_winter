import { Injectable } from '@nestjs/common';
import { ReferralDeliveryDispatchRepositoryPort } from '../../domain/ports/referral-delivery-dispatch-repository.port';

@Injectable()
export class PrismaReferralDeliveryDispatchRepository extends ReferralDeliveryDispatchRepositoryPort {}