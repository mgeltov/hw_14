import sqlite3
import json

def get_by_type_year_genre(type='Movie', year=2019, genre='Drama'):
    search_genre = str.lower(genre)
    search_type = str.lower(type)
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                select title, description
                from netflix
                where lower(listed_in) like '%{search_genre}%'
                and release_year = {year}
                and lower(type) = '{search_type}'
        """
        cursor.execute(query)
        search_list = []
        for row in cursor.fetchall():
            search_dict = dict()
            search_dict['title'] = row[0]
            search_dict['description'] = row[1]
            search_list.append(search_dict)

        return json.dumps(search_list)
