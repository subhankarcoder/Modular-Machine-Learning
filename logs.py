from flask import Flask
from src.logger import logging

app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def index():
  logging.info("GETING LOGGING MESSAGE HERE")

  return "FLASK APPLICATION RUNNING"

if __name__ == "__main__":
  app.run(debug=True)
