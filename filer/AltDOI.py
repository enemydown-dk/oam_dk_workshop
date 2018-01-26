'''Get altmetric information from API'''

import urllib.request
import urllib.error
import json
import csv

API_KEY = '0d3b46ee2c2b6jcd864693be02d4a0e7'
INPUT_FILE = 'in.csv'
EXPORT_FILE = 'out.txt'

def pull_data_api(url):
    '''request data from api and call function write_data'''
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        write_data(EXPORT_FILE, data)
        print(data)

    except urllib.error.HTTPError as _:
        print(_.reason)

def open_csv():
    '''open file with filename in INPUT_FILE and call function pull_data_api'''
    with open(INPUT_FILE, newline='') as _:
        reader = csv.reader(_, delimiter=';')
        #next(f)
        for row in reader:
            url = "http://api.altmetric.com/v1/doi/" + row[0] + "?key=" + API_KEY
            pull_data_api(url)

def write_data(file_name, data):
    '''write data to file with fame from EXPORT_FILE'''
    with open(file_name, mode="a") as file:
        file.write(json.dumps(data))

def main():
    '''this be main'''
    open_csv()


if __name__ == '__main__':
    main()
