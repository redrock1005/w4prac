from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.jl043qw.mongodb.net/?retryWrites=true&w=majority', tlsCAFile = ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods=['POST'])
def test_post():
    url_give = request.form['url_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_give, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    contents = soup.select('#contents > div.movie-info-container > div.movie-header-area')
    for content in contents:
        content_title = content.select_one('div > h3').text
        image_url = content.select_one('div > img')['src']

    data = []
    actors_name = soup.select('#synopsis > article:nth-child(7) > div > div')
    for actor_name in actors_name:
        actors = actor_name.select_one('div.name').text
        if actors is not None:
            actor = actors
            data.append({'actor':actor})

    Synops = soup.select('#synopsis > article:nth-child(1)')
    for Synop in Synops:
        synop = Synop.select_one('p').text


    doc={
        'title':content_title,
        'image':image_url,
         'actor':data,
        'synop':synop,
    }
    db.w4prac.insert_one(doc)
    return jsonify({'msg': '저장 완료'})



if __name__ == '__main__':
   app.run('0.0.0.0',port=4000,debug=True)


# URL을 읽어서 HTML를 받아오고,




