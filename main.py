import pandas as pd
import numpy as np
import sys

def load_data(file_path):
    """Load data from a CSV or Excel file."""
    if file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    elif file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    else:
        raise ValueError("File must be in .csv or .xlsx format.")

def validate_arguments(file_path, priority_weights, benefit_impacts, output_path):
    """Validate inputs and check for consistency."""
    if len(sys.argv) != 5:
        raise ValueError("Usage: <script.py> <InputFile> <Weights> <Impacts> <OutputFile>")

    try:
        # Load the input data
        data = load_data(file_path)

        # Ensure there are at least three columns
        if len(data.columns) < 3:
            raise ValueError("The input file must contain at least three columns.")

        # Convert weights and impacts to appropriate formats
        priority_weights = [float(w) for w in priority_weights.split(',')]
        benefit_impacts = benefit_impacts.split(',')

        # Ensure numeric columns contain valid numbers
        for column in data.columns[1:]:
            if not pd.to_numeric(data[column], errors='coerce').notnull().all():
                raise ValueError(f"Column '{column}' contains non-numeric values.")

        # Check that weights match the number of criteria columns
        if len(priority_weights) != len(data.columns[1:]):
            raise ValueError("The number of weights must match the number of criteria columns.")

        # Check that impacts match the number of criteria columns
        if len(benefit_impacts) != len(data.columns[1:]):
            raise ValueError("The number of impacts must match the number of criteria columns.")

        # Validate that impacts are either '+' or '-'
        if not all(impact in ['+', '-'] for impact in benefit_impacts):
            raise ValueError("Impacts must be '+' for benefit or '-' for cost.")

    except FileNotFoundError:
        raise FileNotFoundError("Input file not found.")
    except Exception as error:
        raise Exception(f"Error validating inputs: {str(error)}")

    return data, priority_weights, benefit_impacts

def compute_topsis(data, weights, impacts):
    """Calculate TOPSIS scores and rankings."""
    # Extract numerical data
    numerical_data = data.iloc[:, 1:].values.astype(float)

    # Step 1: Normalize the decision matrix
    normalization_factor = np.sqrt(np.sum(numerical_data**2, axis=0))
    normalized_data = numerical_data / normalization_factor

    # Step 2: Calculate the weighted normalized matrix
    weighted_data = normalized_data * np.array(weights)

    # Step 3: Identify ideal best and worst values
    ideal_best = np.zeros(len(data.columns) - 1)
    ideal_worst = np.zeros(len(data.columns) - 1)

    for idx in range(len(data.columns) - 1):
        if impacts[idx] == '+':
            ideal_best[idx] = np.max(weighted_data[:, idx])
            ideal_worst[idx] = np.min(weighted_data[:, idx])
        else:
            ideal_best[idx] = np.min(weighted_data[:, idx])
            ideal_worst[idx] = np.max(weighted_data[:, idx])

    # Step 4: Calculate separation distances
    separation_best = np.sqrt(np.sum((weighted_data - ideal_best)**2, axis=1))
    separation_worst = np.sqrt(np.sum((weighted_data - ideal_worst)**2, axis=1))

    # Step 5: Compute TOPSIS scores
    performance_scores = separation_worst / (separation_best + separation_worst)

    # Rank the scores
    rankings = len(performance_scores) - np.argsort(performance_scores).argsort()

    return performance_scores, rankings

def main():
    try:
        # Ensure proper command-line arguments
        if len(sys.argv) != 5:
            print("Usage: python <script.py> <InputFile> <Weights> <Impacts> <OutputFile>")
            sys.exit(1)

        input_path = sys.argv[1]
        input_weights = sys.argv[2]
        input_impacts = sys.argv[3]
        output_path = sys.argv[4]

        # Validate inputs and preprocess the data
        processed_data, processed_weights, processed_impacts = validate_arguments(
            input_path, input_weights, input_impacts, output_path
        )

        # Calculate TOPSIS scores and rankings
        scores, ranks = compute_topsis(processed_data, processed_weights, processed_impacts)

        # Append results to the dataframe
        processed_data['Topsis Score'] = scores.round(4)
        processed_data['Rank'] = ranks

        # Save the results to the specified output file
        processed_data.to_csv(output_path, index=False)
        print(f"Results successfully written to {output_path}")

    except Exception as error:
        print(f"Error: {str(error)}")
        sys.exit(1)

if __name__ == "__main__":
    main()