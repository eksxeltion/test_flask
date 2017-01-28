from flask import Flask, render_template, request
import yelp_places
import os

app = Flask(__name__)

@app.route("/")
def index():
    place = request.values.get('place')
    if place:
        search_term = request.values.get('term')
        return render_template('index.html', place=place, term=search_term, restaurants=yelp_places.get_top_places(search_term, place, 3))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)