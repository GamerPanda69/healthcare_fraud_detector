#schemas.py
from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date
from typing import Optional, List

class ClaimRequest(BaseModel):
    provider_id:str
    claim_id:str
    amount:float
    icd_code:str
    start_date:date
    end_date:date
