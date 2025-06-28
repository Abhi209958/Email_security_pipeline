import asyncio
import os
from temporalio.worker import Worker
from temporalio.client import Client
from workflows import EmailProcessingWorkflow
from temporal.activities import process_signal_activity_activity

async def main():
    temporal_host = os.getenv("TEMPORAL_HOST", "temporal")
    temporal_port = os.getenv("TEMPORAL_PORT", "7233")
    client = await Client.connect(f"{temporal_host}:{temporal_port}", namespace="default")
    worker = Worker(
        client,
        task_queue="email-task-queue",
        workflows=[EmailProcessingWorkflow],
        activities=[process_signal_activity_activity],
    )
    print("Worker started.")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
