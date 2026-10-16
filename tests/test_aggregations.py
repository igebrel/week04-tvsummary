
from tvsummary.processor import count_genres, average_rating_by_language

def test_count_genres_with_multiple_genres():
    """Check that the program counts different genres correctly."""
    records = [
        {"genres": ["Drama", "Comedy"]},
        {"genres": ["Drama"]},
        {"genres": ["Action", "Comedy"]},
    ]

    result = count_genres(records)

    assert result == {
        "Drama": 2,
        "Comedy": 2,
        "Action": 1,
    }


def test_count_genres_with_empty_records():
    """Check that an empty list returns an empty dictionary."""
    records = []

    result = count_genres(records)

    assert result == {}


def test_count_genres_with_missing_genres():
    """Check that missing genre information does not cause an error."""
    records = [
        {"name": "Show A"},
        {"genres": None},
        {"genres": ["Drama"]},
    ]

    result = count_genres(records)

    assert result == {"Drama": 1}

def test_average_rating_by_language():
    """Check that average ratings are calculated correctly."""
    records = [
        {"language": "English", "rating": {"average": 8.0}},
        {"language": "English", "rating": {"average": 6.0}},
        {"language": "French", "rating": {"average": 9.0}},
    ]

    result = average_rating_by_language(records)

    assert result == {
        "English": 7.0,
        "French": 9.0,
    }

def test_average_rating_with_missing_values():
    """Check that missing ratings are ignored."""
    records = [
        {"language": "English", "rating": {"average": 8.0}},
        {"language": "English", "rating": {"average": None}},
        {"language": "English", "rating": None},
        {"language": "French", "rating": {"average": 6.0}},
    ]

    result = average_rating_by_language(records)

    assert result == {
        "English": 8.0,
        "French": 6.0,
    }