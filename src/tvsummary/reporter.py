
import json
from pathlib import Path


class JSONReporter:
    """Save the TV show summary to a JSON file."""

    def __init__(self, output_file="summary.json"):
        self.output_file = Path(output_file)

    def save_report(self, summary):
        """Write the summary to a JSON file."""
        with self.output_file.open("w", encoding="utf-8") as file:
            json.dump(summary, file, indent=2, ensure_ascii=False)

        print(f"Summary saved to {self.output_file}")
