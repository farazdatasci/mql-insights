import pandas as pd

def clean_data(df):
    df.columns = df.columns.str.strip()
    df = df.fillna("Blank")
    return df