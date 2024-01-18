# Data-Extraction-and-NLP
Text Analysis Project
---
Overview
---
This project aims to perform text analysis on a collection of articles extracted from specified URLs. The goal is to compute various variables outlined in the ["Text Analysis.docx"](https://docs.google.com/document/d/1PhMnkBFc1D1U7da3f33QKRQsQhKPfthK/edit?usp=sharing&ouid=116109919028728930152&rtpof=true&sd=true) file, including positive and negative scores, polarity score, subjectivity score, average sentence length, and more.

### Project StructureInput: 
The URLs for the articles are provided in an Excel file [Input.xlsx](https://docs.google.com/spreadsheets/d/1kseE2rYcWFplPgglb79cnGmU8viiRbje/edit?usp=sharing&ouid=116109919028728930152&rtpof=true&sd=true). Each article is associated with a unique URL_ID.

### Data Extraction: 
Python is used, along with the Beautiful Soup library, to crawl the provided URLs and extract article text. The extracted text is saved in text files in the output folder, with the file name being the corresponding URL_ID.

### Text Analysis: 
Text analysis is performed using the TextBlob library in Python. Various variables are computed, such as positive and negative scores, fog index, percentage of complex words, and more. The analysis results are stored in an output Excel file [Output Data Structure.xlsx](https://docs.google.com/spreadsheets/d/1Hm-UipDsn93nuimMx6JZuAkOYAyID9G2/edit?usp=sharing&ouid=116109919028728930152&rtpof=true&sd=true), following the specified format.

---
Project Dependencies

[Python 3.10]
[pandas]
[textblob]
[nltk]
[syllables]

Install the required dependencies using the following:
bash
Copy code
pip install pandas textblob nltk syllables
Usage

Clone the repository:
bash
Copy code
git clone https://github.com/saha-trideep/Data-Extraction-and-NLP.git


cd text-analysis-project

Install dependencies:


bash
Copy code


`pip install -r requirements.txt`

Run the script:


bash
Copy code


`python text_analysis_script.py`

Check the output:

---
The analysis results will be saved in output/Output Data Structure.xlsx.

Contributors
GitHub: saha-trideep

License

This project is licensed under the MIT License.

