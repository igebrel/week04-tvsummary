
"""Define a simple model for a TV show record."""

from dataclasses import dataclass, field


@dataclass
class TVShow:
    """Store the main information about a TV show."""

    name: str
    language: str = "Unknown"
    genres: list[str] = field(default_factory=list)
    rating: float | None = None
    premiered: str | None = None

    @classmethod
    def from_dict(cls, data: dict) -> "TVShow":
        """Create a TVShow object from TVMaze API data."""
        return cls(
            name=data.get("name") or "Unknown",
            language=data.get("language") or "Unknown",
            genres=data.get("genres") or [],
            rating=(data.get("rating") or {}).get("average"),
            premiered=data.get("premiered"),
        )
