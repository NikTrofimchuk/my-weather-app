from flask import Flask, request, Response, json
import requests
import os

app = Flask(__name__)
API_KEY = os.getenv('WEATHER_API_KEY')

@app.route("/weather")
def get_weather():
    city = request.args.get('city')
    if not city:
        return Response(json.dumps({"error": "No city provided"}, ensure_ascii=False), mimetype='application/json'), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    response = requests.get(url)

    if response.status_code != 200:
        return Response(json.dumps({"error": "City not found"}, ensure_ascii=False), mimetype='application/json'), 404

    data = response.json()
    result = {
        "city": data["name"],
        "description": data["weather"][0]["description"],
        "temperature": data["main"]["temp"]
    }
    return Response(json.dumps(result, ensure_ascii=False), mimetype='application/json')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
