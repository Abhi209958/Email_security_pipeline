from datetime import timedelta
from temporalio import workflow

@workflow.defn
class EmailProcessingWorkflow:
    @workflow.run
    async def run(self, email_id: int):
        await workflow.execute_activity(
            "process_signal_activity",  
            email_id,
            start_to_close_timeout=timedelta(seconds=30),
        )
