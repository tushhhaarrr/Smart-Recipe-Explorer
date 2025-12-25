from sqlalchemy import Column, Integer, String, Boolean, DateTime, UniqueConstraint, text, func
from app.database.connection import Base
from sqlalchemy.dialects.postgresql import ARRAY


# Database Model for Recipes
class Recipe(Base):
    __tablename__ = "recipes"  

    id = Column(Integer, primary_key=True, index=True)
    
    # informationcolumns
    name = Column(String(100), nullable=False)
    cuisine = Column(String(50), nullable=False)
    isVegetarian = Column(Boolean, default=True)  
    prepTimeMinutes = Column(Integer, nullable=False)
    ingredients = Column(ARRAY(String), nullable=False)
    tags = Column(ARRAY(String), nullable=False)
    difficulty = Column(String, nullable=False)
    instructions = Column(String, nullable=False)
    description = Column(String, nullable=False, server_default="No description provided")

    # it assures that there is no redundancy in recipes
    __table_args__ = (
        UniqueConstraint("name", "cuisine", name="uq_recipe_name_cuisine"),
    )



# Database for ai suggestion
class AISuggestion(Base):
    __tablename__ = "ai_suggestions"

    id = Column(
        String,
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    #user ggiven ingredients
    ingredients = Column(ARRAY(String), nullable=False)
    #ai answers
    suggestion_text = Column(String, nullable=False)
    
    # this tells time
    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )