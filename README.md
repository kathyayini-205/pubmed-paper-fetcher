# pubmed-paper-fetcher

This Python program fetches research papers from PubMed based on a user-specified query, filters them to include only papers with at least one author affiliated with a pharmaceutical or biotech company, and outputs the results as a CSV file.

## Code Organization

The code is organized into two main parts:

* `pubmed_fetcher.py`: This module contains the core logic for interacting with the PubMed API, fetching paper details, filtering authors, and writing the results to a CSV file.
* `get-papers-list.py`: This script provides the command-line interface for the program, allowing users to specify the query and output options.

## Installation and Execution

1.  **Install Poetry:**
    ```bash
    pip install poetry
    ```
2.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
3.  **Install dependencies:**
    ```bash
    poetry install
    ```
4.  **Run the program:**
    ```bash
    poetry run get-papers-list <query> [-f <filename.csv>] [-d]
    ```
    * `<query>`: The PubMed query string (e.g., "cancer therapy").
    * `-f <filename.csv>`:  Optional. Specifies the output CSV filename.
    * `-d`: Optional. Enables debug mode.

## Tools and Libraries

* [Biopython](https://biopython.org/): Used for interacting with the PubMed API.
* [Poetry](https://python-poetry.org/): Used for dependency management and packaging.
* Python's built-in `csv` module: Used for CSV file handling.
* Python's built-in `argparse` module: Used for command-line argument parsing.

## Notes

* Remember to replace `"your.email@example.com"` in `pubmed_fetcher.py` with your email address.
* The Medline record parsing in `fetch_paper_details()` needs to be implemented.
* The author affiliation filtering heuristics may need further refinement.
