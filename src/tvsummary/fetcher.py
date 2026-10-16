
"""Download TV show records from the TVMaze API."""

import requests

from tvsummary.config import load_config
from tvsummary.exceptions import FetchError


class TVMazeFetcher:
    """Fetch TV show records from the TVMaze API."""

    def __init__(self, url=None, timeout=None):
        """Initialize the fetcher using configuration settings."""
        config = load_config()

        base_url = config["api"]["base_url"]

        self.url = url if url is not None else f"{base_url}?page=0"
        self.timeout = (
            timeout if timeout is not None else config["api"]["timeout"]
        )

    def fetch_records(self):
        """Download records and return them as a list."""
        try:
            response = requests.get(self.url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()

        except requests.RequestException as error:
            raise FetchError(
                f"Unable to download TV show records: {error}"
            ) from error
