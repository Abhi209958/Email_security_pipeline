from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.db import Email, db_session
from app.utils.logger import logger
from datetime import datetime
from temporalio.client import Client
from temporal.workflows import EmailProcessingWorkflow
import os

router = APIRouter()

class EmailIn(BaseModel):
    sender: str
    subject: str
    timestamp: str
    links: str

@router.post("/ingest")
async def ingest_email(email: EmailIn):
    try:
        timestamp = datetime.fromisoformat(email.timestamp.replace("Z", "+00:00")).strftime('%Y-%m-%d %H:%M:%S')
        
        new_email = Email(sender=email.sender, subject=email.subject, timestamp=timestamp, links=email.links)
        db_session.add(new_email)
        db_session.commit()
        logger.info(f"Email ingested: {email.sender} - {email.subject}")

        # Retrieve Temporal host and port from environment (use docker network alias)
        temporal_host = os.getenv("TEMPORAL_HOST", "temporal")
        temporal_port = os.getenv("TEMPORAL_PORT", "7233")
        temporal_address = f"{temporal_host}:{temporal_port}"

        # Start Temporal workflow
        client = await Client.connect(temporal_address)
        await client.start_workflow(
            EmailProcessingWorkflow.run,
            new_email.id,
            id=f"email-processing-{new_email.id}",
            task_queue="email-task-queue"
        )

        return {"message": "Email ingested and processing workflow started"}
    except Exception as e:
        logger.error(f"Error ingesting email: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")