from flask import render_template
from app import app
from models.online_shop import all_orders

@app.route("/orders")
def index():
    return render_template("index.html", title="Home", all_orders=all_orders)



# Extension - Create a new route
# <index> is the value we type in the browser, e.g.  /1
@app.route("/orders/<index>")
def order(index):
    index_num = int(index)
    order = all_orders[index_num]
    return render_template("order.html", title="Single order", order=order)