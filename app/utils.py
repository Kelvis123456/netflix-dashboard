import pandas as pd
from collections import Counter

def load_data(path):
    return pd.read_csv(path)

def get_top_directors(df):
    df = df.dropna(subset=["director"])
    return df["director"].value_counts().head(10)

def get_type_counts(df):
    return df["type"].value_counts()

def get_top_categories(df):
    categories = df["listed_in"].dropna().str.split(", ")
    all_categories = [cat for sublist in categories for cat in sublist]
    return Counter(all_categories).most_common(5)