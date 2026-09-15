import clickhouse_connect
import polars as pl

client = clickhouse_connect.get_client(
    host='lp2qum9z4z.ap-south-1.aws.clickhouse.cloud',
    user='default',
    password='JB0dE9p4lCX_z',
    secure=True
)

# GitHub data
result = client.query("SELECT * FROM github_events_cleaned")

df = pl.DataFrame(
    result.result_rows,
    schema=result.column_names,
    orient="row"
)

print("GitHub Data:")
print(df)
print("\nShape:", df.shape)

# Slack data
slack_result = client.query(
    "SELECT * FROM slack_events_cleaned LIMIT 10"
)

slack_df = pl.DataFrame(
    slack_result.result_rows,
    schema=slack_result.column_names,
    orient="row"
)

print("\nSlack Data:")
print(slack_df)
print("Shape:", slack_df.shape)


# IDE data
ide_result = client.query(
    "SELECT * FROM ide_activity_cleaned"
)

ide_df = pl.DataFrame(
    ide_result.result_rows,
    schema=ide_result.column_names,
    orient="row"
)

print("\nIDE Data:")
print(ide_df)
print("Shape:", ide_df.shape)

# Combined developer activity

github_activity = (
    df.group_by("developer_id")
    .len()
    .rename({"len": "github_activity"})
)

slack_activity = (
    slack_df.group_by("developer_id")
    .len()
    .rename({"len": "slack_activity"})
)

ide_activity = (
    ide_df.group_by("developer_id")
    .len()
    .rename({"len": "ide_activity"})
)

# Start with all developer IDs
developers = pl.concat([
    df.select("developer_id"),
    slack_df.select("developer_id"),
    ide_df.select("developer_id")
]).unique()

# Join activity counts
combined = (
    developers
    .join(github_activity, on="developer_id", how="left")
    .join(slack_activity, on="developer_id", how="left")
    .join(ide_activity, on="developer_id", how="left")
    .fill_null(0)
)

# Calculate total activity
combined = combined.with_columns(
    (
        pl.col("github_activity")
        + pl.col("slack_activity")
        + pl.col("ide_activity")
    ).alias("total_activity")
)

combined = combined.sort("total_activity", descending=True)

print("\nDeveloper Activity Summary:")
print(combined)

# IDE activity analysis

ide_summary = (
    ide_df
    .group_by("activity_type")
    .agg([
        pl.len().alias("activity_count"),
        pl.col("duration_minutes").sum().alias("total_duration"),
        pl.col("duration_minutes").mean().round(2).alias("avg_duration")
    ])
    .sort("activity_count", descending=True)
)

print("\nIDE Activity Summary:")
print(ide_summary)

# Developer-wise IDE activity and time

developer_ide_summary = (
    ide_df
    .group_by("developer_id")
    .agg([
        pl.len().alias("ide_activity_count"),
        pl.col("duration_minutes").sum().alias("total_coding_minutes"),
        pl.col("duration_minutes").mean().round(2).alias("avg_activity_duration")
    ])
    .sort("total_coding_minutes", descending=True)
)

print("\nDeveloper IDE Summary:")
print(developer_ide_summary)

# Final Developer Analytics

final_summary = (
    combined
    .join(
        developer_ide_summary,
        on="developer_id",
        how="left"
    )
    .fill_null(0)
)

# Activity intensity
final_summary = final_summary.with_columns(
    (
        pl.col("total_activity") +
        pl.col("ide_activity_count")
    ).alias("activity_intensity")
)

# Sort developers by activity intensity
final_summary = final_summary.sort(
    "activity_intensity",
    descending=True
)

print("\nFinal Developer Analytics:")
print(final_summary)

# Save final analytics for dashboard/API

final_summary.write_csv(
    "final_developer_analytics.csv"
)

print("\nFinal analytics saved successfully!")