import os
import nltk
import syllables
import pandas as pd
from textblob import TextBlob 

# Download the punkt resource
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Create an empty DataFrame with the required columns
output_columns = [
    'URL_ID', 'URL', 'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE',
    'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX', 'AVG NUMBER OF WORDS PER SENTENCE',
    'COMPLEX WORD COUNT', 'WORD COUNT', 'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH'
]

output_df = pd.DataFrame(columns=output_columns)

# Read URLs from Excel file
input_file = "input/Input.xlsx"
df_input = pd.read_excel(input_file)

#------------------------------------#
# define function to perform textual analysis
     
def per_complex_word(blob):
    words = blob.words
    complex_word_count = 0
    total_syllables = 0
    complexity_threshold = 2 
    
    for word in words:
        syllables_count = syllables.estimate(word)
        total_syllables += syllables_count
        if syllables_count > complexity_threshold:
            complex_word_count += 1
            
    percentage_of_complex_words = complex_word_count / len(words) * 100
    return percentage_of_complex_words


def fog_index(blob):
    sentences = blob.sentences
    words = blob.words
    avg_sentence_length = len(text) / len(sentences)
    complex_word_count = 0
    complexity_threshold = 2
    
    for word in words:
        syllables_count = syllables.estimate(word)
        if syllables_count > complexity_threshold:
            complex_word_count += 1
            
    percentage_of_complex_words = complex_word_count / len(words) * 100
    fog_index = 0.4 * (avg_sentence_length + percentage_of_complex_words)
    return fog_index


def complex_word_count(blob):
    words = blob.words
    complex_word_count = 0
    complexity_threshold = 2
    
    for word in words:
        syllables_count = syllables.estimate(word)
        if syllables_count > complexity_threshold:
            complex_word_count += 1
    return complex_word_count


def syllable_per_word(blob):
    words = blob.words
    total_syllables = 0
    
    for word in words:
        syllables_count = syllables.estimate(word)
        total_syllables += syllables_count
    syllable_per_word = total_syllables / len(words)
    return syllable_per_word

def personal_pronoun_ratio(blob):
    tags = blob.tags
    personal_pronouns = []
    personal_pronoun_count = 0

    for word, tag in tags:
        if tag == 'PRP':
            personal_pronouns.append(word)
            personal_pronoun_count += 1
    personal_pronoun_ratio = personal_pronoun_count / len(blob.words)
    return personal_pronoun_ratio

def avg_word_length(blob):
    total_word_length = sum(len(word) for word, _ in blob.tags)
    return total_word_length / len(blob.words)
    
    
#------------------------------------------#
# Loop through URLs and perform text analysis
for index, row in df_input.iterrows():
    url_id = row['URL_ID']
    url = row['URL']

    # Read the extracted text from the corresponding file
    file_path = f"output/{url_id}.txt"
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Perform text analysis using TextBlob
        blob = TextBlob(text)
        positive_score = blob.sentiment.polarity
        negative_score = 1 - positive_score
        polarity_score = blob.sentiment.polarity
        subjectivity_score = blob.sentiment.subjectivity
        sentences = blob.sentences
        word_counts = blob.word_counts
        words = blob.words
        avg_sentence_length = len(text) / len(sentences)
        percentage_of_complex_word = per_complex_word(blob)
        _fog_index = fog_index(blob)
        avg_words_per_sentence = len(words) / len(sentences)
        complex_wrd_count = complex_word_count(blob)
        _syllable_per_word = syllable_per_word(blob)
        personal_pronouns_ratio = personal_pronoun_ratio(blob)
        avrg_wrd_lngth = avg_word_length(blob)
        
        # Append the results to the output DataFrame
        if isinstance(output_df, pd.DataFrame):
            new_data = {
                'URL_ID': url_id,
                'URL': url,
                'POSITIVE SCORE': positive_score,
                'NEGATIVE SCORE': negative_score,
                'POLARITY SCORE': polarity_score,
                'SUBJECTIVITY SCORE': subjectivity_score,
                'AVG SENTENCE LENGTH': avg_sentence_length,
                'PERCENTAGE OF COMPLEX WORDS': percentage_of_complex_word,
                'FOG INDEX': _fog_index,
                'AVG NUMBER OF WORDS PER SENTENCE': avg_words_per_sentence,
                'COMPLEX WORD COUNT': complex_wrd_count,
                'WORD COUNT' : len(words),
                'SYLLABLE PER WORD': _syllable_per_word,
                'PERSONAL PRONOUNS': personal_pronouns_ratio,
                'AVG WORD LENGTH': avrg_wrd_lngth
            }
            output_df = pd.concat([output_df, pd.DataFrame([new_data])], ignore_index=True)
        else:
            print("Namespace Conflict")
    else:
        print(f"File not found for URL_ID {url_id}: {file_path}")


# Save the output DataFrame to Excel
output_file = "output/Output Data Structure.xlsx"
output_df.to_excel(output_file, index=False)

print(f"Output saved to {output_file}")