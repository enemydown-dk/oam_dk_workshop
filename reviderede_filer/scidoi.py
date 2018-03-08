"""
Extracts OA metadata from Science Direct.
"""

import urllib.request
import urllib.error
import json
import csv

APIKEY = '64ca3ad5b69086dca1Ac2a9b9c8166cb' #indtast din APIkey fra Science Direct her (denne er fiktiv).
FILE_NAME = 'doiliste.csv' #navn på inputfil her.
JSON_NAME = 'json.txt' #navn på output fil her.

def pull_data_api(url):
    """Opslag i Science Direct API"""
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        write_json_2_csv(JSON_NAME, data)
        print(data)

    except urllib.error.HTTPError as _:
        print(_.reason)

def open_csv():
    """Læser inputfilen i variablen FILE_NAME"""
    with open(FILE_NAME, newline='') as _:
        reader = csv.reader(_, delimiter=';')
        for row in reader:
            wos_url = "https://api.elsevier.com/content/article/doi/" \
            + row[0] + "?apiKey=" + APIKEY + "&httpAccept=application%2Fjson"
            pull_data_api(wos_url)

def write_json_2_csv(json_name, data):
    """Skriver datastrøm (json) til outputfilen i variablen JSON_NAME"""
    with open(json_name, mode="a") as file:
        file.write(json.dumps(data))

def main():
    """main"""
    open_csv()

if __name__ == '__main__':
    main()
