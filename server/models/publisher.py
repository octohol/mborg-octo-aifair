from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Publisher(BaseModel):
    """
    Model representing a game publisher.
    
    Publishers are organizations that publish games on the crowdfunding platform.
    Each publisher can have multiple games associated with them.
    """
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one publisher has many games
    games = relationship("Game", back_populates="publisher")

    @validates('name')
    def validate_name(self, key, name):
        """Validate the publisher name meets minimum length requirements."""
        return self.validate_string_length('Publisher name', name, min_length=2)

    @validates('description')
    def validate_description(self, key, description):
        """Validate the publisher description meets minimum length requirements."""
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)

    def __repr__(self):
        """Return string representation of the Publisher instance."""
        return f'<Publisher {self.name}>'

    def to_dict(self):
        """
        Convert the Publisher instance to a dictionary.
        
        Returns:
            dict: Dictionary representation including id, name, description, and game count
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }