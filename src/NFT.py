import requests
from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy
from Model import Nft, app, db

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def nft_page():
    return render_template('nft_page.html')


@app.route('/nft_search', methods=['GET'])
def nft_search():
    args = request.args['args']
   
    url = f"https://solana-gateway.moralis.io/nft/mainnet/{args}/metadata"

    headers = {

        "accept": "application/json",

        "X-API-Key": "ehP9BUwX165OuRbiGBRu1CoJzKC9hI3IaTTBGSb3MjJ139NS6T6wcWrHBK7P25SD"

    }

    response = requests.get(url, headers=headers)

    nft = Nft()                                     
    dbExist = nft.checkInDb(args)


    if dbExist:
        payload = dbExist
        return make_response(render_template('nft_result.html', payload=payload))

    response2 = response.json()
   
    
    payload = {
        "name": response2["name"],
        "description": response2["metaplex"]["metadataUri"],
        "address": response2["mint"]

    }

    nft = Nft(**payload)

    nft.addToDb()
    
    return make_response(render_template('nft_result.html', payload=payload))

if __name__ == "__main__":
    app.run(debug=True)