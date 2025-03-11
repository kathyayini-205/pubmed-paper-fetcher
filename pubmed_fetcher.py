from Bio import Entrez
import csv
from typing import List, Dict

Entrez.email = "your.email@example.com"  # Replace with your email

def fetch_papers(query: str) -> List[Dict]:
    """
    Fetches research papers from PubMed based on the given query.

    Args:
        query: The PubMed query string.

    Returns:
        A list of dictionaries, where each dictionary represents a paper.
    """
    try:
        handle = Entrez.esearch(db="pubmed", term=query, retmax="100")  # Adjust retmax as needed
        record = Entrez.read(handle)
        paper_ids = record["IdList"]

        papers =
        for paper_id in paper_ids:
            paper_details = fetch_paper_details(paper_id)
            if paper_details:
                papers.append(paper_details)
        return papers

    except Exception as e:
        print(f"Error fetching papers: {e}")
        return

def fetch_paper_details(paper_id: str) -> Dict:
    """
    Fetches details for a specific paper from PubMed.

    Args:
        paper_id: The PubMed ID of the paper.

    Returns:
        A dictionary containing the paper's details, or None if an error occurs.
    """
    try:
        handle = Entrez.efetch(db="pubmed", id=paper_id, rettype="medline", retmode="text")
        record = handle.read()
        #   Parse the record (this part requires more detailed parsing logic
        #   using regular expressions or a dedicated parser for Medline format)
        #   Extract: Title, Publication Date, Authors, Affiliations, Corresponding Author Email
        #   The below is a placeholder - you'll need to implement the parsing
        details = {
            "PubmedID": paper_id,
            "Title": "To be extracted",
            "Publication Date": "To be extracted",
            "Authors":,
            "Non-academic Author(s)": "To be determined",
            "Company Affiliation(s)": "To be determined",
            "Corresponding Author Email": "To be extracted",
        }
        return details

    except Exception as e:
        print(f"Error fetching paper details for {paper_id}: {e}")
        return None

def is_non_academic_author(affiliation: str) -> bool:
    """
    Checks if an author's affiliation indicates a non-academic institution.

    Args:
        affiliation: The author's affiliation string.

    Returns:
        True if the affiliation suggests a non-academic institution, False otherwise.
    """
    non_academic_keywords = ["pharmaceutical", "biotech", "company"]
    affiliation = affiliation.lower()
    return any(keyword in affiliation for keyword in non_academic_keywords)

def filter_papers(papers: List[Dict]) -> List[Dict]:
    """
    Filters the list of papers to include only those with at least one
    non-academic author.

    Args:
        papers: A list of dictionaries, where each dictionary represents a paper.

    Returns:
        A filtered list of dictionaries.
    """
    filtered_papers =
    for paper in papers:
        non_academic_authors =
        for author in paper.get("Authors",):
            if is_non_academic_author(author.get("Affiliation", "")):
                non_academic_authors.append(author["Name"])  # Assuming "Name" is the key
        if non_academic_authors:
            paper["Non-academic Author(s)"] = ", ".join(non_academic_authors)
            #   You'll need to extract company affiliations more precisely here
            paper["Company Affiliation(s)"] = "To be extracted"
            filtered_papers.append(paper)
    return filtered_papers

def write_csv(papers: List[Dict], filename: str = None) -> None:
    """
    Writes the list of papers to a CSV file or prints to the console.

    Args:
        papers: A list of dictionaries, where each dictionary represents a paper.
        filename: The name of the CSV file to write to. If None, prints to the console.
    """
    fieldnames = [
        "PubmedID",
        "Title",
        "Publication Date",
        "Non-academic Author(s)",
        "Company Affiliation(s)",
        "Corresponding Author Email",
    ]
    if filename:
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for paper in papers:
                writer.writerow(paper)
    else:
        writer = csv.DictWriter(None, fieldnames=fieldnames)
        writer.writeheader()
        for paper in papers:
            writer.writerow(paper)
        print(writer.getvalue())
