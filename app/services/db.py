from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from app.models import Base, Email, Signal
import time

DATABASE_URL = "mysql+pymysql://root:YourNewStrongPassword@db:3306/email_signal_processing"

engine = None
while True:
    try:
        engine = create_engine(DATABASE_URL)
        # Try connecting to the database
        conn = engine.connect()
        conn.close()
        print("✅ Database is ready.")
        break
    except OperationalError as e:
        print(f"⏳ Waiting for database to be ready: {e}")
        time.sleep(2)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_session = next(get_db())
