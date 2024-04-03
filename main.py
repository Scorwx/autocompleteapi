import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api')
def hello():
    args = request.args
    term = args.get("term")
    response = requests.get(f"https://www.enuygun.com/ucak-bileti/trip-autocomplete/?term={term}")
    data = response.json()
    airports = []
    for airport_info in data:
        airport = {
            "airport": airport_info['airport'],
            "city": airport_info['city_name'],
            "country": airport_info['country_name'],
            "id": airport_info['id']
        }
        airports.append(airport)
    
    return jsonify(airports)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
