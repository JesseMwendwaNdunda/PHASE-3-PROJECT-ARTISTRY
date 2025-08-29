from db import get_session
from models import Artwork, Artist, Exhibition
import click
from datetime import datetime

session = get_session()

# -------------------
# Artist Functions
# -------------------
def add_artist():
    name = click.prompt("Enter artist name")
    birth_year = click.prompt("Enter birth year", type=int)
    country = click.prompt("Enter country")
    artist = Artist(name=name, birth_year=birth_year, country=country)
    session.add(artist)
    session.commit()
    click.secho("Artist added successfully!", fg="green")

def list_artists():
    artists = session.query(Artist).all()
    if artists:
        for a in artists:
            click.secho(f"{a.id}. {a.name} ({a.birth_year}) - {a.country}", fg="blue")
    else:
        click.secho("No artists found.", fg="red")

# -------------------
# Exhibition Functions
# -------------------
def add_exhibition():
    name = click.prompt("Enter exhibition name")
    location = click.prompt("Enter location")
    date_str = click.prompt("Enter date (YYYY-MM-DD)")

    # Convert string to Python date object
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        click.secho("Invalid date format. Please use YYYY-MM-DD.", fg="red")
        return

    exhibition = Exhibition(name=name, location=location, date=date_obj)
    session.add(exhibition)
    session.commit()
    click.secho("Exhibition added successfully!", fg="green")

def list_exhibitions():
    exhibitions = session.query(Exhibition).all()
    if exhibitions:
        for e in exhibitions:
            click.secho(f"{e.id}. {e.name} - {e.location} - {e.date}", fg="blue")
    else:
        click.secho("No exhibitions found.", fg="red")

# -------------------
# Artwork Functions
# -------------------
def add_artwork():
    title = click.prompt("Enter artwork title")
    list_artists()
    artist_id = click.prompt("Enter artist ID for this artwork", type=int)
    artist = session.query(Artist).get(artist_id)
    if not artist:
        click.secho("Invalid artist ID.", fg="red")
        return

    year = click.prompt("Enter year", type=int)
    price = click.prompt("Enter price", type=float)
    artwork = Artwork(title=title, year=year, price=price, artist_obj=artist)
    session.add(artwork)
    session.commit()
    click.secho("Artwork added successfully!", fg="green")

def list_artworks():
    artworks = session.query(Artwork).all()
    if artworks:
        for art in artworks:
            exhibitions = ", ".join([ex.name for ex in art.exhibitions])
            click.secho(
                f"{art.id}. {art.title} by {art.artist_obj.name} ({art.year}) - "
                f"Price: {art.price if art.price else 'N/A'} - "
                f"Exhibitions: {exhibitions if exhibitions else 'None'}",
                fg="blue"
            )
    else:
        click.secho("No artworks found.", fg="red")

# -------------------
# Delete Functions
# -------------------
def delete_item():
    click.secho("\nDelete Menu:", fg="yellow")
    click.secho("1. Delete Artist", fg="blue")
    click.secho("2. Delete Exhibition", fg="blue")
    click.secho("3. Delete Artwork", fg="blue")
    choice = click.prompt("Enter choice", type=int)

    if choice == 1:
        list_artists()
        artist_id = click.prompt("Enter Artist ID to delete", type=int)
        artist = session.query(Artist).get(artist_id)
        if artist:
            session.delete(artist)
            session.commit()
            click.secho("Artist deleted successfully!", fg="green")
        else:
            click.secho("Artist not found.", fg="red")

    elif choice == 2:
        list_exhibitions()
        exhibition_id = click.prompt("Enter Exhibition ID to delete", type=int)
        exhibition = session.query(Exhibition).get(exhibition_id)
        if exhibition:
            session.delete(exhibition)
            session.commit()
            click.secho("Exhibition deleted successfully!", fg="green")
        else:
            click.secho("Exhibition not found.", fg="red")

    elif choice == 3:
        list_artworks()
        artwork_id = click.prompt("Enter Artwork ID to delete", type=int)
        artwork = session.query(Artwork).get(artwork_id)
        if artwork:
            session.delete(artwork)
            session.commit()
            click.secho("Artwork deleted successfully!", fg="green")
        else:
            click.secho("Artwork not found.", fg="red")
    else:
        click.secho("Invalid choice.", fg="red")

# -------------------
# Main Menu
# -------------------
def menu():
    while True:
        click.secho("\n==== Art Gallery Manager ====", fg="yellow")
        click.secho("1. Add Artist", fg="blue")
        click.secho("2. List Artists", fg="blue")
        click.secho("3. Add Exhibition", fg="blue")
        click.secho("4. List Exhibitions", fg="blue")
        click.secho("5. Add Artwork", fg="blue")
        click.secho("6. List Artworks", fg="blue")
        click.secho("7. Delete Item", fg="blue")
        click.secho("8. Exit", fg="blue")

        choice = click.prompt("Enter choice", type=int)
        if choice == 1:
            add_artist()
        elif choice == 2:
            list_artists()
        elif choice == 3:
            add_exhibition()
        elif choice == 4:
            list_exhibitions()
        elif choice == 5:
            add_artwork()
        elif choice == 6:
            list_artworks()
        elif choice == 7:
            delete_item()
        elif choice == 8:
            click.secho("Goodbye!", fg="red")
            break
        else:
            click.secho("Invalid choice, try again.", fg="red")

if __name__ == "__main__":
    menu()
