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
        raw_actors_list_1 = []
        for row in cursor.fetchall():
            raw_actors_list_1.append(row)

        raw_actors_list = []
        for item in raw_actors_list_1:
            x = " ".join(item)
            raw_actors_list.append(x)
        raw_actors_list = str(raw_actors_list)
        raw_actors_list = raw_actors_list.replace("[", "")
        raw_actors_list = raw_actors_list.replace("]", "")
        raw_actors_list = raw_actors_list.replace("'", "")
        raw_actors_list = str.split(raw_actors_list, ", ")

        return raw_actors_list

def counter_more_than_twice(name1='Jack Black', name2='Dustin Hoffman'):
    actors = raw_actors(name1, name2)
    counter = 1
    actors_more_than_twice = []
    for item in actors:
        if item != name1 and item != name2:
            if actors.count(item) > 2:
                actors_dict = dict()
                actors_dict['actor'] = item
                actors_dict['counter'] = actors.count(item)
                actors_more_than_twice.append(actors_dict)
    unique_list = []
    for item in actors_more_than_twice:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

print(counter_more_than_twice('Rose McIver',  'Ben Lamb'))