from app import db

class TransactionsModel(db.Model):
    __tablename__ = "Transactions"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    venue = db.Column(db.String)
    cost = db.Column(db.Float)
    payer = db.Column(db.String)
    attendees = db.Column(db.String)
    
    def __init__(self, date, venue, cost, payer, attendees):
        self.date = date
        self.venue = venue
        self.cost = cost
        self.payer = payer
        self.attendees = attendees

    def __repr__(self):
        return f"<Transaction {self.date} - {self.venue} - {self.cost}>"

if __name__ == "__main__":
    # Run this file directly to create the database tables.
    print ("Creating database tables...")
    db.create_all()
    print ("Done!")
