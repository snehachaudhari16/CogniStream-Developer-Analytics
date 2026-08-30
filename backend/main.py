from fastapi import FastAPI

app = FastAPI(title="CogniStream API")


@app.get("/")
def home():
    return {
        "message": "CogniStream API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/developers")
def get_developers():
    return {
        "message": "Developer API is working"
    }


@app.get("/github-events")
def get_github_events():
    return {
        "message": "GitHub Events API is working"
    }


@app.get("/slack-events")
def get_slack_events():
    return {
        "message": "Slack Events API is working"
    }


@app.get("/ide-activity")
def get_ide_activity():
    return {
        "message": "IDE Activity API is working"
    }
