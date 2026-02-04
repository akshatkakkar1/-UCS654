# TOPSIS Python Package

**TOPSIS** (Technique for Order Preference by Similarity to Ideal Solution) is a multi-criteria decision analysis method.

## Installation

```bash
pip install Topsis-Akshat-102303730
```

## Usage

### Command Line

```bash
topsis <input_file> <weights> <impacts> <output_file>
```

### Parameters

- **input_file**: Path to input CSV file
- **weights**: Comma-separated weights (e.g., "1,1,1,2")
- **impacts**: Comma-separated impacts, either + or - (e.g., "+,+,-,+")
- **output_file**: Path to output CSV file

### Example

```bash
topsis data.csv "1,1,1,2" "+,+,-,+" result.csv
```

### Input File Format

The input CSV file should have:
- First column: Object/item names
- Remaining columns: Criteria values (numeric)

Example:
```
Model,Price,Storage,Camera,Looks
M1,250,16,12,5
M2,200,16,8,3
M3,300,32,16,4
```

### Output

The output file will contain:
- All original columns
- **Topsis Score**: Calculated TOPSIS score
- **Rank**: Rank based on TOPSIS score

## Requirements

- Python >= 3.6
- pandas >= 1.0.0
- numpy >= 1.18.0

## License

MIT License

## Author

Akshat Kakkar

## Links

- GitHub: https://github.com/akshatkakkar1/-UCS654
