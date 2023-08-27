from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a strong secret key

# Sample product data (you might use a database in a real application)
products = [
    {"id": 1, "name": "Product 1", "price": 10.0},
    {"id": 2, "name": "Product 2", "price": 20.0},
    {"id": 3, "name": "Product 3", "price": 15.0},
]

@app.route("/")
def index():
    return render_template("index.html", products=products)

@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(product_id)
    return redirect(url_for("index"))

@app.route("/cart")
def cart():
    cart_items = [product for product in products if product["id"] in session.get("cart", [])]
    total_price = sum(product["price"] for product in cart_items)
    return render_template("cart.html", cart_items=cart_items, total_price=total_price)

if __name__ == "__main__":
    app.run(debug=True)
