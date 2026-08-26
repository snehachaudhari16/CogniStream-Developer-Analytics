import polars as pl

github = pl.read_csv("Data/Cleaned/github_events_cleaned.csv")
slack = pl.read_csv("Data/Cleaned/slack_events_cleaned.csv")
ide = pl.read_csv("Data/Cleaned/ide_activity_cleaned.csv")

print("GitHub Shape:", github.shape)
print("Slack Shape:", slack.shape)
print("IDE Shape:", ide.shape)

print("\nGitHub Columns:")
print(github.columns)

print("\nSlack Columns:")
print(slack.columns)

print("\nIDE Columns:")
print(ide.columns)

print("\nGitHub Event Types:")
print(github.group_by("event_type").len().sort("len", descending=True))

print("\nSlack Message Types:")
print(slack.group_by("message_type").len().sort("len", descending=True))

print("\nIDE Activity Types:")
print(ide.group_by("activity_type").len().sort("len", descending=True))

print("\nProgramming Languages:")
print(ide.group_by("language").len().sort("len", descending=True))

print("\nDeveloper GitHub Activity:")
print(github.group_by("developer_id").len().sort("len", descending=True).head(10))

print("\nDeveloper Slack Activity:")
print(slack.group_by("developer_id").len().sort("len", descending=True).head(10))

print("\nDeveloper IDE Time:")
print(
    ide.group_by("developer_id")
    .agg(pl.col("duration_minutes").sum().alias("total_minutes"))
    .sort("total_minutes", descending=True)
    .head(10)
)
developer_summary.write_csv("Data/final_developer_analytics.csv")
print("Final developer analytics saved successfully.")
