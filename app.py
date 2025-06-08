from flask import Flask, request, jsonify
from flask_cors import CORS
from weather_service import get_weather_data
from db import init_db, insert_weather, get_all_weather, update_weather, delete_weather

app = Flask(__name__)
CORS(app)
init_db()

@app.route('/weather', methods=['POST'])
def fetch_weather():
    data = request.json
    location = data.get("location")
    weather = get_weather_data(location)
    if weather:
        insert_weather(weather['location'], weather['temp'])  # save to DB
        return jsonify(weather)
    return jsonify({"error": "Could not fetch weather"}), 400

@app.route('/weather', methods=['GET'])
def read_weather():
    return jsonify(get_all_weather())

@app.route('/weather/<int:weather_id>', methods=['PUT'])
def update_weather_entry(weather_id):
    data = request.json
    new_temp = data.get("temperature")
    if update_weather(weather_id, new_temp):
        return jsonify({"message": "Weather entry updated."})
    return jsonify({"error": "Entry not found."}), 404

@app.route('/weather/<int:weather_id>', methods=['DELETE'])
def delete_weather_entry(weather_id):
    if delete_weather(weather_id):
        return jsonify({"message": "Weather entry deleted."})
    return jsonify({"error": "Entry not found."}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)
