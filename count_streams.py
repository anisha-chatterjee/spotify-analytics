from setup import *

#searches for trackName if it exists in countstreams
#returns (exists, i) where i is the index of the trackName dictionary
#exists: true = 1, false = 0
def search(streams, trackName):
    for i, obj in enumerate(streams):
        if obj['trackName']==trackName:
            return (1, i)
    return (0, 0)

#removes endTime, msPlayed from each song dictionary
def clean(streams):
    for obj in streams:
        del(obj['endTime'])
        del(obj['msPlayed'])
    
    return streams

#adds "count" element to each song dictionary in list
def count():
    streamings = get_streamings()

    #countstreams - new list of unique song dictionaries & added "count" element
    countstreams = []

    for obj in streamings:
        trackName = obj['trackName']
        ms = obj['msPlayed']

        #only counts as a stream if >30 seconds
        if ms >= 30000:
            #if it already exists in countstreams, index in list where
            (exists, i) = search(countstreams, trackName)
            if exists==1:
                countstreams[i]['count'] = countstreams[i]['count'] + 1
            else:
                countstreams.append(obj)
                countstreams[len(countstreams)-1]['count'] = 1
    
    #removes endTime & msPlayed entrie
    cleaned = clean(countstreams)
    return cleaned
