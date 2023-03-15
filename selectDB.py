def display_DB(cursor):
    cursor.execute("SELECT * FROM film ORDER BY id DESC LIMIT 15")
    rows = cursor.fetchall()
    return rows


def first_element(cursor):
    cursor.execute("SELECT name FROM film ORDER BY id DESC LIMIT 15")
    bdd = cursor.fetchall()
    if len(bdd) != 0:
        return bdd[-1][0]
    else:
        return []
