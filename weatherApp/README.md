# Flask Weather App

Simple Flask app to look up current weather by city using OpenWeatherMap.

Setup

1. Create an OpenWeatherMap API key and set environment variable `OWM_API_KEY`.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Run

```bash
# Linux / macOS
export OWM_API_KEY=your_key_here
python app.py

# Windows (PowerShell)
$env:OWM_API_KEY = 'your_key_here'
python app.py
```

Open http://127.0.0.1:5000/ and enter a city.