
from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return """
    <h1>Welcome to AWS Cloud Computing Lab!</h1>
    <p>My Flask application is running successfully.</p>
    <p>Deployed using GitHub and AWS Elastic Beanstalk.</p>
    """

if __name__ == "__main__":
    application.run(debug=True)
