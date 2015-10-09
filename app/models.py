from app import db

class JSON_TABLE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    claim_id = db.Column(db.Integer)
    json_row = db.Column(db.String(1000))

    def __init__(self, claim_id,json_row):
        self.claim_id = claim_id
        self.json_row = json_row
db.create_all()
