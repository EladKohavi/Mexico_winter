-- Setup analytics tables
-- This script sets up analytics tracking

-- Create analytics table
CREATE TABLE analytics_events (
    id SERIAL PRIMARY KEY,
    event_id UUID DEFAULT gen_random_uuid(),
    user_data JSONB,
    event_tags TEXT[],
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Modify column types
ALTER TABLE analytics_events ALTER COLUMN user_data TYPE JSONB;

-- Create custom types
CREATE TYPE priority_level AS ENUM ('low', 'medium', 'high', 'critical');
ALTER TABLE analytics_events ADD COLUMN priority priority_level DEFAULT 'medium';

-- Add array column
ALTER TABLE analytics_events ADD COLUMN categories TEXT[] DEFAULT '{}';

-- Create advanced indexes
CREATE INDEX idx_analytics_jsonb ON analytics_events USING GIN (user_data);
CREATE INDEX idx_analytics_tags ON analytics_events USING GIN (event_tags);

-- Partial index
CREATE INDEX idx_high_priority ON analytics_events (created_at) 
WHERE priority IN ('high', 'critical');

-- Update with JSONB operations
UPDATE analytics_events 
SET user_data = user_data || '{"processed": true}'::JSONB 
WHERE user_data ? 'user_id';