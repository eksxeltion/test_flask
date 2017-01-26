from flask import Flask, render_template, request
import weather
import os

app = Flask(__name__)

@app.route("/")
def index():
    place = request.values.get('place')
    if place:
        return render_template('index.html', place=place, weather=weather.get_weather(place))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)