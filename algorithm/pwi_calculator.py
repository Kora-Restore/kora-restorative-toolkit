
import pandas as pd

def calculate_pwi(file_path):
    # Load dataset
    df = pd.read_csv(file_path)

    # Calculate Violence Index (VI)
    df["VI"] = df["Conflicts_per_century"] * df["Deaths_per_conflict"]

    # Calculate Sustainable & Equitable Wellbeing Index (SEWI)
    df["SEWI"] = (df["BHW"] + df["EF"] + df["ES"]) / 3

    # Calculate Peace & Wellbeing Index (PWI)
    df["PWI"] = df["SEWI"] / df["VI"]

    # Sort by PWI
    df_sorted = df.sort_values(by="PWI", ascending=False)

    return df_sorted

# Example usage:
# result = calculate_pwi("ancient.csv")
# print(result)
