# Sampling Techniques on Imbalanced Credit Card Dataset

<div align="center">

**Assignment 02 - UCS654**

**Name:** Akshat Kakkar  
**Roll Number:** 102303730

</div>

---

## 📋 Problem Statement

The objective of this assignment is to understand the importance of **sampling techniques** in handling imbalanced datasets and to analyze how different sampling strategies affect the performance of various machine learning models.

A highly imbalanced credit card fraud dataset was provided. Such imbalance can significantly degrade classification performance. The task was to balance the dataset using multiple sampling techniques and evaluate their impact on different machine learning models.

---

## 🔬 Methodology

### 📊 Dataset
The credit card dataset was downloaded from the provided GitHub source and loaded into a pandas DataFrame. The dataset contains a severe class imbalance between fraudulent and non-fraudulent transactions.

### 🎯 Sampling Techniques Applied

Five sampling techniques were used to create balanced datasets:

| Sampling ID | Technique | Description |
|------------|-----------|-------------|
| **Sampling1** | Random UnderSampling | Randomly removes samples from majority class |
| **Sampling2** | Random OverSampling | Randomly duplicates samples from minority class |
| **Sampling3** | SMOTE | Synthetic Minority Oversampling Technique |
| **Sampling4** | SMOTE-Tomek | Combination of SMOTE and Tomek links |
| **Sampling5** | NearMiss | Undersampling based on distance metrics |

### 🤖 Machine Learning Models

Five classification models were trained on each sampled dataset:

| Model ID | Algorithm |
|----------|-----------|
| **M1** | Logistic Regression |
| **M2** | Decision Tree |
| **M3** | Random Forest |
| **M4** | K-Nearest Neighbors |
| **M5** | Gaussian Naive Bayes |

### 📝 Evaluation Procedure

1. Each sampled dataset was split into training and testing sets
2. Models were trained on the training data
3. Accuracy was computed on the test data
4. Results were compared across all model–sampling combinations

---

## 📊 Results

### Accuracy Comparison

Accuracy (%) comparison of models across sampling techniques:

| Model | Sampling1 | Sampling2 | Sampling3 | Sampling4 | Sampling5 |
|-------|-----------|-----------|-----------|-----------|-----------|
| **Logistic Regression** | 33.33 | 91.92 | 91.92 | **92.79** | 50.00 |
| **Decision Tree** | 50.00 | **98.69** | 98.25 | 97.97 | 16.67 |
| **Random Forest** | 33.33 | **100.00** | 99.34 | 99.55 | 16.67 |
| **KNN** | 33.33 | **98.47** | 83.84 | 86.71 | 83.33 |
| **Naive Bayes** | 33.33 | 74.67 | **87.77** | 82.66 | 33.33 |

### 🏆 Best Sampling Technique per Model

| Model | Best Sampling Technique | Accuracy |
|-------|------------------------|----------|
| Logistic Regression | **Sampling4** (SMOTE-Tomek) | 92.79% |
| Decision Tree | **Sampling2** (Random OverSampling) | 98.69% |
| Random Forest | **Sampling2** (Random OverSampling) | 100.00% |
| KNN | **Sampling2** (Random OverSampling) | 98.47% |
| Naive Bayes | **Sampling3** (SMOTE) | 87.77% |

### 🔍 Key Observations

- **Random OverSampling (Sampling2)** performed best for most models (4 out of 5)
- **Random Forest** achieved perfect accuracy (100%) with Random OverSampling
- **Random UnderSampling (Sampling1)** and **NearMiss (Sampling5)** showed poor performance
- **SMOTE-based techniques** (Sampling3 & Sampling4) provided consistent, reliable results

---

## 💡 Conclusion

This study demonstrates the **critical importance** of sampling strategies when working with imbalanced datasets. Key takeaways:

- Different sampling techniques affect model performance differently
- No single sampling method is optimal for all models
- Random OverSampling showed strong performance across multiple classifiers
- SMOTE-based techniques provide a good balance of synthetic data generation
- Selecting an appropriate sampling strategy can substantially improve classification accuracy in fraud detection tasks

---

## 📁 Files

- `Sampling_102303730.ipynb` - Jupyter notebook with complete implementation
- `Creditcard_data.csv` - Credit card dataset used for analysis
- `Readme.md` - This documentation file

