import os
from parler import Parler

jst = os.envrion['JST']
mst = os.environ['MST']

print(jst)

client = Parler(mst, jst)

print(client.getFeed())
