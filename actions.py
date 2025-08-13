# actions.py
import os
import sqlite3
from pathlib import Path
from typing import Iterable, List, Tuple, Optional

# --- Configuration -----------------------------------------------------------

# On Render, set this in the service's Environment tab to /var/data/locations.db
DB_PATH = os.getenv("SQLITE_PATH", "/var/data/locations.db")

# Make sure the parent directory exists (Render creates /var/data when the disk is attached,
# but this also lets you safely point SQLITE_PATH to a nested directory if you ever want to).
Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)


# --- Connection / Initialization --------------------------------------------

def get_conn() -> sqlite3.Connection:
    """
    Open a fresh connection to the SQLite DB.
    A per-call connection plays nicely with Gunicorn workers/threads.
    """
    conn = sqlite3.connect(DB_PATH)
    # Optional nice-to-haves for durability & read concurrency:
    # WAL allows readers while a writer is active.
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn


def init_db() -> None:
    """
    Idempotently create the 'locations' table if it doesn't exist yet.
    """
    with get_conn() as conn:
        c = conn.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS locations (
                product_number TEXT,
                location       TEXT
            )
            """
        )
        conn.commit()


# Initialize schema at import time so the table exists on first boot.
init_db()


# --- Helpers ----------------------------------------------------------------

def _normalize_part(part: str) -> str:
    # remove spaces, uppercase for consistency
    return part.replace(" ", "").upper()


def _normalize_location(location: str) -> str:
    return location.replace(" ", "").upper()


# --- Public API used by your Flask routes -----------------------------------

def add_item(part: str, location: str) -> int:
    """
    Insert a (product_number, location) pair.
    Returns:
      1 = inserted
      2 = already existed (no-op)
    """
    finished_part = _normalize_part(part)
    finished_location = _normalize_location(location)

    with get_conn() as conn:
        c = conn.cursor()
        # avoid exact duplicate pairs
        c.execute(
            "SELECT 1 FROM locations WHERE product_number = ? AND location = ?",
            (finished_part, finished_location),
        )
        if c.fetchone():
            return 2  # already exists

        c.execute(
            "INSERT INTO locations (product_number, location) VALUES (?, ?)",
            (finished_part, finished_location),
        )
        conn.commit()
        return 1


def look_up(part: str) -> List[str]:
    """
    Return all locations for the given product_number (normalized).
    """
    finished_part = _normalize_part(part)
    with get_conn() as conn:
        c = conn.cursor()
        c.execute(
            "SELECT location FROM locations WHERE product_number = ? ORDER BY location ASC",
            (finished_part,),
        )
        rows = c.fetchall()
        return [r[0] for r in rows]


def delete(part: str, location: str) -> int:
    """
    Delete a specific (product_number, location) mapping.
    Returns:
      1 = deleted
      2 = not found (no-op)
    """
    finished_part = _normalize_part(part)
    finished_location = _normalize_location(location)

    with get_conn() as conn:
        c = conn.cursor()
        c.execute(
            "SELECT 1 FROM locations WHERE product_number = ? AND location = ?",
            (finished_part, finished_location),
        )
        if not c.fetchone():
            return 2

        c.execute(
            "DELETE FROM locations WHERE product_number = ? AND location = ?",
            (finished_part, finished_location),
        )
        conn.commit()
        return 1


def change_location(part: str, old_location: str, new_location: str) -> int:
    """
    Update a product's specific location value (old -> new).
    Returns:
      1 = updated
      2 = original pair not found (no-op)
      3 = new pair already exists (no-op, to avoid duplicates)
    """
    finished_part = _normalize_part(part)
    finished_old = _normalize_location(old_location)
    finished_new = _normalize_location(new_location)

    if finished_old == finished_new:
        return 3  # nothing to change

    with get_conn() as conn:
        c = conn.cursor()
        # ensure the old pair exists
        c.execute(
            "SELECT 1 FROM locations WHERE product_number = ? AND location = ?",
            (finished_part, finished_old),
        )
        if not c.fetchone():
            return 2

        # ensure the new pair doesn't already exist
        c.execute(
            "SELECT 1 FROM locations WHERE product_number = ? AND location = ?",
            (finished_part, finished_new),
        )
        if c.fetchone():
            return 3

        c.execute(
            "UPDATE locations SET location = ? WHERE product_number = ? AND location = ?",
            (finished_new, finished_part, finished_old),
        )
        conn.commit()
        return 1


def deleteall(confirm: Optional[bool] = False) -> int:
    """
    Dangerous: wipe the table clean.
    If confirm is True, it deletes all rows and recreates the table (fresh).
    Returns:
      1 = wiped/recreated
      2 = skipped (confirm was False)
    """
    if not confirm:
        return 2

    with get_conn() as conn:
        c = conn.cursor()
        # Drop and recreate gives you a truly clean slate
        c.execute("DROP TABLE IF EXISTS locations")
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS locations (
                product_number TEXT,
                location       TEXT
            )
            """
        )
        conn.commit()
        return 1


def mass_insert(data: Iterable[Tuple[str, str]]) -> int:
    """
    Bulk insert of (product_number, location) tuples.
    - Normalizes each pair (strip spaces, uppercase).
    - Skips exact duplicates already present.
    Returns count of rows newly inserted.
    """
    normalized = [(_normalize_part(p), _normalize_location(l)) for p, l in data]
    inserted = 0

    with get_conn() as conn:
        c = conn.cursor()
        # To avoid duplicates efficiently, we can insert where not exists
        for p, l in normalized:
            c.execute(
                "SELECT 1 FROM locations WHERE product_number = ? AND location = ?",
                (p, l),
            )
            if c.fetchone():
                continue
            c.execute(
                "INSERT INTO locations (product_number, location) VALUES (?, ?)",
                (p, l),
            )
            inserted += 1
        conn.commit()

    return inserted






















# import sqlite3

# # Add a part and location to the database
# def add_item(part,location):
#     '''
#     This function takes part(the name or the part or the part number) and
#     the location(the slot number or storage location ex: 1-A-23), then adds
#     it to the database for use. this only takes one as a time!
#     '''
#     conn = sqlite3.connect('locations.db')
#     c = conn.cursor()

#     part_stripped = part.replace(" ", "")
#     location_stripped = location.replace(" ", "")
#     finished_part = part_stripped.upper()
#     finished_location = location_stripped.upper()
    

#     # adds the part and location to the database
#     c.execute("INSERT INTO locations VALUES (?,?)",(finished_part,finished_location))

#     conn.commit()
#     conn.close()

# # Looks up a part and provides its location
# def look_up(part):
#     '''
#     This takes the part(number or name given to the product) and looks for it in the 
#     database, if found it returns the locatin.
#     '''
#     stripped = part.replace(" ", "")
#     finished = stripped.upper()
#     # print(finished)

#     conn = sqlite3.connect('locations.db')
#     c = conn.cursor()

#     c.execute("SELECT * FROM locations WHERE product_number = (?)",(finished,))
#     items = c.fetchall()

#     conn.close

#     # Checkes if the part was found then tell you no part found if no part was found.
#     if not items:
#         print('Part Not Found')
#         return []


#     # for item in items:
#     #     print(item[1])
#     locations = [item[1] for item in items]
#     print('Found locations: ', locations)

#     return locations

# # The show all shows ALL
# def show_all():
#     '''
#     Selects all items from the database and displayes them
#     '''
#     conn = sqlite3.connect('locations.db')
#     c = conn.cursor()

#     # Selects all items from the database and displayes them
#     c.execute("SELECT * FROM locations")
#     items = c.fetchall()
#     for item in items:
#         print(item)

#     conn.close()


# # Change the locaton of a part that already exist
# def change_location(part, location, new_location):
#     '''
#     Allows the user to change the location of a part. Prompts for the part,
#     shows the current location, asks for the new location, and updates the database.
#     '''
#     conn = sqlite3.connect('locations.db')
#     c = conn.cursor()

#     cleaned_part = part.replace(" ", "").upper()
#     cleaned_location = location.replace(" ", "").upper()
#     cleaned_new_location = new_location.replace(" ", "").upper()

#     # Look up the part
#     c.execute("SELECT * FROM locations WHERE product_number = ? AND location = ?", (cleaned_part, cleaned_location))
#     item = c.fetchone()

#     # print(part)
#     # print(location)
#     # print(new_location)

#     if not item:
#         print("Part not found.")
#         conn.close()
#         return 2


#     # Update the location
#     c.execute("UPDATE locations SET location = ? WHERE product_number = ? AND location = ?", (cleaned_new_location, cleaned_part, cleaned_location))
#     conn.commit()

#     # print(f"Updated '{part}' to new location: {new_location}")
#     conn.close()
#     return 1

# # Remove part from Database 
# def delete(part,location):
#     conn = sqlite3.connect('locations.db')
#     c = conn.cursor()
#     # Select the item chosen 

#     part_stripped = part.replace(" ", "")
#     location_stripped = location.replace(" ", "")
#     finished_part = part_stripped.upper()
#     finished_location = location_stripped.upper()

#     # print(part)
#     # print(location)
#     c.execute("SELECT * FROM locations WHERE product_number = ? AND location = ?",(finished_part, finished_location))
#     item = c.fetchone()
#     print(item)
#     # Identifies that the item chosen exists before deleting
#     if item:
#         c.execute("DELETE FROM locations WHERE product_number = ? AND location = ?",(finished_part, finished_location))
#         conn.commit()
#         conn.close()
#         return 1
#     else:
#         conn.close()
#         return 2


# def deleteall():
#     conn = sqlite3.connect('locations.db')
#     c = conn.cursor()
#     # CREATING A TABLE:
#     c.execute('DELETE FROM locations')
#     conn.commit()
#     conn.close()

# def createtable():
#     conn = sqlite3.connect('locations.db')
#     c = conn.cursor()
#     # CREATING A TABLE:
#     c.execute('''CREATE TABLE locations (
#         product_number text,
#         location text
#         )''')
#     conn.commit()
#     conn.close()


# def mass_insert(data):
#     conn = sqlite3.connect('locations.db')
#     c = conn.cursor()
#     c.executemany('INSERT INTO locations (product_number, location) VALUES (?, ?)', data)
#     conn.commit()
#     conn.close()