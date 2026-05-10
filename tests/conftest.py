import pytest
from bs4 import BeautifulSoup


class MockResponse:
    def __init__(self, text):
        self.text = text

    def raise_for_status(self):
        pass  # Simulate always OK


@pytest.fixture
def mock_movie_page(monkeypatch):
    mock_html = """
    <html>
        <body>
            <rt-text slot="title" context="heading">Mock Movie Title</rt-text>
            <rt-text slot="critics-score">55%</rt-text>
            <rt-text slot="audience-score">70%</rt-text>

            <rt-text slot="metadata-genre">Action</rt-text>
            <rt-text slot="metadata-genre">Fantasy</rt-text>
            <rt-text slot="metadata-genre">Adventure</rt-text>
        </body>
    </html>
    """
    monkeypatch.setattr("requests.get", MockResponse(mock_html))
    return BeautifulSoup(mock_html, "html.parser")


@pytest.fixture
def mock_movie_page_no_title(monkeypatch):
    mock_html = """
    <html>
        <body>
            <rt-text slot="critics-score">55%</rt-text>
            <rt-text slot="audience-score">70%</rt-text>

            <rt-text slot="metadata-genre">Action</rt-text>
            <rt-text slot="metadata-genre">Fantasy</rt-text>
            <rt-text slot="metadata-genre">Adventure</rt-text>
        </body>
    </html>
    """
    monkeypatch.setattr("requests.get", MockResponse(mock_html))
    return BeautifulSoup(mock_html, "html.parser")


@pytest.fixture
def mock_movie_page_no_audience_score(monkeypatch):
    mock_html = """
    <html>
        <body>
            <rt-text slot="title" context="heading">Mock Movie Title</rt-text>
            <rt-text slot="critics-score">55%</rt-text>

            <rt-text slot="metadata-genre">Action</rt-text>
            <rt-text slot="metadata-genre">Fantasy</rt-text>
            <rt-text slot="metadata-genre">Adventure</rt-text>
        </body>
    </html>
    """
    monkeypatch.setattr("requests.get", MockResponse(mock_html))
    return BeautifulSoup(mock_html, "html.parser")


@pytest.fixture
def mock_movie_page_no_critics_score(monkeypatch):
    mock_html = """
    <html>
        <body>
            <rt-text slot="title" context="heading">Mock Movie Title</rt-text>
            <rt-text slot="audience-score">70%</rt-text>

            <rt-text slot="metadata-genre">Action</rt-text>
            <rt-text slot="metadata-genre">Fantasy</rt-text>
            <rt-text slot="metadata-genre">Adventure</rt-text>
        </body>
    </html>
    """
    monkeypatch.setattr("requests.get", MockResponse(mock_html))
    return BeautifulSoup(mock_html, "html.parser")


@pytest.fixture
def mock_movie_page_no_genres(monkeypatch):
    mock_html = """
    <html>
        <body>
            <rt-text slot="title" context="heading">Mock Movie Title</rt-text>
            <rt-text slot="critics-score">55%</rt-text>
            <rt-text slot="audience-score">70%</rt-text>
        </body>
    </html>
    """
    monkeypatch.setattr("requests.get", MockResponse(mock_html))
    return BeautifulSoup(mock_html, "html.parser")
