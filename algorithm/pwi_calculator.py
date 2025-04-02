import pandas as pd

def calculate_pwi(file_path):
    """
    Loads a dataset, computes Violence Index (VI), Sustainable & Equitable Wellbeing Index (SEWI),
    and the final Peace & Wellbeing Index (PWI) for each civilization.
    """

    # Load the CSV file
    df = pd.read_csv(file_path)

    # Calculate Violence Index (VI)
    df["VI"] = df["Conflicts_per_century"] * df["Deaths_per_conflict"]

    # Calculate Sustainable & Equitable Wellbeing Index (SEWI)
    df["SEWI"] = (df["BHW"] + df["EF"] + df["ES"]) / 3

    # Calculate Peace & Wellbeing Index (PWI)
    df["PWI"] = df["SEWI"] / df["VI"]

    # Sort results by PWI (highest first)
    df_sorted = df.sort_values(by="PWI", ascending=False)

    return df_sorted


# Example usage:
if __name__ == "__main__":
    file_path = "data/ancient.csv"  # Change to any other file you add later
    results = calculate_pwi(file_path)
    print("\nPeace & Wellbeing Index (PWI) Results:\n")
    print(results[["Civilization", "PWI", "SEWI", "VI"]])
