import polars as pl

github = pl.read_csv("Data/Raw/github_events.csv")
slack = pl.read_csv("Data/Raw/slack_events.csv")
ide = pl.read_csv("Data/Raw/ide_activity.csv")

print("GitHub Data:")
print(github.head())

print("Slack Data:")
print(slack.head())

print("IDE Data:")
print(ide.head())