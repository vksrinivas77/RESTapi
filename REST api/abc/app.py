from flask import Flask
app = Flask(__name__)
import controller.controller as  controller

@app.route('/')
def user():
    return "hello word"
