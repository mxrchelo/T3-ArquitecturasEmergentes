from flask import Flask, jsonify, request
import utils
from db import create_tables

app = Flask(__name__)


@app.route('/locations/<company_api_key>', methods=["GET"])
def get_locations(company_api_key):
    locations = utils.get_locations(company_api_key)
    return jsonify(locations)

@app.route("/location/<company_api_key>", methods=["PUT"])
def update_location(company_api_key):
    location_details = request.get_json()
    id = location_details["id"]
    name = location_details["name"]
    country = location_details["country"]
    city = location_details["city"]
    meta = location_details["meta"]
    result = utils.update_location(company_api_key, id, name, country, city, meta)
    return jsonify(result)

@app.route("/location/<company_api_key>/<id>", methods=["DELETE"])
def delete_location(company_api_key,id):
    result = utils.delete_location(company_api_key,id)
    return jsonify(result)

@app.route("/location/<company_api_key>/<id>", methods=["GET"])
def get_location_by_id(company_api_key,id):
    location = utils.get_by_id(company_api_key,id)
    return jsonify(location)

@app.route("/locations/<company_api_key>", methods=["POST"])
def insert_locations(company_api_key):
    location_details = request.get_json()
    company_id = location_details["company_id"]
    name = location_details["name"]
    country = location_details["country"]
    city = location_details["city"]
    meta = location_details["meta"]
    result = utils.insert_location(company_api_key,company_id, name, country, city, meta)
    return jsonify(result)




@app.route('/sensors/<company_api_key>', methods=["GET"])
def get_sensors(company_api_key):
    sensors = utils.get_sensors(company_api_key)
    return jsonify(sensors)


@app.route("/sensor/<company_api_key>", methods=["POST"])
def insert_sensor(company_api_key):
    sensor_details = request.get_json()
    location_id = sensor_details["location_id"]
    name = sensor_details["name"]
    category = sensor_details["category"]
    meta = sensor_details["meta"]
    api_key = sensor_details["api_key"]
    result = utils.insert_sensor(company_api_key, location_id, name, category, meta, api_key)
    return jsonify(result)


@app.route("/sensor/<company_api_key>", methods=["PUT"])
def update_sensor(company_api_key):
    sensor_details = request.get_json()
    id = sensor_details["id"]
    location_id = sensor_details["location_id"]
    name = sensor_details["name"]
    category = sensor_details["category"]
    meta = sensor_details["meta"]
    result = utils.update_sensor(company_api_key, id, location_id, name, category, meta)
    return jsonify(result)


@app.route("/sensor/<company_api_key>/<id>", methods=["DELETE"])
def delete_sensor(company_api_key,id):
    result = utils.delete_sensor(company_api_key, id)
    return jsonify(result)


@app.route("/sensor/<company_api_key>/<id>", methods=["GET"])
def get_sensor_by_id(company_api_key,id):
    sensor = utils.get_by_id(company_api_key, id)
    return jsonify(sensor)


@app.route('/sensors_data/<sensor_api_key>', methods=["GET"])
def get_list_sensor_data(sensor_api_key):
    sensor_details = request.get_json()
    list = sensor_details["list"]
    sensors = utils.get_list_sensor_data(sensor_api_key, list)
    return jsonify(sensors)


@app.route("/sensor_data/<sensor_api_key>", methods=["POST"])
def insert_sensor_data(sensor_api_key):
    sensor_details = request.get_json()
    name = sensor_details["name"]
    data = sensor_details["data"]
    date = sensor_details["date"]
    result = utils.insert_sensor(sensor_api_key, name, data, date)
    return jsonify(result)


@app.route("/sensor_data/<sensor_api_key>", methods=["PUT"])
def update_sensor_data(sensor_api_key):
    sensor_details = request.get_json()
    id = sensor_details["id"]
    name = sensor_details["name"]
    data = sensor_details["data"]
    date = sensor_details["date"]
    result = utils.update_sensor_data(sensor_api_key, id, name, data, date)
    return jsonify(result)


@app.route("/sensor_data/<sensor_api_key>/<id>", methods=["DELETE"])
def delete_sensor_data(sensor_api_key,id):
    result = utils.delete_sensor_data(sensor_api_key, id)
    return jsonify(result)


@app.route("/sensor_data/<sensor_api_key>/<id>", methods=["GET"])
def get_sensor_data_by_id(sensor_api_key,id):
    sensor = utils.get_sensor_data_by_id(sensor_api_key, id)
    return jsonify(sensor)



if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=False)