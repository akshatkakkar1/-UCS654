# 🌍 Probability Density Function Learning via Roll-Number Parameterization

**UCS654: Predictive Analysis Using Statistics**  
**Assignment 1** | Roll Number: **102303730**

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Dataset](#-dataset)
- [Methodology](#-methodology)
- [Implementation](#-implementation)
- [Results](#-results)
- [Key Insights](#-key-insights)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [How to Run](#-how-to-run)

---

## 🎯 Overview

This project explores **probability density functions (PDFs)** through a unique roll-number-parameterized nonlinear transformation applied to real-world air quality data. By leveraging statistical methods, we estimate the parameters of a Gaussian-like distribution from transformed NO₂ concentration values.

### 🔍 Problem Statement
- Apply a **nonlinear transformation** to air quality data based on university roll number
- Learn and estimate parameters of the resulting **probability density function**
- Demonstrate understanding of statistical modeling and data transformation techniques

---

## 📊 Dataset

**Source:** India Air Quality Dataset (Kaggle)

**Variable of Interest:** Nitrogen Dioxide (NO₂) Concentration

**Preprocessing Steps:**
- Extracted NO₂ concentration values from raw data
- Removed missing and invalid entries using `dropna()`
- Converted data to float type for numerical computations
- **Dataset Size:** Large-scale air quality measurements (>50MB)

---

## 🧮 Methodology

### Step 1: Roll-Number-Based Nonlinear Transformation

Each NO₂ data point $x$ undergoes a nonlinear transformation:

$$z = x + a_r \cdot \sin(b_r \cdot x)$$

where the parameters are derived from roll number $r = 102303730$:

$$a_r = 0.05 \times (r \bmod 7)$$
$$b_r = 0.3 \times (r \bmod 5 + 1)$$

### Step 2: Probability Density Function Estimation

The transformed variable $z$ follows an assumed PDF of the form:

$$\hat{p}(z) = c \cdot e^{-\lambda (z - \mu)^2}$$

### Parameter Estimation

**1. Mean (Location Parameter):**
$$\mu = \frac{1}{N} \sum_{i=1}^{N} z_i$$

**2. Variance:**
$$\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (z_i - \mu)^2$$

**3. Lambda (Precision Parameter):**
$$\lambda = \frac{1}{2\sigma^2}$$

**4. Normalization Constant:**
$$c = \sqrt{\frac{\lambda}{\pi}}$$

---

## 💻 Implementation

### Code Structure

```python
# 1. Import Libraries
import pandas as pd
import numpy as np

# 2. Load and Preprocess Data
ROLL_NUMBER = 102303730
df = pd.read_csv("data.csv", encoding="latin1", on_bad_lines='skip')
x = df["no2"].dropna().astype(float).values

# 3. Roll-Number-Based Transformation
a_r = 0.05 * (ROLL_NUMBER % 7)
b_r = 0.3 * (ROLL_NUMBER % 5 + 1)
z = x + a_r * np.sin(b_r * x)

# 4. Parameter Estimation
mean = np.mean(z)
variance = np.var(z)
lam = 1 / (2 * variance)
c = np.sqrt(lam / np.pi)
```

---

## 📈 Results

### Computed Parameters

| Parameter | Symbol | Value |
|-----------|--------|-------|
| **Roll-based coefficient** | $a_r$ | `0.2` |
| **Roll-based coefficient** | $b_r$ | `0.3` |
| **Mean** | $\mu$ | `23.0898` |
| **Lambda** | $\lambda$ | `0.001993` |
| **Normalization constant** | $c$ | `0.02519` |

### Resulting Probability Density Function

$$\hat{p}(z) = 0.02519 \cdot e^{-0.001993 \cdot (z - 23.09)^2}$$

---

## 💡 Key Insights

✅ **Personalized Transformation:** Roll-number parameterization ensures unique nonlinear transformations for each student

✅ **Gaussian-Like Distribution:** The transformed data exhibits characteristics similar to a normal distribution

✅ **Statistical Rigor:** Parameters estimated using fundamental statistical measures (mean, variance)

✅ **Real-World Application:** Demonstrates practical application of probability theory to environmental data

✅ **Data Quality:** Successfully handled large-scale dataset with proper preprocessing techniques

---

## 🛠 Technologies Used

- **Python 3.x** - Core programming language
- **pandas** - Data manipulation and CSV handling
- **NumPy** - Numerical computations and array operations
- **Jupyter Notebook** - Interactive development environment

---

## 📁 Project Structure

```
Assignment1/
│
├── data.csv              # India Air Quality Dataset (>50MB)
├── PythonCode.ipynb      # Implementation notebook
└── Readme.md             # Project documentation
```

---

## 🚀 How to Run

1. **Clone or download** the project directory

2. **Install required packages:**
   ```bash
   pip install pandas numpy jupyter
   ```

3. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook PythonCode.ipynb
   ```

4. **Run all cells** to reproduce the analysis

---

## 📝 Conclusion

This assignment successfully demonstrates the application of probability theory and statistical modeling to real-world environmental data. The roll-number-based parameterization creates a unique analytical framework while maintaining scientific rigor in parameter estimation and distribution modeling.

---

**Course:** UCS654 - Predictive Analysis Using Statistics  
**Institution:** University Institute of Engineering  
**Semester:** January 2026