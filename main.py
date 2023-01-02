from flask import Flask, jsonify
from utils import search_title, get_by_releases_period, get_kids_films, get_family_films, get_adult_films, get_by_genre

app = Flask(__name__, template_folder='templates')


@app.route('/movie/<title>')
def page_movie_info(title):
    movie = search_title(title)
    return jsonify(movie)


@app.route('/movie/<int:year1>/to/<int:year2>')
def page_movie_periods(year1, year2):
    movies = get_by_releases_period(year1, year2)
    return jsonify(movies)


@app.route('/rating/children')
def kids_films():
    movies = get_kids_films()
    return jsonify(movies)


@app.route('/rating/family')
def family_films():
    movies = get_family_films()
    return jsonify(movies)


@app.route('/rating/adult')
def adult_films():
    movies = get_adult_films()
    return jsonify(movies)


@app.route('/genre/<genre>')
def by_genre(genre):
    movies = get_by_genre(genre)
    return jsonify(movies)


if __name__ == '__main__':
    app.run()