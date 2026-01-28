from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (allow POST from any origin)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/metrics")
def get_metrics(payload: dict):
    return {
        "status": "endpoint working",
        "received": payload
    }
