# from clearDB import clear_DB
from selectDB import display_DB, first_element
from scrap import scrap
from prettytable import PrettyTable
import time


# clear_DB(con, cursor)
def rss_feed(con, cursor):
    films = scrap()
    print(films[0][0])
    firstElement = first_element(cursor)
    print(firstElement)
    if len(firstElement) == 0 or firstElement != films[0][0]:
        print("Nouveaux film(s) disponible(s)")
        if films is not None:
            for all in films:
                cursor.execute(
                    """
                        INSERT INTO film (
                            name, image, date, description, link
                        ) VALUES (
                            ?, ?, ?, ?, ?
                        );
                    """,
                    (
                        all[0],
                        all[1],
                        all[2],
                        all[3],
                        all[4]
                    )
                )
            con.commit()
            rows = display_DB(cursor)
            t = PrettyTable()
            t.field_names = [
                "ID",
                "Name",
                "Image",
                "Date",
                "Description",
                "Link"
            ]
            for row in rows[::-1]:
                t.add_row(
                    [
                        row[0],
                        row[1],
                        row[2][:10],
                        row[3],
                        row[4][:100],
                        row[5][:10]
                    ]
                )
            print(t)
        else:
            print("Nouvelle tentative dans 1h")
    else:
        print("Pas de nouveau film")
        print("Nouvelle tentative dans 1h")


while True:
    rss_feed()
    time.sleep(60 * 60)
