from flask import render_template, request
from forms import AddTransactionForm
from models import TransactionsModel
from app import app, db


@app.route("/")
def index():
    transactions = TransactionsModel.query.all()

    return render_template("index.html", transactions=transactions)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        add_transaction_form = AddTransactionForm(request.form)
        return render_template("add.html", add_transaction_form=add_transaction_form)
    elif request.method == 'POST':
        form = AddTransactionForm(request.form)

        if (form.validate()):
            # Read data from the form and store in the database.
            transaction = TransactionsModel(form.date.data, form.venue.data,
                                            form.cost.data, form.payer.data,
                                            form.attendees.data)

            db.session.add(transaction)

            # Save all pending changes to the database
            db.session.commit()

            # Get all of the transactions from the database to be displayed.
            transactions = TransactionsModel.query.all()

            return render_template("index.html", transactions=transactions)
        else:
            return render_template("add.html", add_transaction_form=form)
