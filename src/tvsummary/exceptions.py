
"""Define custom exceptions for the TVMaze project."""


class TVSummaryError(Exception):
    """Base exception for errors in the TVMaze project."""


class FetchError(TVSummaryError):
    """Raised when TV show records cannot be downloaded."""


class DataValidationError(TVSummaryError):
    """Raised when TV show records contain invalid data."""


class ReportError(TVSummaryError):
    """Raised when the summary report cannot be saved."""
