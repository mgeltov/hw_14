import sqlite3

def search_title(search_text):
    search_text = str.lower(search_text)
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                select title, country, release_year, listed_in, description
                from netflix
                where lower(title) like '%{search_text}%'
                order by release_year desc
                limit 1
        """
        cursor.execute(query)
        search_dict = dict()
        for row in cursor.fetchall():
            search_dict['title'] = row[0]
            search_dict['country'] = row[1]
            search_dict['release_year'] = row[2]
            search_dict['genre'] = row[3]
            search_dict['description'] = row[4]

        return search_dict


def get_by_releases_period(year1, year2):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                select title, release_year
                from netflix
                where release_year between {year1} and {year2}
                limit 100
        """
        cursor.execute(query)
        result_list = []
        for row in cursor.fetchall():
            result_dict = dict()
            result_dict['title'] = row[0]
            result_dict['release_year'] = row[1]
            result_list.append(result_dict)
        return result_list


def get_kids_films():
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                select title, rating, description
                from netflix
                where rating in ('G')
                limit 100
        """
        cursor.execute(query)
        result_list = []
        for row in cursor.fetchall():
            result_dict = dict()
            result_dict['title'] = row[0]
            result_dict['rating'] = row[1]
            result_dict['description'] = row[2]
            result_list.append(result_dict)
        return result_list


def get_family_films():
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                select title, rating, description
                from netflix
                where rating in ('G', 'PG', 'PG-13')
                limit 100
        """
        cursor.execute(query)
        result_list = []
        for row in cursor.fetchall():
            result_dict = dict()
            result_dict['title'] = row[0]
            result_dict['rating'] = row[1]
            result_dict['description'] = row[2]
            result_list.append(result_dict)
        return result_list


def get_adult_films():
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                select title, rating, description
                from netflix
                where rating in ('R', 'NC-17')
                limit 100
        """
        cursor.execute(query)
        result_list = []
        for row in cursor.fetchall():
            result_dict = dict()
            result_dict['title'] = row[0]
            result_dict['rating'] = row[1]
            result_dict['description'] = row[2]
            result_list.append(result_dict)
        return result_list


def get_by_genre(genre):
    genre = str.lower(genre)
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                select title, description
                from netflix
                where lower(listed_in) like '%{genre}%'
        """
        cursor.execute(query)

        result_list = []
        for row in cursor.fetchall():
            result_dict = dict()
            result_dict['title'] = row[0]
            result_dict['description'] = row[1]
            result_list.append(result_dict)

        return result_list


