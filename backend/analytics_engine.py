import pandas as pd

def generate_summary(df, field):

    df[field] = df[field].fillna("Blank")

    summary = df[field].value_counts().reset_index()
    summary.columns = [field, "MQLs"]

    return summary