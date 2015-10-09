import json
import csv
import os
# __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')


csvfile = open(os.path.join(APP_STATIC, 'file2.csv'), 'rb')
reader = csv.DictReader( csvfile)
clm_no =  '$'
jsondict = {}

for row in reader:
    if row['clm_no'] == clm_no:
       jsondict[clm_no].append(row)
    else:
       clm_no = row['clm_no']
       jsondict.update({clm_no: []})
       jsondict[clm_no].append(row)
print jsondict['10181012']

for key,value in  jsondict:
    x = models.JSON_TABLE(key,value)
    db.session.add(x)

db.session.commit()
