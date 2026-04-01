-- PostgreSQL Migration: Advanced Analytics Schema
-- This migration is designed exclusively for PostgreSQL
-- Requires: PostgreSQL 13+, uuid-ossp extension

-- Enable required PostgreSQL extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Create custom PostgreSQL ENUM types
CREATE TYPE user_status AS ENUM ('active', 'inactive', 'suspended', 'pending');
CREATE TYPE event_category AS ENUM ('click', 'view', 'purchase', 'signup', 'login');

-- Advanced user analytics table using PostgreSQL-specific features
CREATE TABLE user_analytics (
    id BIGSERIAL PRIMARY KEY,
    user_id UUID DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL,
    user_status user_status DEFAULT 'active',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Event tracking with JSONB and array types (PostgreSQL-specific)
CREATE TABLE event_tracking (
    id BIGSERIAL PRIMARY KEY,
    user_id UUID REFERENCES user_analytics(user_id),
    event_category event_category NOT NULL,
    event_data JSONB DEFAULT '{}',
    tags TEXT[] DEFAULT '{}',
    ip_addresses INET[] DEFAULT '{}',
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Use PostgreSQL ALTER COLUMN TYPE syntax with USING clause
ALTER TABLE user_analytics ALTER COLUMN session_id TYPE TEXT USING session_id::TEXT;

-- Add advanced PostgreSQL indexes
CREATE INDEX idx_user_analytics_jsonb ON event_tracking USING GIN (event_data);
CREATE INDEX idx_event_tags ON event_tracking USING GIN (tags);
CREATE INDEX idx_user_status ON user_analytics (user_status) WHERE user_status = 'active';

-- PostgreSQL-specific full-text search index
CREATE INDEX idx_metadata_search ON event_tracking USING GIN (to_tsvector('english', metadata::text));

-- Advanced PostgreSQL view with JSONB operations
CREATE OR REPLACE VIEW active_user_events AS
SELECT 
    ua.user_id,
    ua.user_status,
    et.event_category,
    et.event_data->'properties'->>'page' as page_visited,
    array_length(et.tags, 1) as tag_count,
    et.created_at
FROM user_analytics ua
JOIN event_tracking et ON ua.user_id = et.user_id
WHERE ua.user_status = 'active'
  AND et.event_data ? 'properties';

-- PostgreSQL-specific trigger function
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create trigger (PostgreSQL syntax)
CREATE TRIGGER update_user_analytics_updated_at
    BEFORE UPDATE ON user_analytics
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();