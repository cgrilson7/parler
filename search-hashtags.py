import os
from parler import Parler

jst = os.environ['jst']
mst = os.environ['mst']

print(jst)

client = Parler(mst, jst)

print(client.hashtagSearch('stopthesteal'))
