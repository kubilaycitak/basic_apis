import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Creating data in the form of a list of dictionaries.
matches = [
    {'id': 0,
     'match_date': '2016-12-18',
     'team_1': 'CLOUD9',
     'team_2': 'HELLRAISERS',
     't1_points': 13,
     't2_points': 16,
     't1_world_rank': 9,
     't2_world_rank': 20,
     'winner': 't2'},
    {'id': 1,
     'match_date': '2016-12-18',
     'team_1': 'IMMORTALS',
     'team_2': 'G2',
     't1_points': 17,
     't2_points': 19,
     't1_world_rank': 13,
     't2_world_rank': 10,
     'winner': 't2'},
    {'id': 2,
     'match_date': '2016-12-18',
     'team_1': 'MOUSESPORTS',
     'team_2': 'IMMORTALS',
     't1_points': 16,
     't2_points': 3,
     't1_world_rank': 12,
     't2_world_rank': 13,
     'winner': 't1'},
    {'id': 3,
     'match_date': '2016-12-18',
     'team_1': 'DIGNITAS',
     'team_2': 'G2',
     't1_points': 16,
     't2_points': 9,
     't1_world_rank': 6,
     't2_world_rank': 10,
     'winner': 't1'},
    {'id': 4,
     'match_date': '2016-12-18',
     'team_1': 'OPTIC',
     'team_2': 'HELLRAISERS',
     't1_points': 16,
     't2_points': 10,
     't1_world_rank': 4,
     't2_world_rank': 20,
     'winner': 't1'},
]


# Defining home page.
@app.route('/', methods=['GET'])
def home():
    return '''<h1>CS:GO Matches Archive</h1>
<p>A prototype API for CS:GO matches.</p>'''


# Defining the page that includes all the data.
@app.route('/api/v1/resources/matches/all', methods=['GET'])
def api_all():
    return jsonify(matches)


# Defining the page that gets a data with specified details.
@app.route('/api/v1/resources/matches', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Creating an empty list for the results
    results = []

    # Looping through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for match in matches:
        if match['id'] == id:
            results.append(match)

    # Using the jsonify function to convert the list of dictionaries to the JSON format.
    return jsonify(results)

app.run()