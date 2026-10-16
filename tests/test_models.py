
"""Test the TVShow model using pytest."""

from tvsummary.models import TVShow


def test_tvshow_with_complete_data():
    """Check that all TV show details are stored correctly."""
    data = {
        "name": "Example Show",
        "language": "English",
        "genres": ["Drama", "Comedy"],
        "rating": {"average": 8.5},
        "premiered": "2020-05-10",
    }

    show = TVShow.from_dict(data)

    assert show.name == "Example Show"
    assert show.language == "English"
    assert show.genres == ["Drama", "Comedy"]
    assert show.rating == 8.5
    assert show.premiered == "2020-05-10"


def test_tvshow_with_missing_data():
    """Check that missing values use safe defaults."""
    show = TVShow.from_dict({})

    assert show.name == "Unknown"
    assert show.language == "Unknown"
    assert show.genres == []
    assert show.rating is None
    assert show.premiered is None


def test_tvshow_with_null_values():
    """Check that None values are handled correctly."""
    data = {
        "name": None,
        "language": None,
        "genres": None,
        "rating": None,
        "premiered": None,
    }

    show = TVShow.from_dict(data)

    assert show.name == "Unknown"
    assert show.language == "Unknown"
    assert show.genres == []
    assert show.rating is None
    assert show.premiered is None


def test_tvshow_genres_are_independent():
    """Check that TV shows do not share the same genre list."""
    first_show = TVShow(name="First Show")
    second_show = TVShow(name="Second Show")

    first_show.genres.append("Drama")

    assert first_show.genres == ["Drama"]
    assert second_show.genres == []
