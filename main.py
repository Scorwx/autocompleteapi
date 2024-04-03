import subprocess
import importlib.util

def install_package(package):
    subprocess.check_call(["pip", "install", package])

def check_and_install(package_name):
    spec = importlib.util.find_spec(package_name)
    if spec is None:
        print(f"{package_name} paketi bulunamadı. Yükleniyor...")
        install_package(package_name)
    else:
        print(f"{package_name} zaten yüklü.")

packages_to_check = ["flask", "requests"]

for package in packages_to_check:
    check_and_install(package)

print("Gerekli paketler yüklendi.")


import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
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
    app.run(host="0.0.0.0")
