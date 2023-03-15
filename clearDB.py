from selectDB import display_DB


def clear_DB(con, cursor):
    cursor.execute("DELETE FROM film")
    con.commit()
    display_DB(cursor)
    print("Database cleared")
