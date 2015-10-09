from app import app
import generator
import models
import json
import csv
import os
from app import db
# __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')

# @app.route('/generate')
# def index():
#       generator.generator()
#       return "Fetched all the json"


@app.route('/fetch/<row_no>')
def fetch(row_no):
      a = []
      x =  models.JSON_TABLE.query.all()
      return x[int(row_no)].json_row

# @app.route('/demo')
# def demo():
#     return ""


@app.route('/generate')
def generate():
      csvfile = open(os.path.join(APP_STATIC, 'second.csv'), 'rb')
      reader = csv.DictReader( csvfile)
      clm_no = "$"
      jsondict = {}
      for row in reader:
          if row['clm_no'] == clm_no:
             jsondict[clm_no].append(row)
          else:
             clm_no = row['clm_no']
             jsondict.update({clm_no:[]})
             jsondict[clm_no].append(row)
      for key in  jsondict:
         x = models.JSON_TABLE(int(key),(json.dumps(jsondict[key])))
         db.session.add(x)

      db.session.commit()
      return "Table updated  from csv"
