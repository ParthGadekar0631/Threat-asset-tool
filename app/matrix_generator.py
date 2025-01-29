# matrix_generator.py

import pandas as pd
import numpy as np

def calculate_risk_score(row):
    """
    Calculate risk score based on impact and likelihood.

    :param row: A row of the DataFrame
    :return: Risk score (Impact * Likelihood)
    """
    return row['Impact'] * row['Likelihood']

def generate_threat_asset_matrix(data):
    """
    Generate a threat-asset matrix with risk scores.

    :param data: DataFrame containing Threat, Asset, Impact, and Likelihood columns
    :return: Pivot table (Threat-Asset matrix) with risk scores
    """
    # Add a risk score column
    data['Risk_Score'] = data.apply(calculate_risk_score, axis=1)

    # Create a pivot table
    matrix = data.pivot_table(
        index='Threat',
        columns='Asset',
        values='Risk_Score',
        aggfunc=np.sum,
        fill_value=0
    )

    return matrix

# Example usage
if __name__ == "__main__":
    # Sample data
    sample_data = {
        "Threat": ["Phishing", "Phishing", "Malware", "Ransomware"],
        "Asset": ["Server", "Email", "Workstation", "Database"],
        "Impact": [8, 6, 7, 9],
        "Likelihood": [0.7, 0.8, 0.5, 0.4]
    }

    df = pd.DataFrame(sample_data)
    matrix = generate_threat_asset_matrix(df)
    print("Threat-Asset Matrix:")
    print(matrix)
