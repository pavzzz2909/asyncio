from DB.connect import connect, close



def create_swapi_db():
    conn, cur = connect()
    cur.execute("CREATE SCHEMA IF NOT EXISTS swapi;")

    cur.execute('''CREATE TABLE IF NOT EXISTS swapi.films   (
											id int primary key,
											title text,
											url text);''')

    cur.execute('''CREATE TABLE IF NOT exists swapi.planets	(
											id int primary key,
											name text,
											url text);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS swapi.species	(
											id int primary key,
											name text,
											url text);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS swapi.starships (
											id int primary key,
											name text,
											url text);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS swapi.vehicles(
									id int primary key,
									name text,
									url text);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS swapi.people (
                                  id int primary key,
                                  name text,
								  height text,
								  mass text,
								  hair_color text,
								  skin_color text,
								  eye_color text,
								  birth_year text,
								  gender text,
								  homeworld text,
                                  films text,
                                  species text,
                                  starships text,
                                  vehicles text,
								  url text,
								  created text,
								  edited text);''')
    close(conn, cur)



def delete_swapi_db():
	conn, cur = connect()
	try:
		cur.execute('''	drop table swapi.films;
					drop table swapi.people;
					drop table swapi.planets;
					drop table swapi.species;
					drop table swapi.starships ;
					drop table swapi.vehicles;''')
	except:
		pass
	close(conn, cur)
