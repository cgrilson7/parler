import os
from parler import Parler

jst = os.environ['jst']
mst = os.environ['mst']

client = Parler(mst, jst)

import json

with open("hashtags_2.json", "r") as read_file:
    data = json.load(read_file)

print(data)

import time
import ast

results = []
for hashtag in data['hashtags']:
    current = str(client.hashtagSearch(hashtag))
    current_eval = ast.literal_eval(current)
    current_eval['time'] = time.time()
    results.append(current_eval)
    time.sleep(2)

with open("hashtag_search_results.json") as data_file:
    past_results = json.load(data_file)

results = past_results + results

with open('hashtag_search_results.json', 'w') as outfile:
    json.dump(results, outfile)
    