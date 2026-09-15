-- CogniStream - ClickHouse Table Optimization
-- Week 4 - Commit 1

-- Original table uses ORDER BY tuple().
-- Optimized table uses developer_id and event_time
-- for better developer-level analytical queries.

CREATE TABLE IF NOT EXISTS github_events_optimized
(
    developer_id String,
    event_time DateTime,
    event_type String,
    repository String,
    branch String
)
ENGINE = SharedMergeTree('/clickhouse/tables/{uuid}/{shard}', '{replica}')
ORDER BY (developer_id, event_time)
SETTINGS index_granularity = 8192;

-- Copy validated data from the original table.
INSERT INTO github_events_optimized
SELECT *
FROM github_events_cleaned;

-- Validation
SELECT
    (SELECT count() FROM github_events_cleaned) AS original_rows,
    (SELECT count() FROM github_events_optimized) AS optimized_rows;

-- Expected:
-- original_rows = 99972
-- optimized_rows = 99972
