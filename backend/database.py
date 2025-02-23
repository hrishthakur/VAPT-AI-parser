from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from config import DATABASE_URL
import logging

logger = logging.getLogger(__name__)

# Create engine and SessionLocal outside of init_db
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """Initialize the database tables."""
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        raise


# Optional: Create a database session context manager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
