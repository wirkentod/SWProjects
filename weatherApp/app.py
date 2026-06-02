import os
from flask import Flask, app, render_template, request, redirect, url_for, flash

from weather.api import get_weather


def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("FLASK_SECRET", "dev-secret")

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    @app.route("/weather", methods=["GET", "POST"])
    def weather():
        if request.method == "POST":
            city = request.form.get("city", "").strip()
            return redirect(url_for("weather", city=city))

        city = request.args.get("city", "").strip()
        if not city:
            flash("Please enter a city name.")
            return redirect(url_for("index"))

        try:
            result = get_weather(city)
        except Exception as e:
            return render_template("weather.html", error=str(e), city=city)

        return render_template("weather.html", **result)

    @app.route("/example", methods=["GET"])
    def redirex():
        return render_template("base.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=True)
