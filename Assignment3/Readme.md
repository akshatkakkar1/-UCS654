# Assignment 3: TOPSIS Implementation

## 📋 Overview

This assignment implements **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** - a multi-criteria decision analysis method. The project includes three parts:

1. **Part 1**: Command-line TOPSIS script
2. **Part 2**: TOPSIS Python package
3. **Part 3**: Web-based TOPSIS service with email functionality

---

## 📁 Project Structure

```
Assignment3/
├── .env                          # Environment variables for email configuration
├── Part1/
│   └── topsis.py                # Command-line TOPSIS implementation
├── Part2/
│   └── Topsis/
│       └── topsis.py            # TOPSIS Python package
├── Part3/
│   ├── backend/
│   │   ├── app.py              # Flask web application
│   │   ├── topsis_logic.py     # TOPSIS calculation logic
│   │   ├── templates/
│   │   │   └── index.html      # Web interface
│   │   ├── uploads/            # Uploaded CSV files
│   │   └── outputs/            # Generated result files
│   └── frontend/
│       └── index.html          # Original frontend template
├── data (1).csv                 # Sample input data
├── result.csv                   # Sample output data
└── Readme.md                    # This file
```

---

## 🎯 Part 1: Command-Line TOPSIS

### Description
A standalone Python script that performs TOPSIS analysis on CSV data files via command line.

### Features
- ✅ Input validation (file existence, data format, numeric values)
- ✅ Customizable weights and impacts
- ✅ Automatic normalization and scoring
- ✅ Ranking generation
- ✅ CSV output with TOPSIS scores and ranks

### Usage

```bash
cd Part1
python3 topsis.py <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

#### Example:
```bash
python3 topsis.py ../data\ \(1\).csv "1,1,1,1,1" "+,+,+,+,+" ../result.csv
```

#### Parameters:
- **InputDataFile**: CSV file with first column as object names, rest as criteria
- **Weights**: Comma-separated numeric values (e.g., "1,1,1,1,1")
- **Impacts**: Comma-separated +/- values (e.g., "+,+,-,+,+")
  - `+` : Higher value is better
  - `-` : Lower value is better
- **ResultFileName**: Output CSV file path

### Input Format
```csv
Fund Name,P1,P2,P3,P4,P5
M1,0.84,0.71,6.7,42.1,12.59
M2,0.91,0.83,7.0,31.7,10.11
...
```

### Output Format
Original data with two additional columns:
- `Topsis Score`: Calculated TOPSIS score (0-1)
- `Rank`: Ranking based on TOPSIS score (1 = best)

---

## 📦 Part 2: TOPSIS Python Package

### Description
TOPSIS implemented as a distributable Python package published on PyPI.

### 🔗 PyPI Package
**Package Name**: `Topsis-Akshat-102303730`  
**PyPI Link**: [https://pypi.org/project/Topsis-Akshat-102303730/1.0.0/](https://pypi.org/project/Topsis-Akshat-102303730/1.0.0/)

### Installation
```bash
pip install Topsis-Akshat-102303730
```

### Usage

#### As a Command-Line Tool:
```bash
topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

#### Example:
```bash
topsis data.csv "1,1,1,2" "+,+,-,+" result.csv
```

#### As a Python Module:
```python
from Topsis import main
import sys

# Set command line arguments
sys.argv = ['topsis', 'data.csv', '1,1,1,2', '+,+,-,+', 'result.csv']
main()
```

### Package Structure
```
Part2/
├── Topsis/
│   ├── __init__.py
│   └── topsis.py
├── setup.py
├── README.md
├── LICENSE
└── MANIFEST.in
```

---

## 🌐 Part 3: Web-Based TOPSIS Service

### Description
A full-stack web application that allows users to:
- Upload CSV files through a web interface
- Enter weights and impacts dynamically
- Receive TOPSIS results via email automatically

### Technology Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3
- **Email**: SMTP (Gmail)
- **Libraries**: pandas, numpy, python-dotenv

### Setup Instructions

#### 1. Install Dependencies
```bash
cd Part3/backend
pip3 install flask pandas numpy python-dotenv
```

#### 2. Configure Email Settings

Edit `.env` file in Assignment3 root directory:
```env
SENDER_EMAIL=your.email@gmail.com
APP_PASSWORD=your_app_password_here
```

**Getting Gmail App Password:**
1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Navigate to **Security** → **2-Step Verification** (enable if not active)
3. Go to **Security** → **App Passwords**
4. Generate password for "Mail"
5. Copy the 16-character password to `.env`

#### 3. Run the Application
```bash
cd Part3/backend
python3 app.py
```

#### 4. Access the Web Interface
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

### Web Interface Features

- 📁 **File Upload**: Drag and drop or browse CSV files
- ⚖️ **Weights Input**: Enter comma-separated weights
- ➕➖ **Impacts Input**: Enter comma-separated impacts (+/-)
- 📧 **Email Delivery**: Results sent automatically to specified email
- ✅ **Real-time Validation**: Input validation and error messages
- 🎨 **Responsive Design**: Clean, modern UI with visual feedback

### API Endpoints

#### `GET /`
Returns the main HTML interface

#### `POST /submit`
Processes TOPSIS calculation and sends results

**Form Data:**
- `file`: CSV file (multipart/form-data)
- `weights`: String (comma-separated)
- `impacts`: String (comma-separated)
- `email`: String (valid email address)

**Response:**
- Success/error message displayed on webpage
- Result CSV sent to email if successful

---

## 🔧 TOPSIS Algorithm

### Steps:
1. **Normalize** the decision matrix
2. **Weight** the normalized matrix
3. **Identify** ideal best and worst solutions
4. **Calculate** Euclidean distances from ideal solutions
5. **Compute** TOPSIS score: `Score = S- / (S+ + S-)`
6. **Rank** alternatives based on scores

### Methodology in Detail:

#### 1. Normalization
The decision matrix is normalized using vector normalization so that all criteria are dimensionless and comparable.

**Formula**: `rᵢⱼ = xᵢⱼ / √(∑xᵢⱼ²)`

#### 2. Weighting
Each normalized criterion is multiplied by its assigned weight to reflect its importance.

**Formula**: `vᵢⱼ = wⱼ × rᵢⱼ`

#### 3. Ideal Best / Worst
For each criterion, determine the ideal best and ideal worst:
- **Benefit (+)**: best = max, worst = min
- **Cost (−)**: best = min, worst = max

#### 4. Separation Measures
Calculate the Euclidean distance of each alternative from the ideal best and worst.

**Formulas**:
- `Sᵢ⁺ = √(∑(vᵢⱼ − vⱼ⁺)²)`
- `Sᵢ⁻ = √(∑(vᵢⱼ − vⱼ⁻)²)`

#### 5. TOPSIS Score
Compute the relative closeness to the ideal solution.

**Formula**: `Cᵢ = Sᵢ⁻ / (Sᵢ⁺ + Sᵢ⁻)`

#### 6. Ranking
Alternatives are ranked based on their TOPSIS scores.
- **Higher score** ⇒ **Better rank**

---

## 📊 Sample Data

### Input (data.csv)

| Fund Name | P1   | P2   | P3  | P4   | P5    |
|-----------|------|------|-----|------|-------|
| M1        | 0.84 | 0.71 | 6.7 | 42.1 | 12.59 |
| M2        | 0.91 | 0.83 | 7.0 | 31.7 | 10.11 |
| M3        | 0.79 | 0.62 | 4.8 | 46.7 | 13.23 |
| M4        | 0.78 | 0.61 | 6.4 | 42.4 | 12.55 |
| M5        | 0.94 | 0.88 | 3.6 | 62.2 | 16.91 |
| M6        | 0.88 | 0.77 | 6.5 | 51.5 | 14.91 |
| M7        | 0.66 | 0.44 | 5.3 | 48.9 | 13.83 |
| M8        | 0.93 | 0.86 | 3.4 | 37.0 | 10.55 |

### Output (result.csv)

| Fund Name | P1   | P2   | P3  | P4   | P5    | Topsis Score | Rank |
|-----------|------|------|-----|------|-------|--------------|------|
| M1        | 0.84 | 0.71 | 6.7 | 42.1 | 12.59 | 0.3821       | 6    |
| M2        | 0.91 | 0.83 | 7.0 | 31.7 | 10.11 | 0.3665       | 7    |
| M3        | 0.79 | 0.62 | 4.8 | 46.7 | 13.23 | 0.4964       | 4    |
| M4        | 0.78 | 0.61 | 6.4 | 42.4 | 12.55 | 0.3248       | 8    |
| M5        | 0.94 | 0.88 | 3.6 | 62.2 | 16.91 | 0.9721       | 1    |
| M6        | 0.88 | 0.77 | 6.5 | 51.5 | 14.91 | 0.5470       | 3    |
| M7        | 0.66 | 0.44 | 5.3 | 48.9 | 13.83 | 0.3950       | 5    |
| M8        | 0.93 | 0.86 | 3.4 | 37.0 | 10.55 | 0.5601       | 2    |

---

## ⚠️ Error Handling

All implementations handle:
- ❌ Missing or invalid files
- ❌ Non-numeric values in criteria columns
- ❌ Insufficient columns (minimum 3 required)
- ❌ Mismatched weights/impacts count
- ❌ Invalid impact values (must be + or -)
- ❌ Invalid email format (Part 3 only)

---

## 🚀 Quick Start

### Running Part 1:
```bash
cd Assignment3/Part1
python3 topsis.py ../data\ \(1\).csv "1,1,1,1,1" "+,+,+,+,+" output.csv
```

### Running Part 3:
```bash
cd Assignment3/Part3/backend
python3 app.py
# Open http://127.0.0.1:5000 in browser
```

---

## 📝 Requirements

### Python Packages:
```
pandas
numpy
flask
python-dotenv
```

Install all at once:
```bash
pip3 install pandas numpy flask python-dotenv
```

### Python Version:
Python 3.7 or higher

---

## 🔐 Security Notes

- ⚠️ Never commit `.env` file to version control
- 🔑 Use App Passwords, not regular Gmail passwords
- 🛡️ Keep email credentials secure
- 🚀 For production, use proper WSGI server (not Flask development server)

---


## 🎓 Academic Information

Akshat Kakkar
102303730

---

## 📄 License

This project is part of academic coursework for UCS654.

---

