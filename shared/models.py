from sqlalchemy import Column, String, Float, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class FraudScore(Base):
	__tablename__= 'fraud_scores'
	
	claim_id=Column(String, primary_key=True)
	provider_id=Column(String)
	final_score=Column(Float)
	z_score=Column(Float)
	reconstruction_error=Column(Float)
	metadata_flags=Column(JSON) #Store Impossible day or other flags
