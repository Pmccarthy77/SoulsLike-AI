import requests
from bs4 import BeautifulSoup
import os

def scrape_page(url, output_filename): 
    """
    Scrapes a public webpage and saves visible text
    """

    response = requests.get(url)

    # Check if you successfully retrieved website info
    if response.status_code != 200:
        print(f"Failed to retrieve page! Status code: {response.status_code}")
        return
    
    # takes raw HTML and parses it into a tree structure
    soup = BeautifulSoup(response.text, "html.parser")

    # removes ALL HTML tags i.e <h1> xxx <\h1> -> xxx
    text = soup.get_text(separator="\n")

    # now we ensure the directory we want to send it to exists (prevents crashing)
    os.makedirs("data/raw", exist_ok=True)

    # build the filepath
    output_path = os.path.join("data/raw", output_filename)

    # writes to file. "w" allows overwriting, utf-8 allows special characters
    # using with automatically closes the file and prevents issues
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

        # confirmation print
        print(f"Saved raw page to {output_path}")







