import pandas as pd
import numpy as np
import os

def run_topsis(input_file, weights, impacts, output_file):
    # File existence check
    if not os.path.isfile(input_file):
        raise Exception("File not found")

    # Read input file
    try:
        data = pd.read_csv(input_file)
    except:
        raise Exception("Unable to read input file")

    # Minimum 3 columns
    if data.shape[1] < 3:
        raise Exception("Input file must contain at least 3 columns")

    # Extract criteria columns
    criteria = data.iloc[:, 1:]

    # Numeric check
    if not np.all(criteria.map(np.isreal)):
        raise Exception("Non-numeric value found")

    # Length check
    if len(weights) != criteria.shape[1] or len(impacts) != criteria.shape[1]:
        raise Exception("Number of weights/impacts must match number of criteria")

    # Impact validation
    for i in impacts:
        if i not in ['+', '-']:
            raise Exception("Impacts must be + or -")

    # Step 1: Normalize
    norm = criteria / np.sqrt((criteria ** 2).sum())

    # Step 2: Weight multiplication
    weighted = norm * weights

    # Step 3: Ideal best & worst
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Distance measures
    s_pos = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    s_neg = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Topsis score
    score = s_neg / (s_pos + s_neg)

    # Step 6: Rank
    data["Topsis Score"] = score
    data["Rank"] = data["Topsis Score"].rank(ascending=False, method="dense").astype(int)

    # Save output
    data.to_csv(output_file, index=False)