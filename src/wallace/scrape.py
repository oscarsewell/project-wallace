import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.rottentomatoes.com/m/"


class MovieScrapeError(Exception):
    """Custom exception for movie scraping errors."""

    pass


def get_movie_url(movie_name: str) -> str:
    """Converts a movie name into its corresponding Rotten Tomatoes URL."""
    formatted_name = (
        movie_name.lower().replace(" ", "_").replace(":", "").replace("'", "")
    )
    return f"{BASE_URL}{formatted_name}"


def get_movie_page(movie_name: str) -> BeautifulSoup:
    """Fetches the HTML content of the movie's Rotten Tomatoes page."""
    movie_url = get_movie_url(movie_name)
    response = requests.get(movie_url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def get_movie_title(soup: BeautifulSoup) -> str:
    """Extracts the movie title from the page's HTML."""
    title = soup.find("rt-text", slot="title", context="heading")
    if not title or not title.text.strip():
        raise MovieScrapeError("Movie title not found on the page.")
    return title.text.strip()


def get_movie_audience_score(soup: BeautifulSoup) -> str:
    """Extracts the audience score from the page's HTML."""
    audience_score = soup.find("rt-text", slot="audience-score")
    if not audience_score or not audience_score.text.strip():
        raise MovieScrapeError("Audience score not found on the page.")
    return audience_score.text.strip()


def get_movie_critics_score(soup: BeautifulSoup) -> str:
    """Extracts the critics score from the page's HTML."""
    critics_score = soup.find("rt-text", slot="critics-score")
    if not critics_score or not critics_score.text.strip():
        raise MovieScrapeError("Critics score not found on the page.")
    return critics_score.text.strip()


def get_movie_genres(soup: BeautifulSoup) -> list:
    """Extracts the genres of the movie from the page's HTML."""
    genre_elements = soup.find_all("rt-text", slot="metadata-genre")
    if not genre_elements or not any(genre.text.strip() for genre in genre_elements):
        raise MovieScrapeError("Genres not found on the page.")
    return [genre.text.strip() for genre in genre_elements]


def get_movie_director(soup: BeautifulSoup) -> str | None:
    """Extracts the director of the movie from the page's HTML."""
    ...


def get_movie_cast(soup: BeautifulSoup) -> list | None:
    """Extracts the cast of the movie from the page's HTML."""
    ...


def get_movie_release_date(soup: BeautifulSoup) -> str | None:
    """Extracts the release date of the movie from the page's HTML."""
    ...


def get_movie_runtime(soup: BeautifulSoup) -> str | None:
    """Extracts the runtime of the movie from the page's HTML."""
    ...
