import ast
import json
from typing import List
from os import listdir

#converts all streaming files to list of python dictionaries
#each element of list is {'endTime': '2021-07-27 16:56', 'artistName': 'The Weeknd', 'trackName': 'Reminder', 'msPlayed': 68266}
def get_streamings(path: str = 'data') -> List[dict]:
    
    files = ['data/' + x for x in listdir(path)
             if x.split('.')[0][:-1] == 'StreamingHistory']
    
    all_streamings = []
    
    for file in files: 
        with open(file, 'r', encoding='UTF-8') as f:
            new_streamings = ast.literal_eval(f.read())
            all_streamings += [streaming for streaming 
                               in new_streamings]
    return all_streamings

#converts all playlist files to list of python dictionaries
#each element of list is {'name': 'clarity', 'lastModifiedDate': '2022-01-28', 'items': [{'track': {'trackName': 'Girls Need Love (with Drake) - Remix', 'artistName': 'Summer Walker', 'albumName': 'Last Day Of Summer', 'trackUri': 'spotify:track:14SaZBTjxlorHJQxXh01Hu'}, 'episode': None, 'localTrack': None},...
def get_playlists(path: str = 'data') -> List[dict]:
    files = ['data/' + x for x in listdir(path)
             if x.split('.')[0][:-1] == 'Playlist']
    
    all_playlists = []

    for file in files: 
        with open(file, 'r', encoding='UTF-8') as f:
            data = json.load(f)
            all_playlists += data['playlists']
    
    return all_playlists
