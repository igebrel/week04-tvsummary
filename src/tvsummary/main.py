"""Run the TVMaze records processing project."""

from tvsummary.fetcher import TVMazeFetcher
from tvsummary.processor import build_summary
from tvsummary.reporter import JSONReporter


def main():
    """Download TV show records and save their summary."""
    fetcher = TVMazeFetcher()
    records = fetcher.fetch_records()

    if records is None:
        print("Unable to process records.")
        return

    if len(records) < 50:
        print("Not enough records to process.")
        return

    summary = build_summary(records)

    reporter = JSONReporter()
    reporter.save_report(summary)

    print(f"Processed {len(records)} TV show records.")


if __name__ == "__main__":
    main()