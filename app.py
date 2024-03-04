from flask import Flask, render_template, request
from weather_fetcher import fetch_weather_data

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def submit_form():
    city_name = None
    data = None

    if request.method == 'POST':
        city_name = request.form.get('city_name')
        if city_name != '':
            data = fetch_weather_data(city_name)

    return render_template('index.html', city_name=city_name, data=data)


if __name__ == '__main__':
    app.run(debug=True)
