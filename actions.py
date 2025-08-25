import sqlite3

# Add a part and location to the database
def add_item(part,location):
    '''
    This function takes part(the name or the part or the part number) and
    the location(the slot number or storage location ex: 1-A-23), then adds
    it to the database for use. this only takes one as a time!
    '''
    conn = sqlite3.connect('locations.db')
    c = conn.cursor()

    part_stripped = part.replace(" ", "")
    location_stripped = location.replace(" ", "")
    finished_part = part_stripped.upper()
    finished_location = location_stripped.upper()
    

    # adds the part and location to the database
    c.execute("INSERT INTO locations VALUES (?,?)",(finished_part,finished_location))

    conn.commit()
    conn.close()

# Looks up a part and provides its location
def look_up(part):
    '''
    This takes the part(number or name given to the product) and looks for it in the 
    database, if found it returns the locatin.
    '''
    stripped = part.replace(" ", "")
    finished = stripped.upper()
    # print(finished)

    conn = sqlite3.connect('locations.db')
    c = conn.cursor()

    c.execute("SELECT * FROM locations WHERE product_number = (?)",(finished,))
    items = c.fetchall()

    conn.close

    # Checkes if the part was found then tell you no part found if no part was found.
    if not items:
        print('Part Not Found')
        return []


    # for item in items:
    #     print(item[1])
    locations = [item[1] for item in items]
    print('Found locations: ', locations)

    return locations

# The show all shows ALL
def show_all():
    '''
    Selects all items from the database and displayes them
    '''
    conn = sqlite3.connect('locations.db')
    c = conn.cursor()

    # Selects all items from the database and displayes them
    c.execute("SELECT * FROM locations")
    items = c.fetchall()
    for item in items:
        print(item)

    conn.close()


# Change the locaton of a part that already exist
def change_location(part, location, new_location):
    '''
    Allows the user to change the location of a part. Prompts for the part,
    shows the current location, asks for the new location, and updates the database.
    '''
    conn = sqlite3.connect('locations.db')
    c = conn.cursor()

    cleaned_part = part.replace(" ", "").upper()
    cleaned_location = location.replace(" ", "").upper()
    cleaned_new_location = new_location.replace(" ", "").upper()

    # Look up the part
    c.execute("SELECT * FROM locations WHERE product_number = ? AND location = ?", (cleaned_part, cleaned_location))
    item = c.fetchone()

    # print(part)
    # print(location)
    # print(new_location)

    if not item:
        print("Part not found.")
        conn.close()
        return 2


    # Update the location
    c.execute("UPDATE locations SET location = ? WHERE product_number = ? AND location = ?", (cleaned_new_location, cleaned_part, cleaned_location))
    conn.commit()

    # print(f"Updated '{part}' to new location: {new_location}")
    conn.close()
    return 1

# Remove part from Database 
def delete(part,location):
    conn = sqlite3.connect('locations.db')
    c = conn.cursor()
    # Select the item chosen 

    part_stripped = part.replace(" ", "")
    location_stripped = location.replace(" ", "")
    finished_part = part_stripped.upper()
    finished_location = location_stripped.upper()

    # print(part)
    # print(location)
    c.execute("SELECT * FROM locations WHERE product_number = ? AND location = ?",(finished_part, finished_location))
    item = c.fetchone()
    print(item)
    # Identifies that the item chosen exists before deleting
    if item:
        c.execute("DELETE FROM locations WHERE product_number = ? AND location = ?",(finished_part, finished_location))
        conn.commit()
        conn.close()
        return 1
    else:
        conn.close()
        return 2


def deleteall():
    conn = sqlite3.connect('locations.db')
    c = conn.cursor()
    # CREATING A TABLE:
    c.execute('DELETE FROM locations')
    conn.commit()
    conn.close()

def createtable():
    conn = sqlite3.connect('locations.db')
    c = conn.cursor()
    # CREATING A TABLE:
    c.execute('''CREATE TABLE locations (
        product_number text,
        location text
        )''')
    conn.commit()
    conn.close()


def mass_insert(data):
    conn = sqlite3.connect('locations.db')
    c = conn.cursor()
    c.executemany('INSERT INTO locations (product_number, location) VALUES (?, ?)', data)
    conn.commit()
    conn.close()