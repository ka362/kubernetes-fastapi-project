from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Kubernetes FastAPI Application Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/incidents")
def incidents():
    return {
        "total_incidents": 3,
        "open": 2,
        "resolved": 1
    }

@app.get("/version")
def version():
    return {"version": "v2"}