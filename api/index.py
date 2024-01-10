import requests
import json
import pandas as pd

url = "https://www.tvanouvelles.ca/api/schools/closed"
response = requests.get(url)
data = response.json()["result"]["institutions"]

df = pd.json_normalize(data)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
df
