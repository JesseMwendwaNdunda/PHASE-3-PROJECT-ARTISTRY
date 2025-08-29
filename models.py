from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, Date
from sqlalchemy.orm import relationship
from db import Base

# Association table for many-to-many relationship between Artwork and Exhibition
artwork_exhibition = Table(
    'artwork_exhibition',
    Base.metadata,
    Column('artwork_id', Integer, ForeignKey('artworks.id'), primary_key=True),
    Column('exhibition_id', Integer, ForeignKey('exhibitions.id'), primary_key=True)
)

class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birth_year = Column(Integer, nullable=True)
    country = Column(String, nullable=True)

    # One-to-many relationship: Artist → Artwork
    artworks = relationship("Artwork", back_populates="artist_obj")

    def __repr__(self):
        return f"<Artist(id={self.id}, name='{self.name}')>"

class Artwork(Base):
    __tablename__ = "artworks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'), nullable=False)  # foreign key to Artist
    year = Column(Integer, nullable=True)
    price = Column(Float, nullable=True)

    # Relationships
    artist_obj = relationship("Artist", back_populates="artworks")
    exhibitions = relationship(
        "Exhibition",
        secondary=artwork_exhibition,
        back_populates="artworks"
    )

    def __repr__(self):
        return f"<Artwork(id={self.id}, title='{self.title}', artist_id={self.artist_id})>"

class Exhibition(Base):
    __tablename__ = "exhibitions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=True)
    date = Column(Date, nullable=True)
    

    # Many-to-many relationship: Exhibition ↔ Artwork
    artworks = relationship(
        "Artwork",
        secondary=artwork_exhibition,
        back_populates="exhibitions"
    )

    def __repr__(self):
        return f"<Exhibition(id={self.id}, name='{self.name}')>"
