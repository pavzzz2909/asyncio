from psycopg2 import sql

from support.imports import *


from get_data.parse import retrieve_source

from DB.connect import connect, close
from DB.select import select_units

async def insert_film(json_person, id, maximum, now):
    """ Добавление фильма + """
    if json_person == {"detail": "Not found"}:
        pass
    else:
        row = [json_person[col] for col in json_person if(col in ['title', 'url'])]
        row.append(id)
        conn, cursor = connect()
        query = sql.SQL('''INSERT INTO swapi.films (title, url, id) VALUES (%s, %s, %s)''')
        cursor.execute(query, row)
        close(conn, cursor)
        now += 1
    return now



async def insert_planet(json_person, id, maximum, now):
    """ Добавление планеты + """
    if json_person == {"detail": "Not found"}:
        pass
    else:
        row = [json_person[col] for col in json_person if(col in ['name', 'url'])]
        row.append(id)
        conn, cursor = connect()
        query = sql.SQL('''INSERT INTO swapi.planets (name, url, id) VALUES (%s, %s, %s)''')
        cursor.execute(query, row)
        close(conn, cursor)
        now += 1
    return now



async def insert_species(json_person, id, maximum, now):
    """ Добавление рассы + """
    if json_person == {"detail": "Not found"}:
        pass
    else:
        row = [json_person[col] for col in json_person if(col in ['name', 'url'])]
        row.append(id)
        conn, cursor = connect()
        query = sql.SQL('''INSERT INTO swapi.species (name, url, id) VALUES (%s, %s, %s)''')
        cursor.execute(query, row)
        close(conn, cursor)
        now += 1
    return now



async def insert_starships(json_person, id, maximum, now):
    """ Добавление корабля + """
    if json_person == {"detail": "Not found"}:
        pass
    else:
        row = [json_person[col] for col in json_person if(col in ['name', 'url'])]
        row.append(id)
        conn, cursor = connect()
        query = sql.SQL('''INSERT INTO swapi.starships (name, url, id)
         VALUES (%s, %s, %s)''')
        cursor.execute(query, row)
        close(conn, cursor)
        now += 1
    return now


async def insert_vehicles(json_person, id, maximum, now):
    """ Добавление транспортного средства + """

    if json_person == {"detail": "Not found"}:
        pass
    else:
        row = [json_person[col] for col in json_person if(col in ['name', 'url'])]
        row.append(id)
        conn, cursor = connect()
        query = sql.SQL('''INSERT INTO swapi.vehicles (name, url, id) VALUES (%s, %s, %s)''')
        cursor.execute(query, row)
        close(conn, cursor)
        now += 1
    return now

from pprint import pprint
async def insert_person(json_person, id, maximum, now):
    # [id, birth_year, eye_color, films, gender, hair_color, height, homeworld, mass, name, skin_color, species, starships, vehicles]
    if json_person == {"detail": "Not found"}:
        pass
    else:
        #print(json_person)
        row1 = [json_person[col] for col in json_person if(col in ['birth_year', 'eye_color', 'gender', 'hair_color', 'height', 'mass', 'name', 'skin_color'])]
        row2 = [select_units(json_person[col], col) for col in json_person if(col in ['films', 'homeworld', 'species', 'starships', 'vehicles'])]
        row = row1 + row2
        row.append(id)
        conn, cursor = connect()
        pprint(row)
        query = sql.SQL('''INSERT INTO swapi.people (name, height, mass, hair_color, skin_color, eye_color, birth_year, gender,
        homeworld, films, species, starships, vehicles, id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''')
        try:
            cursor.execute(query, row)
        except:
            pass

        close(conn, cursor)
        now += 1
    return now
