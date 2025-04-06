
import pandas as pd

def analyze_competitors(csv_path):
    df = pd.read_csv(csv_path)
    print("== Competitor Summary ==")
    for idx, row in df.iterrows():
        print(f"Brand: {row['Brand']} | USP: {row['USP']}")
