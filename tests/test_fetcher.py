
"""Test downloading TV show records from the TVMaze API."""

import pytest
import requests

from tvsummary.exceptions import FetchError
from tvsummary.fetcher import TVMazeFetcher


def test_fetch_records_success(monkeypatch):
    """Check that a successful API request returns records."""

    sample_records = [
        {"name": "Show One"},
        {"name": "Show Two"},
    ]

    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return sample_records

    def fake_get(url, timeout):
        assert url == "https://api.tvmaze.com/shows?page=0"
        assert timeout == 10
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)

    fetcher = TVMazeFetcher()
    result = fetcher.fetch_records()

    assert result == sample_records
    assert len(result) == 2


def test_fetch_records_connection_error(monkeypatch):
    """Check that connection errors raise FetchError."""

    def fake_get(url, timeout):
        raise requests.ConnectionError("Connection failed")

    monkeypatch.setattr(requests, "get", fake_get)

    fetcher = TVMazeFetcher()

    with pytest.raises(FetchError, match="Connection failed"):
        fetcher.fetch_records()


def test_fetch_records_http_error(monkeypatch):
    """Check that HTTP errors raise FetchError."""

    class FakeResponse:
        def raise_for_status(self):
            raise requests.HTTPError("500 Server Error")

    def fake_get(url, timeout):
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)

    fetcher = TVMazeFetcher()

    with pytest.raises(FetchError, match="500 Server Error"):
        fetcher.fetch_records()
