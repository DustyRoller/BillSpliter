from flask import render_template, request
from models import transaction
from app import app
import sys

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    print('This is error output', file=sys.stderr)
    if request.method == "GET":
        return render_template("add.html", action="Add")

    # Because we 'returned' for a 'GET', if we get to this next bit, we must
    # have received a POST

    # Get the incoming data from the request.form dictionary.
    # The values on the right, inside get(), correspond to the 'name'
    # values in the HTML form that was submitted.

    transaction_date = request.form.get("date_field")
    if transaction_date == "":
        return render_template("add.html", action="Add", message="Invalid date")
    transaction_venue = request.form.get("venue_field")
    if transaction_venue == "":
        return render_template("add.html", action="Add", message="Invalid venue")
    transaction_cost = request.form.get("cost_field")
    if transaction_cost == "":
        return render_template("add.html", action="Add", message="Invalid cost")
    transaction_payer = request.form.get("payer_field")
    if transaction_payer == "":
        return render_template("add.html", action="Add", message="Invalid payer")
    transaction_attendees = request.form.get("attendees_field")
    if transaction_attendees == "":
        return render_template("add.html", action="Add", message="Invalid attendees")

    t = transaction(transaction_date, transaction_venue, transaction_cost, transaction_payer, transaction_attendees)

    return render_template("index.html", transaction=t)
