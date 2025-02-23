from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Vulnerability(Base):
    __tablename__ = "vulnerabilities"

    id = Column(Integer, primary_key=True, index=True)
    issue_name = Column(String, nullable=False)
    tech_stack = Column(String, nullable=True)
    component = Column(String, nullable=True)
    severity = Column(String, nullable=False)
    sla = Column(String, nullable=True)

    best_fix = Column(String, nullable=True)
    business_friendly_fix = Column(String, nullable=True)
    temporary_mitigation = Column(String, nullable=True)
