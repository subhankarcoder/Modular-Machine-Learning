from flask import Flask
from src.logger import logging
from src.exception import CustomExceptionClass
import os, sys

app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def index():
  try: 
    raise Exception("TESTING EXCEPTION FILE")
  except Exception as e:
    ML = CustomExceptionClass(e,sys)
    logging.info(ML.error_message)
    logging.info("GETING LOGGING MESSAGE HERE")

    return "FLASK APPLICATION RUNNING"

if __name__ == "__main__":
  app.run(debug=True)