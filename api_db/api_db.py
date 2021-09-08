import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Defining a function that returns items from the database as dictionaries rather than lists.
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Defining home page.
@app.route('/', methods=['GET'])
def home():
    return '''<h1>CS:GO Matches Archive</h1>
<p>A prototype API for CS:GO matches.</p>'''


# Defining the connection object.
@app.route('/api/v1/resources/matches/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('matches.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_matches = cur.execute('SELECT * FROM csgo_matches;').fetchall()

    return jsonify(all_matches)


# Defining a function to return 404 pages when something goes wrong.
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# Creating a function that returns results based on several details.
@app.route('/api/v1/resources/matches', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    match_date = query_parameters.get('match_date ')
    team_1 = query_parameters.get('team_1')
    team_2 = query_parameters.get('team_2')
    t1_world_rank = query_parameters.get('t1_world_rank')
    t2_world_rank = query_parameters.get('t2_world_rank')
    

    # Building the SQL query that will be used to find the requested data
    query = "SELECT * FROM csgo_matches WHERE"
    to_filter = []
    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if match_date:
        query += ' match_date=? AND'
        to_filter.append(match_date)
    if team_1:
        query += ' team_1=? AND'
        to_filter.append(team_1)
    if team_2:
        query += ' team_2=? AND'
        to_filter.append(team_2)
    if t1_world_rank:
        query += ' t1_world_rank=? AND'
        to_filter.append(t1_world_rank)
    if t2_world_rank:
        query += ' t2_world_rank=? AND'
        to_filter.append(t2_world_rank)
    if not (id or match_date or team_1 or team_2 or t1_world_rank or t2_world_rank):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('matches.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()