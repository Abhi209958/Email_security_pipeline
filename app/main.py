from fastapi import FastAPI, HTTPException
from app.routers import ingest
from app.services import db
from app.utils.logger import logger

app = FastAPI()

app.include_router(ingest.router)



@app.on_event("startup")
async def startup_event():
    logger.info("Starting up the application")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down the application")