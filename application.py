from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return "<h1>Flask App Successfully Deployed!</h1>"
