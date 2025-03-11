import argparse
from pubmed_fetcher import fetch_papers, filter_papers, write_csv

def main():
    parser = argparse.ArgumentParser(
        description="Fetch research papers from PubMed and filter by author affiliation."
    )
    parser.add_argument("query", help="PubMed query string")
    parser.add_argument(
        "-f",
        "--file",
        help="Specify the filename to save the results. If not provided, print to console.",
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Print debug information"
    )
    args = parser.parse_args()

    if args.debug:
        print(f"Query: {args.query}")
        print(f"Output file: {args.file}")

    papers = fetch_papers(args.query)
    if papers:
        filtered_papers = filter_papers(papers)
        write_csv(filtered_papers, args.file)

if __name__ == "__main__":
    main()
