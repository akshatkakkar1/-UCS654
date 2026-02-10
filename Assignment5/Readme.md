# Data Generation using Modelling and Simulation for Machine Learning

## 📌 Overview
This assignment demonstrates the generation of synthetic datasets using **SimPy** discrete-event simulation library to model a multi-server queue system. The generated data is then used to train and compare multiple Machine Learning models for predicting average customer waiting time in a queue.

## 🎯 Objective
- Generate realistic queue simulation data using SimPy
- Create a dataset with 1000 samples
- Train and evaluate 7 different ML models
- Compare model performance using MAE, RMSE, and R² metrics

---

## 🧪 Methodology

### 🛠 Queue Simulation Design

The simulation models a **multi-server queue system** with the following characteristics:

| Component | Description |
|-----------|-------------|
| **Environment** | SimPy discrete-event simulation environment |
| **Servers** | Multiple servers (Resource) with variable capacity |
| **Arrivals** | Random customer arrivals following exponential distribution |
| **Service** | Random service times following exponential distribution |
| **Simulation Time** | 200 time units per run |

### 📊 Input Parameters & Bounds

| Parameter | Range | Description |
|-----------|-------|-------------|
| `arrival_rate` | 1 – 10 | Average number of customers arriving per time unit |
| `service_time` | 1 – 8 | Average service time per customer |
| `servers` | 1 – 5 | Number of available servers |

### 📈 Output Metrics

For each simulation run, the following metrics are recorded:

| Metric | Description |
|--------|-------------|
| `avg_wait` | Average waiting time for all customers |
| `max_wait` | Maximum waiting time experienced |
| `customers` | Total number of customers served |

---

## 🗂 Data Generation Process

1. **Random Parameter Generation**: For each iteration, randomly sample parameters within defined bounds
2. **Simulation Execution**: Run SimPy queue simulation with sampled parameters
3. **Metric Collection**: Record output metrics (avg_wait, max_wait, customers)
4. **Dataset Creation**: Repeat process 1000 times to create a comprehensive dataset

### Generated Dataset Structure

```
| arrival_rate | service_time | servers | avg_wait | max_wait | customers |
|--------------|--------------|---------|----------|----------|-----------|
| 3.45         | 5.23         | 2       | 12.34    | 45.67    | 567       |
| 7.89         | 2.15         | 4       | 3.21     | 15.43    | 1234      |
| ...          | ...          | ...     | ...      | ...      | ...       |
```

**Total Samples**: 1000

---

## 🤖 Machine Learning Pipeline

### Feature Engineering
- **Features (X)**: `arrival_rate`, `service_time`, `servers`, `customers`
- **Target (y)**: `avg_wait`

### Data Preprocessing
- **Train-Test Split**: 80% training, 20% testing
- **Scaling**: StandardScaler applied to features
- **Random State**: 42 (for reproducibility)

### Models Evaluated

1. **Linear Regression** - Baseline linear model
2. **Decision Tree** - Non-linear tree-based model
3. **Random Forest** - Ensemble of 100 decision trees
4. **Support Vector Regression (SVR)** - Kernel-based regression
5. **K-Nearest Neighbors (KNN)** - Instance-based learning
6. **Multi-Layer Perceptron (MLP)** - Neural network (500 iterations)
7. **XGBoost** - Gradient boosting ensemble

### Evaluation Metrics
- **MAE (Mean Absolute Error)**: Average prediction error magnitude
- **RMSE (Root Mean Squared Error)**: Penalizes larger errors more
- **R² Score**: Proportion of variance explained by the model

---

## 📈 Results

### 🏆 Model Performance Comparison

| Model | MAE ⬇️ | RMSE ⬇️ | R² ⬆️ |
|-------|--------|---------|-------|
| **Random Forest** | **4.94** | **6.58** | **0.917** |
| **XGBoost** | 5.68 | 7.53 | 0.892 |
| **KNN** | 5.89 | 8.09 | 0.875 |
| **Decision Tree** | 6.66 | 9.21 | 0.838 |
| **MLP** | 7.07 | 9.29 | 0.835 |
| **SVR** | 7.67 | 11.96 | 0.727 |
| **Linear Regression** | 9.92 | 12.75 | 0.690 |

*⬇️ Lower is better | ⬆️ Higher is better*

### 📊 Key Insights

✅ **Random Forest** emerged as the best performer with:
   - Lowest MAE (4.94) and RMSE (6.58)
   - Highest R² score (0.917), explaining 91.7% of variance

✅ **Ensemble methods** (Random Forest, XGBoost) significantly outperformed other models

✅ **Tree-based models** (Decision Tree, Random Forest, XGBoost) captured non-linear relationships effectively

❌ **Linear Regression** performed poorly (R² = 0.69), confirming the non-linear nature of queue dynamics

❌ **SVR** also struggled (R² = 0.727), suggesting kernel selection issues

### 📉 Visualization

A bar chart comparing R² scores shows clear performance hierarchy:
- Random Forest and XGBoost dominate with R² > 0.89
- Tree-based models cluster in the 0.83-0.91 range
- Linear models lag behind significantly

---

## 🧰 Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Primary programming language |
| **SimPy** | Discrete-event simulation library |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computations |
| **Scikit-Learn** | ML models and preprocessing |
| **XGBoost** | Gradient boosting implementation |
| **Matplotlib** | Data visualization |
| **Google Colab** | Development environment |

---

## 💡 Conclusions

1. **Simulation-Generated Data is Effective**: SimPy successfully created a realistic dataset suitable for supervised learning

2. **Non-Linear Relationships Exist**: The queue system exhibits complex, non-linear relationships between input parameters and waiting times

3. **Ensemble Methods Excel**: Random Forest's superior performance (91.7% R²) demonstrates the power of ensemble learning for simulation data

4. **Practical Applications**: This approach can be extended to:
   - Hospital emergency room optimization
   - Call center staffing prediction
   - Manufacturing process optimization
   - Restaurant queue management

5. **Model Selection Matters**: Choosing the right model family (tree-based vs linear) is crucial for simulation-based ML tasks

---

## 🚀 Future Enhancements

- Increase dataset size to 5000+ samples
- Add more complex queue features (priority queues, multiple service types)
- Implement hyperparameter tuning (GridSearch, RandomSearch)
- Add time-series features for temporal patterns
- Deploy best model as a web service for real-time predictions

---

## 📝 How to Run

1. Open `data_gen.ipynb` in Google Colab or Jupyter
2. Install required libraries: `!pip install simpy xgboost`
3. Run all cells sequentially
4. View model comparison results and visualization

---

## 👨‍💻 Author - Akshat Kakkar
**Assignment 5 - UCS654**  
Data Generation using Modelling and Simulation