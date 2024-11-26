from setup import *
from count_streams import *

#new dictionary including name & items
#items: for each track: grab trackName, remove track & add trackName to new dictionary to add back to original dictionary
#[{'name': 'clarity', 'items': ['Girls Need Love (with Drake) - Remix', 'Shot For Me', "When It's All Said And Done", 'Sorry', 'You Know Wassup', 'Toxic', 'Marvins Room', 'Loaded Gun', 'Doing It Wrong']},...
def clean(playlists):

    cleaned = []

    for obj in playlists:
        name = obj['name']
        items = []

        for track in obj['items']:
            if track['track'] != None:
                trackName = track['track']['trackName']
                items.append(trackName)
        
        new_clean = {'name': name, 'items': items}
        cleaned.append(new_clean)

    return cleaned

#counts = dictionary with counts
def count_max(counts, items):
    if items == None:
        return None
    
    (max_track, m) = (items[0], 0) #starter

    for track in items:
        (b, i) = search(counts, track) #returns index of count_max where track resides
        count = counts[i]['count'] #returns streaming count for this specific song
        if count > m:
            (max_track, m) = (track, count)

    return max_track


def top(counts):
    playlists = clean(get_playlists())

    top_tracks = []

    for playlist in playlists:
        name = playlist['name']
        items = playlist['items']
        ttrack = {'name': name, 'top track': count_max(counts, items)}
        top_tracks.append(ttrack)
    
    return top_tracks

def specific_playlist_top(playlistName):
    counts = count()
    top_tracks = top(counts)

    for playlist in top_tracks:
        if playlist['name'] == playlistName:
            return playlist
    
    return None

#doesn't work if the playlist does not exist
def grab_items(playlists, playlistName):
    for playlist in playlists:
        if (playlist['name'] == playlistName):
            items = playlist['items']
    
    return items


def top_ten(playlistName, counts):
    playlists = clean(get_playlists())

    items = grab_items(playlists, playlistName)
    top10 = []
    i = 0

    while(i < 10):
        top = count_max(counts, items)
        if top != None:
            top10.append(top)
            items.remove(top)
            i = i+1
        else:
            i = 10
    
    return top10

def top_twenty(playlistName, counts):
    playlists = clean(get_playlists())

    items = grab_items(playlists, playlistName)
    top20 = []
    i = 0

    while(i < 20):
        top = count_max(counts, items)
        if top != None:
            top20.append(top)
            items.remove(top)
            i = i+1
        else:
            i = 20
    
    return top20

print(top_twenty('pop a bing', count()))

