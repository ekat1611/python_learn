import requests
from Artsy import User

user = User()


def auth():
    auth_response = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                      data={
                          "client_id": user.client_id,
                          "client_secret": user.client_secret
                      })

    return auth_response.json().get('token')


headers = {"X-Xapp-Token": auth()}

with open("/Users/user/Downloads/dataset_24476_4 (4).txt".encode('utf8')) as artists:
    artists_dct = {}
    for artist in artists.readlines():
        response = requests.get(f"https://api.artsy.net/api/artists/{artist.rstrip()}", headers=headers).json()
        artists_dct[response.get("sortable_name")] = response.get("birthday")

for i in sorted(artists_dct, key=artists_dct.get):
    print(i)