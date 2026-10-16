"""Tests for saving TVMaze summary reports."""

import json

from tvsummary.reporter import JSONReporter


def test_save_report_creates_json_file(tmp_path):
    """Check that the reporter saves the correct JSON data."""

    output_file = tmp_path / "test_summary.json"

    summary = {
        "total_shows": 3,
        "genres": {
            "Drama": 2,
            "Comedy": 1,
        },
    }

    reporter = JSONReporter(output_file=output_file)
    reporter.save_report(summary)

    assert output_file.exists()

    with output_file.open("r", encoding="utf-8") as file:
        saved_data = json.load(file)

    assert saved_data == summary