from feedgen.feed import FeedGenerator
from flask import Flask, Response
import sqlite3
from selectDB import display_DB


con = sqlite3.connect("films.db")
cursor = con.cursor()
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS film (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    image TEXT,
    date TEXT,
    description TEXT,
    link TEST
);
"""
)
app = Flask(__name__)

fg = FeedGenerator()
fg.language("fr")
fg.title("Unofficial OVTOK RSS feed")
fg.author({"name": "BeowolfK"})
fg.link(href="http://ovtok.com/lecl0i38j/home/ovtok", rel="self")
fg.logo("http://ovtok.com/favicon.png")
fg.icon("http://ovtok.com/favicon.png")
fg.subtitle(
    "This is an unofficial RSS feed of OVTOK\
streaming site created by BeowolfK"
    )
all_films = display_DB(cursor)
for film in all_films:
    fe = fg.add_entry()
    fe.id(film[-1])
    fe.title(film[1])
    fe.description(film[4])
    fe.link(href=film[-1])


@app.route('/feed.xml')
def get_feed():
    return Response(fg.rss_str(pretty=True),
                    mimetype='application/rss+xml')


if __name__ == '__main__':
    app.run(debug=True)
