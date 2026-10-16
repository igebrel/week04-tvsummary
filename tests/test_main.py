
"""Test the main TVMaze processing workflow."""

import tvsummary.main as main_module


def test_main_success(monkeypatch, capsys):
    """Check that valid records are processed and saved."""
    records = [{"name": f"Show {i}"} for i in range(50)]
    saved_reports = []

    monkeypatch.setattr(
        main_module.TVMazeFetcher,
        "fetch_records",
        lambda self: records,
    )
    monkeypatch.setattr(
        main_module.JSONReporter,
        "save_report",
        lambda self, summary: saved_reports.append(summary),
    )

    main_module.main()

    assert len(saved_reports) == 1
    assert saved_reports[0]["records_processed"] == 50
    assert "Processed 50 TV show records." in capsys.readouterr().out


def test_main_download_failure(monkeypatch, capsys):
    """Check that the program stops when downloading fails."""
    monkeypatch.setattr(
        main_module.TVMazeFetcher,
        "fetch_records",
        lambda self: None,
    )

    main_module.main()

    assert "Unable to process records." in capsys.readouterr().out


def test_main_insufficient_records(monkeypatch, capsys):
    """Check that fewer than 50 records are rejected."""
    records = [{"name": "Example Show"}]

    monkeypatch.setattr(
        main_module.TVMazeFetcher,
        "fetch_records",
        lambda self: records,
    )

    main_module.main()

    assert "Not enough records to process." in capsys.readouterr().out
