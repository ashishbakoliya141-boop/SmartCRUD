from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import URL
from .config import settings

DATABASE_URL = URL.create(
    drivername="postgresql",
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME
)
print("----------------------------------------------------------------------------------->",DATABASE_URL)

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker( # it creates temprary conversation session
    autocommit=False,
    autoflush=False, # sqlalchemy automatcially does not push changes from the database
    bind=engine
)

Base = declarative_base() # map the all models inside database tables

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()