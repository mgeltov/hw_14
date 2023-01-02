import sqlite3

def raw_actors(name1='Jack Black', name2='Dustin Hoffman'):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                select netflix.cast
                from netflix
                where netflix.cast like '%{name1}%'
                and netflix.cast like '%{name2}%'
        """
        cursor.execute(query)
        raw_actors_list = []
        for row in cursor.fetchall():
            raw_actors_list.append(row)
        return raw_actors_list

print(raw_actors())