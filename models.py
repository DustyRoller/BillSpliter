class transaction(object):
    def __init__(self, date, venue, cost, payer, attendees):
        self.date = date
        self.venue = venue
        self.cost = cost
        self.payer = payer
        self.attendees = attendees

    def __repr__(self):
        return f"<Transaction {self.date} - {self.venue} - {self.cost}>"
