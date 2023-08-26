from flask import Flask
from Product_Recommendation_System.logger import logging
from Product_Recommendation_System.exception import CustomException
import os, sys
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def  index():
    try:
        raise Exception("Testing Custom Exception file")
    except Exception as e:
        Product_Recommendation_System = CustomException(e, sys)
        logging.info(Product_Recommendation_System.error_message)
        logging.info("we are testing logging module")
        return "demo2.py testing"

    

if __name__=="__main__":
    app.run(debug=True)

