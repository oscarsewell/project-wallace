import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.rottentomatoes.com/m/"


def get_movie_url(movie_name: str) -> str:
    """Converts a movie name into its corresponding Rotten Tomatoes URL."""
    formatted_name = movie_name.lower().replace(" ", "_")
    return f"{BASE_URL}{formatted_name}"


def get_movie_page(movie_name: str) -> BeautifulSoup:
    """Fetches the HTML content of the movie's Rotten Tomatoes page."""
    movie_url = get_movie_url(movie_name)
    response = requests.get(movie_url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def get_movie_title(soup: BeautifulSoup) -> str:
    """Extracts the movie title from the page's HTML."""
    return soup.find("rt-text", slot="title", context="heading").text.strip()


def get_movie_scores(soup: BeautifulSoup) -> dict:
    """Extracts the critics and audience scores from the movie's Rotten Tomatoes page."""
    ratings = {}

    critics_score = soup.find("rt-text", slot="critics-score")
    if critics_score:
        ratings["critics_score"] = critics_score.text.strip()

    audience_score = soup.find("rt-text", slot="audience-score")
    if audience_score:
        ratings["audience_score"] = audience_score.text.strip()

    return ratings


def get_movie_genres(soup: BeautifulSoup) -> list:
    """Extracts the genres of the movie from the page's HTML."""
    genre_elements = soup.find_all("rt-text", slot="metadata-genre")
    return [genre.text.strip() for genre in genre_elements]


if __name__ == "__main__":
    movie_name = "Mortal Kombat II"
    movie_page = get_movie_page(movie_name)
    title = get_movie_title(movie_page)
    scores = get_movie_scores(movie_page)
    genres = get_movie_genres(movie_page)
    print(f"Title: {title}")
    print(f"Critics Score: {scores.get('critics_score', 'N/A')}")
    print(f"Audience Score: {scores.get('audience_score', 'N/A')}")
    print(f"Genres: {', '.join(genres)}")
