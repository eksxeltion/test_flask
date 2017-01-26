from flask import Flask, render_template, request
import weather

app = Flask(__name__)

@app.route("/")
def index():
	place = request.values.get('place')
	if place:
		return render_template('index.html', place=place, weather=weather.get_weather(place))
	else:
		return render_template('index.html')

if __name__ == "__main__":
    app.run()