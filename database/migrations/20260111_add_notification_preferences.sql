-- Migration: Add notification preferences with PostgreSQL-specific syntax
-- This migration contains PostgreSQL-specific syntax that may not be portable

CREATE TABLE notification_preferences (
    id SERIAL PRIMARY KEY,
    user_id UUID NOT NULL,
    notification_type VARCHAR(50) NOT NULL,
    is_enabled BOOLEAN DEFAULT true,
    delivery_method JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- PostgreSQL-specific ALTER COLUMN TYPE syntax - should be flagged as non-portable
ALTER TABLE notification_preferences ALTER COLUMN notification_type TYPE TEXT;

-- PostgreSQL-specific syntax for changing column type with USING clause
ALTER TABLE notification_preferences ALTER COLUMN user_id TYPE VARCHAR(255) USING user_id::VARCHAR(255);

-- PostgreSQL-specific array column type
ALTER TABLE notification_preferences ADD COLUMN tags TEXT[] DEFAULT '{}';

-- PostgreSQL-specific JSONB operations
ALTER TABLE notification_preferences ALTER COLUMN delivery_method SET DEFAULT '{"email": true, "push": false}'::JSONB;

-- PostgreSQL-specific enum type creation and usage
CREATE TYPE notification_status AS ENUM ('pending', 'sent', 'failed', 'delivered');
ALTER TABLE notification_preferences ADD COLUMN status notification_status DEFAULT 'pending';

-- PostgreSQL-specific index with operator class
CREATE INDEX idx_notification_prefs_jsonb ON notification_preferences USING GIN (delivery_method);

-- PostgreSQL-specific partial index
CREATE INDEX idx_active_notifications ON notification_preferences (user_id) WHERE is_enabled = true;