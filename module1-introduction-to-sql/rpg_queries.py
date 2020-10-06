import sqlite3

def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

GET_CHARACTERS = """
 SELECT * FROM charactercreator_character;
"""
# Total of individual characters
COUNT_CHARACTERS = """
SELECT COUNT(DISTINCT name) FROM charactercreator_character;
"""

# Count of each subclass
COUNT_THIEF = "SELECT count(*) FROM charactercreator_thief;"
COUNT_FIGHTER = "SELECT count(*) FROM charactercreator_fighter;"
COUNT_MAGE = "SELECT count(*) FROM charactercreator_mage;"
COUNT_CLERIC = "SELECT count(*) FROM charactercreator_CLERIC;"
COUNT_NECRO = "SELECT count(*) FROM charactercreator_necromancer;"

# Total items
TOTAL_ITEMS = "SELECT COUNT(*) FROM armory_item;"

# Total weapons
TOTAL_WEAPONS = "SELECT COUNT(*) FROM armory_weapon;"

# Total items excluding weapons
TOTAL_NOT_WEAPONS = """
    SELECT(SELECT COUNT(*) FROM armory_item) -
    (SELECT COUNT(*) FROM armory_weapon);
"""
# Items per character
WEAPONS_PER_CHARACTER = """
    SELECT COUNT(distinct character_id) as items
    FROM charactercreator_character_inventory
    INNER JOIN armory_weapon 
    ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
    LIMIT 20;
"""


if __name__ == "__main__":
    conn = connect_to_db()
    curs = conn.cursor()
    results = execute_query(curs, COUNT_CHARACTERS)
    print('Character Count: ', results[0][0])

    results = execute_query(curs, COUNT_THIEF)
    print('Thief count: ', results[0][0])
    results = execute_query(curs, COUNT_FIGHTER)
    print('Fighter count: ', results[0][0])
    results = execute_query(curs, COUNT_MAGE)
    print('Mage count: ', results[0][0])
    results = execute_query(curs, COUNT_CLERIC)
    print('Cleric count: ', results[0][0])
    results = execute_query(curs, COUNT_NECRO)
    print('Necromancer count: ', results[0][0])

    results = execute_query(curs, TOTAL_ITEMS)
    print('Total # of items: ', results[0][0])

    results = execute_query(curs, TOTAL_WEAPONS)
    print('Total # of weapons: ', results[0][0])

    results = execute_query(curs, TOTAL_NOT_WEAPONS)
    print('Total # of non-weapons: ', results[0][0])

    results = execute_query(curs, WEAPONS_PER_CHARACTER)
    print('Total items per character', results)