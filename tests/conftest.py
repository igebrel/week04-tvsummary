
"""Shared test fixtures for the TVMaze Summary project."""

import pytest


@pytest.fixture
def sample_records():
    """Provide sample TV show records for testing."""
    return [
        {
            "id": 1,
            "name": "Sample Drama",
            "genres": ["Drama"],
            "language": "English",
            "rating": {"average": 8.5},
        },
        {
            "id": 2,
            "name": "Sample Comedy",
            "genres": ["Comedy"],
            "language": "English",
            "rating": {"average": 7.5},
        },
        {
            "id": 3,
            "name": "Sample Mystery",
            "genres": ["Drama", "Mystery"],
            "language": "French",
            "rating": {"average": 9.0},
        },
    ]
