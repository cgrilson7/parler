import os
from parler import Parler

jst = os.environ['JST']
mst = os.environ['MST']

print(jst)

client = Parler(mst, jst)

print(client.searchHashtags())
