from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class All(Resource):
    # Defining home page.
    @app.route('/', methods=['GET'])
    def home():
    	return '''<h1>CS:GO Matches Archive</h1>
	<p>A prototype API for CS:GO matches.</p>'''

    def get(self):
        data = pd.read_csv('matches.csv')
        data = data.to_dict('records')
        to_re = {'data' : data}, 200
        return jsonify(to_re)

    # Parsing the input and adding a row to CSV when POST is called
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', required=True)
        parser.add_argument('team_1', required=True)
        parser.add_argument('team_2', required=True)
        parser.add_argument('t1_world_rank', required=True)
        parser.add_argument('t2_world_rank', required=True)
        parser.add_argument('winner', required=True)
        args = parser.parse_args()

        data = pd.read_csv('matches.csv')

        new_data = pd.DataFrame({
            'id'            : [args['id']],
            'team_1'        : [args['team_1']],
            'team_2'        : [args['team_2']],
            't1_world_rank' : [args['t1_world_rank']],
            't12_world_rank': [args['t2_world_rank']],
            'winner'        : [args['winner']]
        })

        data = data.append(new_data, ignore_index = True)
        data.to_csv('matches.csv', index=False)
        return {'data' : new_data.to_dict('records')}, 201


    # Deleting a record when DELETE is called
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()

        data = pd.read_csv('matches.csv')
        data = data[data['name'] != args['name']]
        data.to_csv('matches.csv', index=False)
        return {'message' : 'Record deleted successfully.'}, 200


# Showing if the first team won or second
class Winners(Resource):
    def get(self):
        data = pd.read_csv('matches.csv',usecols=[8])
        data = data.to_dict('records')
        
        return {'data' : data}, 200



# Adding URL endpoints
api.add_resource(All, '/all')
api.add_resource(Winners, '/winners')


app.run()
