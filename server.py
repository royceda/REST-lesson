from flask import request, Flask, make_response, json
from services import flights, edit_flight, create_flight, get_flight
#import json

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/flights')
def get_flights():
    flt = flights()
    response = app.response_class(
        response = json.dumps(flt),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/flight/<string:op_nb>', methods=["GET", "POST", "DELETE", "PUT"])
def flight(op_nb):
    
    if request.method == "GET":
        # Get The flight
        print(op_nb)
        flt = get_flight(op_nb);
        response = app.response_class(
            response = json.dumps(flt),
            status=200,
            mimetype='application/json'
        )
        return response

    if request.method == "POST":
        # Create the flight
        data = request.get_json();
        print(op_nb)
        print(data['ori'])
        #flt = create_flight()
        response = app.response_class(
            response = json.dumps(
                {
                    "data": "OK"
                }),
            status=200,
            mimetype='application/json'
        )
        return response

    if request.method == "PUT":
        # Edit flight
        data = request.get_json();
        print(op_nb)
        print(data['ori'])
        #edit_flight(data['op_nb'], data['ori'], data['dst'])
        response = app.response_class(
            response = json.dumps(
                {
                    "data": "OK"
                }),
            status=200,
            mimetype='application/json'
        )
        return response


if __name__ == "__main__":
    app.run(port=7777)
    pass