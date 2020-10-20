from bs4 import BeautifulSoup
import requests
import webbrowser


def song_search(query: str):
    url = f'https://soundcloud.com/search?q={query.replace(" ", "%20")}'
    response = requests.get(url).text
    search = BeautifulSoup(response, 'html.parser')
    songs = search.find_all('li')[4:-4]
    return songs


def get_songs_and_link(songs):
    link_name_array = []
    for x in songs:
        song_split = str(x).replace('<li>', '').replace('</li>', '').replace('<h2>', '').replace('</h2>', '').split('>')
        link, song_name = song_split[0].replace('<a href=', '').replace('"', ''), song_split[1].replace('</a', '')
        link_name_array.append([song_name, link])
    return link_name_array


def choose_song(songs: list):
    i = 1
    for x in songs:
        print(f'{i}. {x[0]}')
        i += 1
    option = int(input('Choose a song: '))
    if (option >= 1) & (option <= i):
        webbrowser.open(f'https://soundcloud.com{songs[option][1]}')
