import json

from flask import Flask, render_template, jsonify, request, url_for
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fetch_cve_data')
def fetch_cve_data():
    base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    cves = []

    response = requests.get(f"{base_url}?resultsPerPage=10")

    if response.status_code == 200:
        data = response.json()
        cves_chunk = data.get("vulnerabilities", {})
        total_records = len(cves)
        cves.extend(cves_chunk)
    return jsonify({"cves": cves})


@app.route('/fetch_n_records', methods=['POST'])
def fetch_n():
    data = request.json
    n = data['topX']
    base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    cves = []
    response = requests.get(f"{base_url}?resultsPerPage={n}")
    if response.status_code == 200:
        data = response.json()
        cves_chunk = data.get("vulnerabilities", {})
        cves.extend(cves_chunk)
    return jsonify({"cves": cves})


@app.route('/fetch_cve_record', methods=['GET', 'POST'])
def fetch_cve_records():
    data = request.json
    print(data)
    cves = []
    cve = data['id']
    base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    response = requests.get(f"{base_url}?cveId={cve}")
    if response.status_code == 200:
        data = response.json()
        cves.append(data)
    print(response, cves, cve)
    with open('result_data.json', 'w') as file:
        json.dump({'response': cves}, file)

    return "SUS"


@app.route('/cve_record')
def cve_record():
    with open('result_data.json', 'r') as file:
        data = json.load(file)
        response_data = data['response'][0]['vulnerabilities']
    print("RESPON:::: ",response_data[0]['cve'])
    return render_template('cve_details.html', cve=response_data[0]['cve'])


if __name__ == '__main__':
    app.run(debug=True)
