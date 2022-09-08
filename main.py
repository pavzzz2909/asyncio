from pprint import pprint

from psycopg2 import sql
import re


from support.imports import *

from DB.create import create_swapi_db, delete_swapi_db
from DB.connect import connect, close
from DB.insert import insert_film, insert_planet, insert_species, insert_starships, insert_vehicles, insert_person
from get_data.parse import retrieve_source



async def get_all_max_counts(type_, session):
    """ Получеам максимальные данные по каждому типу:
    ['planets', 'films', 'species', 'starships', 'vehicles', 'people'] """

    maximum = 0
    async with session.get(f'https://swapi.dev/api/{type_}/?page=1') as response:
        json_data = await response.json()
        return json_data['count']



async def main():
    # delete_swapi_db()
    create_swapi_db()
    tables = ['planets',
              'films',
              'species',
              'starships',
              'vehicles',
              'people']
    dict_maxim = {}
    dict_now = {'planets' : 0, 'films' : 0, 'species' : 0, 'starships' : 0, 'vehicles' : 0, 'people' : 0}
    async with aiohttp.ClientSession() as session:
        for _type in tables:
            maximum_of_type = await get_all_max_counts(_type, session)
            print(f'Обнаружено {_type}: {maximum_of_type}')
            dict_maxim[_type] = maximum_of_type


        for _type in tables:
            id = 1
            while dict_maxim[_type] > dict_now[_type]:
                if(_type == 'films'):
                    json_person = await retrieve_source(f'https://swapi.dev/api/{_type}/{id}/', session)
                    dict_now[_type] = await insert_film(json_person, id, dict_maxim[_type], dict_now[_type])
                if(_type == 'planets'):
                    json_person = await retrieve_source(f'https://swapi.dev/api/{_type}/{id}/', session)
                    dict_now[_type] = await insert_planet(json_person, id, dict_maxim[_type], dict_now[_type])
                if(_type == 'species'):
                    json_person = await retrieve_source(f'https://swapi.dev/api/{_type}/{id}/', session)
                    dict_now[_type] = await insert_species(json_person, id, dict_maxim[_type], dict_now[_type])
                if(_type == 'vehicles'):
                    json_person = await retrieve_source(f'https://swapi.dev/api/{_type}/{id}/', session)
                    dict_now[_type] = await insert_vehicles(json_person, id, dict_maxim[_type], dict_now[_type])
                if(_type=='starships'):
                    json_person = await retrieve_source(f'https://swapi.dev/api/{_type}/{id}/', session)
                    dict_now[_type] = await insert_starships(json_person, id, dict_maxim[_type], dict_now[_type])
                if(_type == 'people'):
                    json_person = await retrieve_source(f'https://swapi.dev/api/{_type}/{id}/', session)
                    dict_now[_type] = await insert_person(json_person, id, dict_maxim[_type], dict_now[_type])
                id += 1
                #print(dict_now[_type])


async def tasks():
    await main()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(tasks())
