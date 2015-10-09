from app import app
import json
import csv
import os
import models
from app import db
# __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')


def generator():
    csvfile = open(os.path.join(APP_STATIC, 'file.csv'), 'r')
    reader = csv.DictReader( csvfile)
    out = [dict(r) for r in reader]
    for row in  out:
        json_row = json.dumps(row)
        x = models.JSON_TABLE(json_row)
        db.session.add(x)
    db.session.commit()
