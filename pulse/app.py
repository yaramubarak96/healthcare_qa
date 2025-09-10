## Also for logging would prefer having prometheous for metrics as well as in line logging 
## but again for the sake of this takehome I will just write the main async function 

from fastapi import FastAPI
from pydantic import BaseModel
import uuid 
from agents import Runner
from pulse.web_agent import web_agent
import logging 
from time import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(title="Pulse Healthcare Agent API", version="0.1.0")

# Basic request and response models 
class PulseRequest(BaseModel):
    user_id: uuid.UUID
    user_name: str 
    query: str 

class PulseResponse(BaseModel):
    answer: str 

@app.get("/")
async def root():
    return {"message": "Pulse Healthcare Agent API is running"}

@app.post("/pulse/answer")
async def pulse(request: PulseRequest): 
    start_time = time()
    logger.info(f"Received request from user {request.user_name} (ID: {request.user_id})")
    logger.info(f"Query: {request.query}")
    result = await Runner.run(web_agent, request.query)
    logger.info(f"Generated response for user {request.user_name}")
    end_time = time()
    logger.info(f"Time taken: {end_time - start_time} seconds")
    logger.info(f"Result: {result}")
    logger.info(f"Steps: {[(x.agent.name, type(x)) for x in result.new_items]}")
    return PulseResponse(answer=result.final_output)
