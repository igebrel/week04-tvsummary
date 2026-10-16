# Week 03 - TVMaze Summary Project
## Overview

This project downloads TV show records from the TVMaze API and processes the returned data using Python. The program organizes the records and creates an aggregated summary in JSON format.

## Files
- `src/tvsummary/fetcher.py` - Downloads TV show records from the TVMaze API.
- `src/tvsummary/processor.py` - Processes the records and creates the summary.
- `src/tvsummary/reporter.py` - Saves the summary to a JSON file.
- `src/tvsummary/main.py` - Runs the project using the other modules.
- `summary.json` - Contains the summary results.
- `pyproject.toml` - Contains the project configuration.
- `requirements.txt` - Lists the required Python packages.
- `.gitignore` - Lists files and folders that Git should ignore.

## Requirements

- Python 3.11 or later
- requests

## Installation


I used a Conda environment to run this project.

To create the environment, run:

```bash
conda env create -f environment.yml
```

To activate the environment, run:

```bash
conda activate tvsummary
```

To install the project, run:

```bash
pip install -e .
```

## How to Run

Run the program from the terminal:

```bash
conda run -n tvsummary python -m tvsummary.main
```

## Output

The program prints the number of processed TV show records and creates `summary.json` containing the aggregated results.

## Acknowledgement

I used ChatGPT for guidance when I had questions about setting up the project, using Git, and checking my work. I reviewed the code and tested the program before completing the project.

## Data Quirks

The TVMaze API may contain missing or incomplete values for some TV shows. For example, some records may not include a language, genre, or rating. The program checks these values before processing the records so that missing data does not cause the program to fail.

## Design Choices

I used different Python collections to organize the data. I used a dictionary to group the TV shows by genre, a set to keep the unique languages, and a list to store the records. I also used a comprehension when processing the data. I chose these collections because they made it easier for me to organize and summarize the TV show records.

## Known Limitations

The program depends on the TVMaze API, so it needs an internet connection to download the records. If the API is unavailable, the program cannot get the data. The results also depend on the information provided by the TVMaze API.
