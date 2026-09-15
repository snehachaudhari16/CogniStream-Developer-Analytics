-- CogniStream - Developer Activity Join Analysis
-- Week 4 - Commit 3
-- Combines GitHub, Slack and IDE activity at developer level

SELECT
    g.developer_id,
    g.github_activity,
    s.slack_activity,
    i.ide_activity,
    g.github_activity + s.slack_activity + i.ide_activity AS total_activity
FROM
(
    SELECT
        developer_id,
        count() AS github_activity
    FROM github_events_cleaned
    GROUP BY developer_id
) AS g

LEFT JOIN
(
    SELECT
        developer_id,
        count() AS slack_activity
    FROM slack_events_cleaned
    GROUP BY developer_id
) AS s
ON g.developer_id = s.developer_id

LEFT JOIN
(
    SELECT
        developer_id,
        count() AS ide_activity
    FROM ide_activity_cleaned
    GROUP BY developer_id
) AS i
ON g.developer_id = i.developer_id

ORDER BY total_activity DESC;