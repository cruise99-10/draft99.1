from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca=certifi.where()

client = MongoClient("mongodb+srv://test:test@cluster0.15fhovx.mongodb.net/test", tlsCAFile=ca)
db = client.dbsparta_plus_week4

SECRET_KEY = 'SPARTA'
import jwt
import datetime
import hashlib


import sys
sys.path.append(["/home","/user","/community","/book","/review"])

from user.user import *
from home.home import *
from community.community import *
from book.book import *
from review.review import *
