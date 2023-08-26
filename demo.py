from flask import Flask
from Product_Recommendation_System.logger import logging

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info("Testing Logging file")
    return "Hi Earth"

if __name__== "__main__":
    app.run(debug=True)