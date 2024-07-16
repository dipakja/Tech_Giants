from flask import Flask, jsonify
from main import collect_telemetry_data

app = Flask(__name__)

@app.route('/telemetry/<int:utilization>', methods=['GET'])
def get_telemetry(utilization):
    data = collect_telemetry_data(utilization)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
