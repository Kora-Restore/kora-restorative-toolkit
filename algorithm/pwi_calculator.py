
import pandas as pd

def calculate_pwi_scores(data):
    # Assume input `data` is a dataframe with each historical era and variables:
    # 'Military Intensity', 'Climate Stability', 'Governance Score', 'Inequality Index', 'Social Trust', 'Mental Health Index'

    df = data.copy()

    # 1. Violence Index (Deaths per million per year)
    df["Violence Index (VI)"] = df["Military Intensity"] * 100  # scaled multiplier

    # 2. Wellbeing Score (WS) derived from weighted KPIs
    df["Wellbeing Score (WS)"] = (
        (df["Climate Stability"] * 0.25) +
        ((100 - df["Inequality Index"]) * 0.25) +
        (df["Social Trust"] * 0.25) +
        (df["Mental Health Index"] * 0.25)
    )

    # 3. Governance Score (1-5) – Democracy and civil liberties
    df["Governance Score (1–5)"] = df["Governance Score"]

    # Clip WS for range safety
    df["Wellbeing Score (WS)"] = df["Wellbeing Score (WS)"].clip(lower=0, upper=100)

    return df
