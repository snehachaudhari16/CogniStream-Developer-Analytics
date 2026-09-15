from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CogniStream API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "CogniStream API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/developers")
def get_developers():
    return [
        {
            "name": "Shahana",
            "project": "Frontend",
            "status": "In Progress",
            "last_commit": "20 mins ago"
        },
        {
            "name": "Rinsha",
            "project": "Backend",
            "status": "Completed",
            "last_commit": "10 mins ago"
        },
        {
            "name": "Sneha",
            "project": "API",
            "status": "Completed",
            "last_commit": "35 mins ago"
        },
        {
            "name": "Rishana",
            "project": "Testing",
            "status": "Review",
            "last_commit": "1 hour ago"
        }
    ]


@app.get("/commits")
def get_commits():
    return [
        {"day": "Mon", "commits": 12},
        {"day": "Tue", "commits": 18},
        {"day": "Wed", "commits": 10},
        {"day": "Thu", "commits": 22},
        {"day": "Fri", "commits": 15}
    ]


@app.get("/github-events")
def github_events():
    return {"message": "GitHub Events API is working"}


@app.get("/slack-events")
def slack_events():
    return {"message": "Slack Events API is working"}


@app.get("/ide-activity")
def ide_activity():
    return {"message": "IDE Activity API is working"}