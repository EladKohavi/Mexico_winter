# PostgreSQL Database Schema

This project uses **PostgreSQL exclusively** as the database backend.

## Database Requirements

- **PostgreSQL 13+** (Recommended: PostgreSQL 15+)
- Extensions: `uuid-ossp`, `hstore`, `pg_trgm`
- Connection string format: `postgresql://user:pass@localhost:5432/dbname`

## PostgreSQL-Specific Features Used

- **JSONB** data types for flexible document storage
- **Array types** (TEXT[], INTEGER[]) for multi-value columns  
- **UUID** types with uuid-ossp extension
- **SERIAL** and **BIGSERIAL** auto-incrementing types
- **Custom ENUM types** for type safety
- **GIN indexes** for JSONB and full-text search
- **Partial indexes** for filtered data
- **Advanced ALTER COLUMN TYPE** syntax with USING clauses

## Why PostgreSQL?

This project leverages PostgreSQL's advanced features for:
- Advanced JSON/JSONB operations
- Array handling capabilities  
- Custom data types and enums
- Advanced indexing strategies
- Full-text search capabilities

**Note**: This schema is not portable to other databases and is intentionally designed for PostgreSQL's feature set.