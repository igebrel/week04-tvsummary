
"""Load configuration settings for the TVMaze project."""

import tomllib
from pathlib import Path
from typing import Any


def load_config(config_path: str | Path = "config.toml") -> dict[str, Any]:
    """Read application settings from a TOML configuration file."""
    path = Path(config_path)

    if not path.is_file():
        raise FileNotFoundError(
            f"Configuration file not found: {path}"
        )

    try:
        with path.open("rb") as file:
            config = tomllib.load(file)
    except tomllib.TOMLDecodeError as error:
        raise ValueError(
            f"Invalid TOML configuration: {error}"
        ) from error

    required_sections = ("api", "processing", "report", "logging")

    for section in required_sections:
        if section not in config or not isinstance(config[section], dict):
            raise ValueError(
                f"Missing or invalid configuration section: {section}"
            )

    return config
