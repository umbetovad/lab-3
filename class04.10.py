from flask import Flask, request 
from flask import url_for 
from flask import render_template 
import psycopg2
import requests

url = "https://solana-gateway.moralis.io/nft/mainnet/{}/metadata"

headers = {
    "accept": "application/json",
    "X-API-Key": "KdYyLJOktNwuiRJLbzjxY5w1sM5Pw2mCDXoxkZIwCY1sZnInGHEXsZFnubmeaR2Y"
}


conn = psycopg2.connect(database="python", user = "postgres", password = "12345", host = "127.0.0.1", port = "5432")
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS nft (name text, count integer)')

conn.commit()

app = Flask(__name__) 
 
@app.route('/',  methods=['GET', 'POST']) 
def index(): 
    if request.method == 'POST':
        address = request.form.get('a')
        response = requests.get(url.format(address), headers=headers)

        print (response.text)
    return render_template('index.html')
 

if __name__ == '__main__': 
    app.run(debug=True)

