import pandas as pd

def smart_insights(df, field):

    insights = []

    top = df[field].value_counts().idxmax()
    insights.append(f"Top MQL Source: {top}")

    counts = df[field].value_counts()
    worst = counts.idxmin()
    insights.append(f"Worst Performing: {worst}")

    blank_pct = (df[field].isna().sum() / len(df)) * 100
    insights.append(f"Blank Data: {blank_pct:.2f}%")

    return insights


def monthly_trend(df):

    if "Date" not in df.columns:
        return None

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    trend = df.groupby(df["Date"].dt.to_period("M")).size()

    return trend