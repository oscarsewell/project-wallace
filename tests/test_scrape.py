import pytest

from wallace.scrape import get_movie_url


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
