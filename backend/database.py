from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Change password if needed
db_url = "postgresql://postgres:root@localhost:5432/hospital_db"

engine = create_engine(db_url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)