from sqlalchemy import Boolean, Column, Float, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    sender = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    links = Column(Text)
    signals = relationship("Signal", back_populates="email")

class Signal(Base):
    __tablename__ = 'signals'
    id = Column(Integer, primary_key=True)
    email_id = Column(Integer, ForeignKey('emails.id'), nullable=False)
    domain_reputation = Column(String(255))
    url_entropy = Column(Float)
    sender_spoof_check = Column(Boolean)
    email = relationship("Email", back_populates="signals")