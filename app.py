from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    logging.info("################Logging Enabled##################")
    logging.info("#############Initiating application##############")
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)

    return 'CI CD pipeline Established'

if __name__=='__main__':
    app.run(debug=True)












