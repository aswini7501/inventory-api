# main.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
   return "Inventory API is running!"

@app.route("/login")
def login():
   return "Login Page"

