from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Category(BaseModel):
    """
    Model representing a game category.
    
    Categories are used to classify games into different types or genres.
    Each category can have multiple games associated with it.
    """
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one category has many games
    games = relationship("Game", back_populates="category")
    
    @validates('name')
    def validate_name(self, key, name):
        """Validate the category name meets minimum length requirements."""
        return self.validate_string_length('Category name', name, min_length=2)
        
    @validates('description')
    def validate_description(self, key, description):
        """Validate the category description meets minimum length requirements."""
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)
    
    def __repr__(self):
        """Return string representation of the Category instance."""
        return f'<Category {self.name}>'
        
    def to_dict(self):
        """
        Convert the Category instance to a dictionary.
        
        Returns:
            dict: Dictionary representation including id, name, description, and game count
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }