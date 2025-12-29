
from app.database.connection import get_engine, Base
from app.database import models

# Get the engine
engine = get_engine()

# Create all tables
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")


