from psycopg2 import sql
from DB.connect import connect, close


def select_units(json_person, col):
    new_str = ''
    #print(col)
    #print(json_person)
    #print()
    if json_person != []:

        if col == 'films':
            column = 'title'
        else:
            column = 'name'
        if col == 'homeworld':
            col = 'planets'
        count = ''
        if type(json_person) != type([]):
            #print(json_person)
            count = f'id={json_person.split("/")[-2]}'
        if len(json_person) > 1 and type(json_person) == type([]):
            for item in json_person:
                count += f"""id={item.split("/")[-2]} OR """
            count = count[:len(count)-4]
        elif len(json_person) == 1 and type(json_person) == type([]):
            count += f"""id={json_person[0].split("/")[-2]}"""
        query = sql.SQL(f'''SELECT {column} FROM swapi.{col} WHERE {count}''')
        #print(query)
        conn, cursor = connect()
        cursor.execute(query)
        res = cursor.fetchall()
        #print(res)
        for peace in res:
            if new_str == '':
                new_str += peace[0]
            else:
                new_str += f', {peace[0]}'
    return new_str
