from fastapi import FastApi
from shared.schemas import ClaimRequest
import redis json

app=FastAPI()
r=redis.Redis(host='redis', port=6379)

@app.post("/ingest")
async def ingest(claim:ClaimRequest):
	r.lpush("claims_queue", claim.model_dump_json())
	return{"status":"Queued","id":claim.claim_id}
