import os
import time
from typing import Optional, Dict, Any

try:
    import requests
except Exception:
    requests = None

# Simple in-memory cache: city -> (timestamp, data)
_CACHE: Dict[str, Any] = {}
_TTL = 300  # seconds


def _is_fresh(entry_ts: float) -> bool:
    return (time.time() - entry_ts) < _TTL


def get_weather(city: str, api_key: Optional[str] = None, units: str = "metric") -> Dict[str, Any]:
    """Fetch current weather for `city` from OpenWeatherMap and return normalized dict.

    Returns dict with keys: city, temp, description, icon_url
    """
    city = city.strip()
    if not city:
        raise ValueError("City must be provided")

    if city in _CACHE:
        ts, data = _CACHE[city]
        if _is_fresh(ts):
            data = dict(data)
            data["cached"] = True
            return data

    api_key = api_key or os.environ.get("OWM_API_KEY")
    if not api_key:
        raise RuntimeError("OpenWeatherMap API key not set in OWM_API_KEY")

    if requests is None:
        raise RuntimeError("`requests` package is required to call the weather API")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": units}
    resp = requests.get(url, params=params, timeout=10)
    if resp.status_code != 200:
        raise ValueError(f"Weather API error: {resp.status_code} {resp.text}")

    data = resp.json()
    weather = data.get("weather")
    main = data.get("main", {})
    if not weather or not isinstance(weather, list):
        raise ValueError("Malformed weather response")

    w = weather[0]
    icon = w.get("icon")
    icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png" if icon else None

    result = {
        "city": data.get("name", city),
        "temp": main.get("temp"),
        "humidity": main.get("humidity"),
        "description": w.get("description"),
        "icon_url": icon_url,
        "cached": False,
    }

    _CACHE[city] = (time.time(), result)
    return result
