import pdb
from db.run_sql import run_sql

from models.albums import Album


def save(album):
    sql = " INSERT INTO albums (name, release_year, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.name, album.release_year, album.genre]
    results = run_sql(sql, values)
    id = results[0]["id"]
    # pdb.set_trace()
    album.id = id
    return album


def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        album = Album(row["name"], row["release_year"], row["genre"], row["id"])
        albums.append(album)

    # pdb.set_trace()
    return albums


def select(id):
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        album = Album(
            result["name"], result["release_year"], result["genre"], result["id"]
        )
    return album

def delete_all():
    sql= "DELETE FROM albums"
    run_sql(sql)