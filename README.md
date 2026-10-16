# Week 04 - TVMaze Summary Project

## Overview

This project builds on my Week 03 TVMaze Summary Project. It downloads TV show records from the TVMaze public API, processes the information, and creates a summary in JSON format.

For Lab 04, I added a TV show data model and automated tests to check that the program works correctly. I also used Ruff and Mypy to check the quality of my Python code.

## Project Files

- `src/tvsummary/fetcher.py` - Downloads TV show records from the TVMaze API.
- `src/tvsummary/models.py` - Defines the TVShow data model.
- `src/tvsummary/processor.py` - Calculates summary information about the TV shows.
- `src/tvsummary/reporter.py` - Saves the summary as a JSON file.
- `src/tvsummary/main.py` - Runs the complete program.
- `tests/test_aggregations.py` - Tests the aggregation functions.
- `tests/test_models.py` - Tests the TVShow data model.
- `tests/test_fetcher.py` - Tests successful downloads and API errors.
- `tests/test_main.py` - Tests the main program.
- `environment.yml` - Defines the Conda environment.
- `pyproject.toml` - Contains the project configuration.
- `requirements.txt` - Lists the Python package dependencies.
- `README.md` - Explains the project.

## Requirements

- Python 3.11
- requests
- pytest
- Ruff
- Mypy

## Installation

I used Anaconda and Visual Studio Code to complete this project.

To create the Conda environment, run:

```bash
conda env create -f environment.yml
```

To install the project in the environment, run:

```bash
conda run -n tvsummary-lab04 python -m pip install -e .
```

The testing and code-quality tools must also be installed in the environment.

## How to Run

Run the program using:

```bash
conda run -n tvsummary-lab04 python -m tvsummary.main
```

The program downloads TV show records, processes the data, and saves a summary in JSON format.

## Automated Testing

I used pytest to test different parts of my project, including data processing, the TVShow model, API error handling, and the main program.

To run all tests, use:

```bash
conda run -n tvsummary-lab04 python -m pytest -v
```

During development, I ran 15 automated tests, and all 15 passed.

## Code Quality

I used Ruff to check for formatting and common code-quality problems.

```bash
conda run -n tvsummary-lab04 python -m ruff check src tests
```

I also used Mypy to check for potential type-related issues.

```bash
conda run -n tvsummary-lab04 python -m mypy src
```

Both checks passed during development.

## Data Quirks

Some TVMaze records may have missing languages, genres, ratings, or premiere dates. The program checks for missing values when calculating the summary.

The TVShow model also provides default values for missing information.

## Design Choices

I divided the program into separate modules to make it easier to understand and test.

I used a dataclass to represent a TV show and dictionaries, lists, and sets to process the records. I used pytest to check the results and monkeypatch to simulate API responses without making real internet requests during testing.

## Known Limitations

The program requires an internet connection to download current records from the TVMaze API. If the API is unavailable, the program cannot download new records.

The quality of the summary also depends on the information provided by TVMaze.

## Acknowledgement

I used ChatGPT for guidance with Python, automated testing, Git, and project documentation. I reviewed the code, ran the tests, and checked the results while completing this lab.