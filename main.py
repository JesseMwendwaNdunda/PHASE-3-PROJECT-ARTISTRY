from db import get_session
from models import Artwork
import click

# Create a session instance
session = get_session()

# Function to add a new artwork
def add_artwork():
    title = click.prompt("Enter artwork title")
    artist = click.prompt("Enter artist")
    year = click.prompt("Enter year", type=int)

    artwork = Artwork(title=title, artist=artist, year=year)
    session.add(artwork)
    session.commit()
    click.secho("Artwork added successfully!", fg="green")

# Function to list all artworks
def list_artworks():
    artworks = session.query(Artwork).all()
    if artworks:
        for art in artworks:
            click.secho(f"{art.id}. {art.title} by {art.artist} ({art.year})", fg="blue")
    else:
        click.secho("No artworks found.", fg="red")

# Function to update an artwork
def update_artwork():
    art_id = click.prompt("Enter artwork ID to update", type=int)
    artwork = session.query(Artwork).get(art_id)
    if artwork:
        new_title = click.prompt("Enter new title")
        artwork.title = new_title
        session.commit()
        click.secho("Updated successfully!", fg="green")
    else:
        click.secho("Artwork not found", fg="red")

# Function to delete an artwork
def delete_artwork():
    art_id = click.prompt("Enter artwork ID to delete", type=int)
    artwork = session.query(Artwork).get(art_id)
    if artwork:
        session.delete(artwork)
        session.commit()
        click.secho("Deleted successfully!", fg="green")
    else:
        click.secho("Artwork not found", fg="red")

# Main menu
def menu():
    while True:
        click.secho("\n==== Art Gallery Manager ====", fg="yellow")
        click.secho("1. Add Artwork", fg="blue")
        click.secho("2. List Artworks", fg="blue")
        click.secho("3. Update Artwork", fg="blue")
        click.secho("4. Delete Artwork", fg="blue")
        click.secho("5. Exit", fg="blue")

        choice = click.prompt("Enter choice", type=int)

        if choice == 1:
            add_artwork()
        elif choice == 2:
            list_artworks()
        elif choice == 3:
            update_artwork()
        elif choice == 4:
            delete_artwork()
        elif choice == 5:
            click.secho("Goodbye!", fg="red")
            break
        else:
            click.secho("Invalid choice, try again.", fg="red")

if __name__ == "__main__":
    menu()
