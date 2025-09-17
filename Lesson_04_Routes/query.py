from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return f"""<h2>Query Parameters </h2
            <ul>
                    <li><a href="/search">/search</a></li>
                    <li><a href="/search?q=python&page=2">/search?q=python&page=2</a></li>
            </ul>
"""
@app.route("/search")
def search():
    query = request.args.get('q', "Nothing!")
    page = request.args.get('page', '1')

    return f"Searching for '{query}' on page {page}."
@app.route("/products")
def search():
    price = request.args.get('max_price', type=float)
    page = request.args.get('page', '1',type=int)

    return f"Searching for '{price}' on page {page}."

if __name__ == "__main__":
    app.run(debug=True)