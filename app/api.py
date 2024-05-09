import os
import sys

from flask import Flask, jsonify, request, send_file
from flask_swagger_ui import get_swaggerui_blueprint

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.model import find_similar_movies, search, visualize_movie_ratings

app = Flask(__name__)

SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Test application"},
)


@app.route("/")
def home():
    return "Welcome to the Notflix API!"


@app.route("/search", methods=["POST"])
def search_movies():
    if request.method == "POST":
        title = request.get_json().get("title")
        if title:
            results = search(title)
            if results.empty:
                return jsonify({"message": "No movies found"}), 404
            return jsonify(results.to_dict(orient="records")), 200
        else:
            return jsonify({"message": "Title parameter is missing"}), 400


@app.route("/recommendations", methods=["POST"])
def recommend_movies():
    if request.method == "POST":
        movie_id = request.get_json().get("movieId")
        if movie_id:
            results = find_similar_movies(movie_id)
            if results.empty:
                return jsonify({"message": "No recommendations found"}), 404
            return jsonify(results.to_dict(orient="records")), 200
        else:
            return jsonify({"message": "movieId parameter is missing"}), 400


@app.route("/visualize", methods=["POST"])
def visualize_ratings():
    if request.method == "POST":
        movie_id = request.get_json().get("movieId")
        if movie_id:
            img_buffer = visualize_movie_ratings(movie_id)
            if img_buffer:
                return send_file(img_buffer, mimetype="image/png"), 200
            else:
                return jsonify({"message": "Failed to generate visualization"}), 500
        else:
            return jsonify({"message": "movieId parameter is missing"}), 400


if __name__ == "__main__":
    app.register_blueprint(swaggerui_blueprint)
    app.run(debug=True)
