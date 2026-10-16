
"""Parametrized tests for TVMaze records."""

import pytest


@pytest.mark.parametrize(
    "genres, expected_count",
    [
        (["Drama"], 1),
        (["Comedy", "Drama"], 2),
        ([], 0),
        (["Action", "Adventure", "Fantasy"], 3),
    ],
)
def test_genre_list_count(genres, expected_count):
    """Check genre counts using different inputs."""
    assert len(genres) == expected_count
