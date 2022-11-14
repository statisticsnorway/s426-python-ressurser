import pandas as pd
import requests
import json
from io import StringIO 
from pyjstat import pyjstat
import urllib.request, json

def hent_klass_data(klassifikasjonsliste, lagringsplass = "Metadata/"):
    if klassifikasjonsliste == "kommune":
        url = 'https://data.ssb.no/api/klass/v1/classifications/131/codesAt.json?date=2021-01-19&presentationNamePattern=%7Bcode%7D%20%7Bname%7D'
        kommuner = pd.read_json(url)['codes']
        kommuner = pd.json_normalize(kommuner)
        kommuner = kommuner.rename(columns={
            'code': 'Kommunenummer',
            'name': 'Kommunenavn',
            'presentationName': 'Kommune'
        })
        kommuner = kommuner[["Kommunenummer", "Kommunenavn", "Kommune"]]
        kommuner = kommuner.set_index("Kommune")
        kommuner.to_json(f'{lagringsplass}kommuner.json', orient = "index")
    if klassifikasjonsliste == "fylke":
        url = 'https://data.ssb.no/api/klass/v1/classifications/104/codesAt.json?date=2021-01-19&presentationNamePattern=%7Bcode%7D%20%7Bname%7D'
        fylker = pd.read_json(url)['codes']
        fylker = pd.json_normalize(fylker)
        fylker = fylker.rename(columns={
            'code': 'Fylkenummer',
            'name': 'Fylkenavn',
            'presentationName': 'Fylke'
        })
        fylker = fylker[["Fylkenummer", "Fylkenavn", "Fylke"]]
        fylker = fylker.set_index("Fylke")
        fylker.to_json(f'{lagringsplass}fylker.json', orient = "index")