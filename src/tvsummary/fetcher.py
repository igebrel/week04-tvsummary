"""Download TV show records from the TVMaze API."""

import requests


class TVMazeFetcher:
    """Fetch TV show records from the TVMaze API."""

    def __init__(self, url="https://api.tvmaze.com/shows?page=0"):
        self.url = url

    def fetch_records(self):
        """Download records and return them as a list."""
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.RequestException as error:
            print(f"Unable to download records: {error}")
            return None