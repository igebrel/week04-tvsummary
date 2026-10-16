
"""Run the TVMaze records processing project."""

import logging

from tvsummary.exceptions import FetchError
from tvsummary.fetcher import TVMazeFetcher
from tvsummary.processor import build_summary
from tvsummary.reporter import JSONReporter

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)


def main():
    """Download TV show records and save their summary."""
    logger.info("Starting TVMaze records processing.")

    fetcher = TVMazeFetcher()

    try:
        records = fetcher.fetch_records()
        logger.info("Successfully downloaded TV show records.")
    except FetchError as error:
        logger.error("Unable to process records: %s", error)
        print(f"Unable to process records: {error}")
        return

    if records is None:
        logger.error("No records were returned.")
        print("Unable to process records.")
        return

    if len(records) < 50:
        logger.warning(
            "Not enough records to process. Found %d records.",
            len(records),
        )
        print("Not enough records to process.")
        return

    logger.info("Processing %d TV show records.", len(records))

    summary = build_summary(records)
    logger.info("TV show summary generated successfully.")

    reporter = JSONReporter()
    reporter.save_report(summary)

    logger.info("JSON summary report saved successfully.")

    print(f"Processed {len(records)} TV show records.")


if __name__ == "__main__":
    main()
