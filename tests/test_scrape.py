import pytest

from wallace.scrape import (
    MovieScrapeError,
    get_movie_audience_score,
    get_movie_critics_score,
    get_movie_genres,
    get_movie_title,
    get_movie_url,
)


@pytest.mark.parametrize(
    "movie_title, expected_url",
    [
        ("Mortal Kombat II", "https://www.rottentomatoes.com/m/mortal_kombat_ii"),
        (
            "The Lord of the Rings: The Return of the King",
            "https://www.rottentomatoes.com/m/the_lord_of_the_rings_the_return_of_the_king",
        ),
        ("Inception", "https://www.rottentomatoes.com/m/inception"),
        (
            "Ready or Not 2: Here I Come",
            "https://www.rottentomatoes.com/m/ready_or_not_2_here_i_come",
        ),
    ],
)
def test_get_movie_url(movie_title, expected_url):
    assert get_movie_url(movie_title) == expected_url


def test_get_movie_title_success(mock_movie_page):
    assert get_movie_title(mock_movie_page) == "Mock Movie Title"


def test_get_movie_title_not_found(mock_movie_page_no_title):
    with pytest.raises(MovieScrapeError, match="Movie title not found on the page."):
        get_movie_title(mock_movie_page_no_title)


def test_get_movie_audience_score_success(mock_movie_page):
    assert get_movie_audience_score(mock_movie_page) == "70%"


def test_get_movie_audience_score_not_found(mock_movie_page_no_audience_score):
    with pytest.raises(MovieScrapeError, match="Audience score not found on the page."):
        get_movie_audience_score(mock_movie_page_no_audience_score)


def test_get_movie_critics_score_success(mock_movie_page):
    assert get_movie_critics_score(mock_movie_page) == "55%"


def test_get_movie_critics_score_not_found(mock_movie_page_no_critics_score):
    with pytest.raises(MovieScrapeError, match="Critics score not found on the page."):
        get_movie_critics_score(mock_movie_page_no_critics_score)


def test_get_movie_genres_success(mock_movie_page):
    assert get_movie_genres(mock_movie_page) == ["Action", "Fantasy", "Adventure"]


def test_get_movie_genres_not_found(mock_movie_page_no_genres):
    with pytest.raises(MovieScrapeError, match="Genres not found on the page."):
        get_movie_genres(mock_movie_page_no_genres)
