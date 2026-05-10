from flask import Flask, jsonify, request
from requests.exceptions import HTTPError

from wallace.scrape import (
    MovieScrapeError,
    get_movie_audience_score,
    get_movie_critics_score,
    get_movie_genres,
    get_movie_page,
    get_movie_title,
)

app = Flask(__name__)


@app.route("/movie", methods=["GET"])
def movie_info():
    movie_name = request.args.get("name")
    if not movie_name:
        return jsonify({"error": "Movie name is required."}), 400

    try:
        soup = get_movie_page(movie_name)
        return jsonify(
            {
                "title": get_movie_title(soup),
                "audience_score": get_movie_audience_score(soup),
                "critics_score": get_movie_critics_score(soup),
                "genres": get_movie_genres(soup),
            }
        )
    except HTTPError:
        return jsonify({"error": f"Movie not found: {movie_name}"}), 404
    except MovieScrapeError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
