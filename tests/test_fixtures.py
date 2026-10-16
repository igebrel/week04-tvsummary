
"""Tests for the shared TVMaze sample records fixture."""


def test_sample_records_fixture(sample_records):
    """Check that the shared fixture provides valid sample records."""
    assert len(sample_records) == 3
    assert sample_records[0]["name"] == "Sample Drama"
    assert sample_records[1]["genres"] == ["Comedy"]
    assert sample_records[2]["language"] == "French"
