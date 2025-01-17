import pandas as pd
import numpy as np
import string
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

def load_dataset(file_path):
    df = pd.read_csv(file_path)
    print("Dataset Loaded Successfully!")
    print("\nDataset Structure:\n", df.info())
    print("\nFirst 5 Rows:\n", df.head())
    return df

def clean_data(df, text_column):
    df = df.dropna(subset=[text_column])
    df = df.drop_duplicates()
    return df

def normalize_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub(r"\d+", "", text)
    return text

def tokenize_text(text):
    return word_tokenize(text)

def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]

def stem_tokens(tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in tokens]

def lemmatize_tokens(tokens):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in tokens]

def vectorize_text(df, text_column):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(df[text_column])
    feature_names = vectorizer.get_feature_names_out()
    vectorized_df = pd.DataFrame(vectors.toarray(), columns=feature_names)
    return vectorized_df

def save_preprocessed_data(df, file_path):
    df.to_csv(file_path, index=False)
    print(f"Preprocessed dataset saved to {file_path}")

def main_workflow():
    file_path = "Amazon_reviews.csv"
    text_column = "review"
    df = load_dataset(file_path)
    df = clean_data(df, text_column)
    df[text_column] = df[text_column].apply(normalize_text)
    df[text_column] = df[text_column].apply(tokenize_text)
    df[text_column] = df[text_column].apply(remove_stopwords)
    df[text_column] = df[text_column].apply(stem_tokens)
    vectorized_df = vectorize_text(df, text_column)
    save_preprocessed_data(vectorized_df, "preprocessed_dataset.csv")

main_workflow()
