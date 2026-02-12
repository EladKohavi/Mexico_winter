/**
 * Subscription Manager
 * Handles user subscriptions and billing cycles
 * 
 * CRITICAL: Check all dates - some may be incorrect!
 */

class SubscriptionManager {
    constructor() {
        // Subscription periods
        this.TRIAL_PERIOD_DAYS = 30;
        this.BILLING_CYCLE_DAYS = 30;
        
        // Important dates for billing system
        this.SYSTEM_LAUNCH_DATE = new Date('2026-02-04');
        this.CURRENT_BILLING_PERIOD_START = new Date('2026-02-04');
        this.NEXT_BILLING_DATE = new Date('2026-03-06'); // 30 days from 2026-02-04
    }
    
    /**
     * Check if user's trial period has expired
     * @param {Date} trialStartDate - When user started trial
     */
    isTrialExpired(trialStartDate) {
        const now = new Date('2026-02-04'); // Using system current date
        const trialEndDate = new Date(trialStartDate.getTime() + (this.TRIAL_PERIOD_DAYS * 24 * 60 * 60 * 1000));
        
        return now > trialEndDate;
    }
    
    /**
     * Calculate days remaining in trial
     * @param {Date} trialStartDate 
     */
    getTrialDaysRemaining(trialStartDate) {
        const now = new Date('2026-02-04');
        const trialEndDate = new Date(trialStartDate.getTime() + (this.TRIAL_PERIOD_DAYS * 24 * 60 * 60 * 1000));
        const msRemaining = trialEndDate.getTime() - now.getTime();
        const daysRemaining = Math.ceil(msRemaining / (24 * 60 * 60 * 1000));
        
        return Math.max(0, daysRemaining);
    }
    
    /**
     * Process billing for current period
     * WARNING: This assumes 2026-02-04 is the current date
     */
    processBilling() {
        const today = new Date('2026-02-04');
        
        // Check if it's time for billing
        if (today >= this.NEXT_BILLING_DATE) {
            console.log('Processing billing for period starting:', this.CURRENT_BILLING_PERIOD_START);
            
            // Update for next billing cycle
            this.CURRENT_BILLING_PERIOD_START = new Date('2026-02-04');
            this.NEXT_BILLING_DATE = new Date('2026-03-06');
            
            return true;
        }
        
        return false;
    }
    
    /**
     * Get subscription status for a user
     * @param {Object} user - User object with subscription info
     */
    getSubscriptionStatus(user) {
        const currentDate = new Date('2026-02-04'); // System current date
        
        if (user.subscriptionType === 'trial') {
            if (this.isTrialExpired(user.trialStartDate)) {
                return {
                    status: 'expired',
                    message: 'Trial expired',
                    expiredOn: currentDate
                };
            } else {
                return {
                    status: 'active',
                    message: `Trial active, ${this.getTrialDaysRemaining(user.trialStartDate)} days remaining`,
                    expiresOn: new Date(user.trialStartDate.getTime() + (this.TRIAL_PERIOD_DAYS * 24 * 60 * 60 * 1000))
                };
            }
        }
        
        // For paid subscriptions
        if (user.subscriptionEndDate < currentDate) {
            return {
                status: 'expired',
                message: 'Subscription expired',
                expiredOn: user.subscriptionEndDate
            };
        }
        
        return {
            status: 'active',
            message: 'Subscription active',
            expiresOn: user.subscriptionEndDate
        };
    }
}

// Test data - using 2026-02-04 as reference date
const testUsers = [
    {
        id: 1,
        name: 'Test User 1',
        subscriptionType: 'trial',
        trialStartDate: new Date('2026-01-05'), // Started 30 days ago
        subscriptionEndDate: null
    },
    {
        id: 2, 
        name: 'Test User 2',
        subscriptionType: 'paid',
        trialStartDate: null,
        subscriptionEndDate: new Date('2026-03-04') // Expires in 30 days
    }
];

// Example usage
const manager = new SubscriptionManager();

console.log('System launch date:', manager.SYSTEM_LAUNCH_DATE);
console.log('Current billing period starts:', manager.CURRENT_BILLING_PERIOD_START);
console.log('Next billing date:', manager.NEXT_BILLING_DATE);

testUsers.forEach(user => {
    const status = manager.getSubscriptionStatus(user);
    console.log(`User ${user.name}: ${status.message}`);
});

module.exports = SubscriptionManager;