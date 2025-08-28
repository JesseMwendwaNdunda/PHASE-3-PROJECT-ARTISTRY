from db import get_session
from models import Artwork

# Function to add a new artwork to the database
def add_artwork(title, artist, year=None, price=None):
    session = get_session()
    artwork = Artwork(title=title, artist=artist, year=year, price=price)
    session.add(artwork)
    session.commit()
    print(f"Added: {artwork}")

# Function to list all artworks currently in the database
def list_artworks():
    session = get_session()
    artworks = session.query(Artwork).all()
    if not artworks:
        print("No artworks found.")
    for art in artworks:
        print(art)

# Function to update an artwork's details by its ID
def update_artwork(art_id, title=None, artist=None, year=None, price=None):
    session = get_session()
    artwork = session.query(Artwork).filter(Artwork.id == art_id).first()
    if not artwork:
        print("Artwork not found.")
        return
    # Update only the fields that are provided
    if title: artwork.title = title
    if artist: artwork.artist = artist
    if year: artwork.year = year
    if price: artwork.price = price
    session.commit()
    print(f"Updated: {artwork}")

# Function to delete an artwork record by its ID
def delete_artwork(art_id):
    session = get_session()
    artwork = session.query(Artwork).filter(Artwork.id == art_id).first()
    if not artwork:
        print("Artwork not found.")
        return
    session.delete(artwork)
    session.commit()
    print(f"Deleted artwork with id={art_id}")
