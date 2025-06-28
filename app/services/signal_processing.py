from app.services.db import Email, Signal, db_session
from app.utils.logger import logger
from temporalio import activity
import random

@activity.defn
async def process_signal_activity(email_id: int):
    email = db_session.query(Email).filter_by(id=email_id).first()
    if not email:
        logger.error(f"Email not found: {email_id}")
        return

    domain_reputation = random.choice(["good", "bad", "unknown"])
    url_entropy = random.uniform(0, 1)
    sender_spoof_check = random.choice([True, False])

    new_signal = Signal(
        email_id=email_id,
        domain_reputation=domain_reputation,
        url_entropy=url_entropy,
        sender_spoof_check=sender_spoof_check
    )
    db_session.add(new_signal)
    db_session.commit()
    logger.info(f"Signal processed for email: {email_id}")