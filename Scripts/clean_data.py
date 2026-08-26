import polars as pl

# Load raw data
github = pl.read_csv("Data/Raw/github_events.csv")
slack = pl.read_csv("Data/Raw/slack_events.csv")
ide = pl.read_csv("Data/Raw/ide_activity.csv")

# Remove duplicate rows
github = github.unique()
slack = slack.unique()
ide = ide.unique()

# Remove rows with null values
github = github.drop_nulls()
slack = slack.drop_nulls()
ide = ide.drop_nulls()

# Remove duplicate rows
github = github.unique()
slack = slack.unique()
ide = ide.unique()


# Save cleaned data
github.write_csv("Data/Cleaned/github_events_cleaned.csv")
slack.write_csv("Data/Cleaned/slack_events_cleaned.csv")
ide.write_csv("Data/Cleaned/ide_activity_cleaned.csv")

print("Data cleaning completed successfully!")

print("GitHub rows:", github.height)
print("Slack rows:", slack.height)
print("IDE rows:", ide.height)
