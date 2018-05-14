from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars.py


app = Flask(__name__)

mongo = PyMongo(app)

# Create a root route that will query your mongo db and pass the mars data into an html template
@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)

# Create a route called scrape that will import your scrape_mars.py script and call your scrape function
@app.route('/scrape')
def scrape():
    mars = mongo.db.mars
    data = scrape_mars.scrape()
    # Store the return value in Mongo as a Python dictionary
    mars.update(
        {},
        data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)






