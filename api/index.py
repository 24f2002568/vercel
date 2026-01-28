from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (allow POST from any origin)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/metrics")
def get_metrics(payload: dict):
    return {
        "status": "endpoint working",
        "received": payload
    }

@app.get("/")
def home():
    return {"message": "API is live. Use POST /metrics"}
