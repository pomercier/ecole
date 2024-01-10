from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://www.tvanouvelles.ca/api/schools/closed"
    response = requests.get(url)
    data = response.json()["result"]["institutions"]
    df = pd.json_normalize(data)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    return df.to_html(header="true", table_id="table")

if __name__ == '__main__':
    app.run()
