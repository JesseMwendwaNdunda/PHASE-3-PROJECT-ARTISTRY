from sqlalchemy import Column, Integer, String, Float
from db import Base

class Artwork(Base):
    __tablename__ = "artworks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    year = Column(Integer, nullable=True)
    price = Column(Float, nullable=True)

    def __repr__(self):
        return f"<Artwork(id={self.id}, title='{self.title}', artist='{self.artist}')>"
