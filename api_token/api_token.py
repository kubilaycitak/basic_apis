from flask import Flask, jsonify, request, make_response
import jwt 
import datetime
from functools import wraps

app = Flask(__name__)

# Defining a secret key.
app.config['SECRET_KEY'] = 'thisisthesecretkey'

# Defining a function that runs the process depending of the validation of the key.
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 403
        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
        except Exception as inst:
            print(inst)
            return jsonify({'message' : 'Token is invalid!'}), 403

        return f(*args, **kwargs)

    return decorated

# Specifying the key required/not-required endpoints
@app.route('/unprotected')
def unprotected():
    return jsonify({'message' : 'This page does not require a key'})

@app.route('/protected')
@token_required
def protected():
    return jsonify({'message' : 'This page requires a key'})

# Logging in
@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'admin':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=15)}, app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({'token' : token})

    return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})


app.run(debug=True)