from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient("mongodb+srv://test:sparta@cluster0.m9zv2vc.mongodb.net/?retryWrites=true&w=majority")
db = client.dbsparta


@app.route('/')
def home():
    return render_template('review.html')


@app.route("/library/write", methods=["POST"])
def posting():
    url_receive = request.form['url_give']
    reviewcomment_receive = request.form['reviewcomment_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']

    doc ={
        'title':title,
        'image':image,
        'desc':desc,
        'reviewcomment':reviewcomment_receive
    }
    db.reviews.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)