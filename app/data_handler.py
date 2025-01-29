import pandas as pd
import json

def parse_csv(file_path):
    """
    Parse a CSV file containing threats and assets.

    :param file_path: Path to the CSV file
    :return: DataFrame containing the data
    """
    try:
        df = pd.read_csv(file_path)
        validate_columns(df.columns)
        return df
    except Exception as e:
        raise ValueError(f"Error parsing CSV file: {e}")

def parse_json(file_path):
    """
    Parse a JSON file containing threats and assets.

    :param file_path: Path to the JSON file
    :return: DataFrame containing the data
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        df = pd.DataFrame(data)
        validate_columns(df.columns)
        return df
    except Exception as e:
        raise ValueError(f"Error parsing JSON file: {e}")

def validate_columns(columns):
    """
    Validate that the required columns are present in the input data.

    :param columns: List of column names
    :raises: ValueError if required columns are missing
    """
    required_columns = {'Threat', 'Asset', 'Impact', 'Likelihood'}
    missing_columns = required_columns - set(columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

def load_data(file_path):
    """
    Load and parse data from a given file.

    :param file_path: Path to the file (CSV or JSON)
    :return: DataFrame containing the data
    """
    if file_path.endswith('.csv'):
        return parse_csv(file_path)
    elif file_path.endswith('.json'):
        return parse_json(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or JSON file.")

# Example usage
if __name__ == "__main__":
    try:
        file_path = "example.csv"  # Replace with your file path
        data = load_data(file_path)
        print(data.head())
    except Exception as e:
        print(e)
