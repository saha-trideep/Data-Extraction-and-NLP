import os
import requests
from bs4 import BeautifulSoup
import pandas as pd


# Read URLs from Excel file
input_file = "input/Input.xlsx"
df = pd.read_excel(input_file)

# Create the 'output' directory if it doesn't exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Loop through URLs and extract article text
for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']

    # Send a GET request and get the response
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the element that contains the article title
        title_element = soup.find("h1", class_="entry-title")
        title = title_element.text if title_element else "Title not found"

        # Find the element that contains the article text
        text_element = soup.find("div", class_="td-post-content tagdiv-type")
        text = text_element.text if text_element else "Text not found"

        # Save the extracted text to a file
        output_file = f"output/{url_id}.txt"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"{title}\n\n{text}")

        print(f"Extraction completed for {url}")
    else:
        print(f"Failed to retrieve content from {url}. Status Code: {response.status_code}")