from temporalio import activity
from app.services.signal_processing import process_signal_activity as signal_processing_core

@activity.defn(name="process_signal_activity")
async def process_signal_activity_activity(signal_id: int):
    await signal_processing_core(signal_id)
