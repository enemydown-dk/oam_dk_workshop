#!/usr/bin/env python3

"""OADOI lookup via DOI from .csv"""

import urllib.request
import urllib.error
import json
import csv

URL = 'https://api.oadoi.org/' #URL til API'et
MAIL = 'lajh@kb.dk' #angiv din e-mail her, påkrævet for at undgå blacklist.
FILE_NAME = 'ind.csv' #angiv filnavn på den fil der indeholder din DOI-liste.
JSON_NAME = 'json.txt' #angiv et filnavn på den fil, hvor du ønsker output.

def pull_data_api(url):
    """Udfører forespørgslen i API og returnerer evt. fejlkoder til terminal"""
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        write_json_2_csv(JSON_NAME, data)
        print(data)

    except urllib.error.HTTPError as _:
        print(_.reason)

def open_csv():
    """Åbner filen i variablen FILE_NAME og læser DOI en efter en + kalder pullDataAPI"""
    with open(FILE_NAME, newline='') as _:
        reader = csv.reader(_, delimiter=';')
        next(_)
        for row in reader:
            pull_data_api(URL + row[0] + '?email=' + MAIL)

def write_json_2_csv(json_name, data):
    """Open filen i variablen JSON_NAME i append format, og skriver herefter data"""
    with open(json_name, mode="a") as file:
        file.write(json.dumps(data))

def main():
    """main"""
    open_csv()

if __name__ == '__main__':
    main()
