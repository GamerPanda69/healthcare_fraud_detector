from fastapi import FastAPI
from shared.schemas import Claimrequest
import redis, json

app=FastAPI()
r=redis.Redis(host='redis', port=6379)

@app.post("/ingest")
async def ingest(claim:Claimrequest):
	r.lpush("claims_queue", claim.model_dump_json())
	return{"status":"Queued","id":claim.claim_id}
