import requests

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

headers = {
    'x-rapidapi-key': "8365320523mshaf467a058e25ebfp18d73djsn90c6460a48a2",
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
}


def search(title):
    querystring = {"s": title, "page": "1", "r": "json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    json = response.json()
    return json


def search_by_id(pk):
    querystring = {"i": pk, "r": "json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    json = response.json()
    return json
