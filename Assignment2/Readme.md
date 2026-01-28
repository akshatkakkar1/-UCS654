# Assignment 2: Learning Probability Density Functions using GANs

## 📋 Objective
This assignment focuses on learning an unknown probability density function (PDF) of a transformed random variable using a **Generative Adversarial Network (GAN)** without assuming any analytical or parametric distribution. The goal is to demonstrate that GANs can effectively learn complex distributions directly from data.

---

## 📊 Dataset
- **Dataset Name:** India Air Quality Data
- **Feature Used:** NO₂ Concentration (x)
- **Source:** Kaggle
- **Dataset Link:** [India Air Quality Data](https://www.kaggle.com/datasets/shrutibhargava94/india-air-quality-data)

---

## 🔧 Transformation Parameters

**University Roll Number:** `102303730`

The transformation parameters are computed as follows:

| Parameter | Formula | Value |
|-----------|---------|-------|
| **a_r** | 0.5 × (r mod 7) | **2.0** |
| **b_r** | 0.3 × ((r mod 5) + 1) | **0.3** |

### Transformation Function
```
z = Tr(x) = x + a_r × sin(b_r × x)
z = x + 2.0 × sin(0.3 × x)
```

where:
- `x` = Original NO₂ concentration values
- `z` = Transformed values
- `mod` returns the remainder
- `r` = University Roll Number

---

## 🏗️ GAN Architecture

### Generator Network
The generator transforms random noise into synthetic samples that follow the target distribution.

| Layer | Input Dimension | Output Dimension | Activation |
|-------|----------------|------------------|------------|
| Linear 1 | 1 | 32 | Tanh |
| Linear 2 | 32 | 64 | ReLU |
| Linear 3 | 64 | 1 | None |

**Input:** Random noise sampled from standard normal distribution N(0,1)  
**Output:** Generated z samples

### Discriminator Network
The discriminator classifies whether a given sample is real or generated.

| Layer | Input Dimension | Output Dimension | Activation |
|-------|----------------|------------------|------------|
| Linear 1 | 1 | 64 | LeakyReLU (α=0.1) |
| Linear 2 | 64 | 32 | LeakyReLU (α=0.1) |
| Linear 3 | 32 | 1 | Sigmoid |

**Input:** Real or generated z samples  
**Output:** Probability that input is real (0 to 1)

### Training Configuration
- **Loss Function:** Binary Cross-Entropy (BCE)
- **Optimizer:** Adam
- **Learning Rate:** 0.00015 (both networks)
- **Batch Size:** 64
- **Training Epochs:** 2500
- **Data Preprocessing:** StandardScaler normalization

---

## 📈 Results

### PDF Plot
![Uploading image.png…]()


---

## 🔍 Observations

### 1. Mode Coverage
- ✅ The generator successfully captures the **major modes** of the transformed distribution
- ⚠️ Minor mode collapse may occur occasionally due to adversarial training dynamics
- The GAN learned to represent both the central tendency and the tail behavior of the distribution
- Multiple peaks in the original distribution were preserved in the generated samples

### 2. Training Stability
- ✅ **Training remained stable** throughout 2500 epochs after applying data normalization
- Generator and discriminator losses **converged gradually**, indicating balanced adversarial learning
- No catastrophic divergence or mode collapse was observed during training
- The learning rate of 0.00015 proved optimal for stable convergence
- Loss oscillations decreased over time, suggesting successful adversarial equilibrium

### 3. Quality of Generated Distribution
- ✅ The GAN-generated PDF **closely matches** the real transformed data distribution
- Statistical similarity between real and generated distributions confirms successful learning
- The generated samples capture both the shape and spread of the target distribution
- Kernel Density Estimation (KDE) shows strong overlap between real and synthetic data
- This demonstrates **successful implicit learning** of the unknown PDF without parametric assumptions

---

## 🛠️ Methodology

### Step 1: Data Transformation
1. Load NO₂ concentration data from the India Air Quality dataset
2. Apply the nonlinear transformation using roll-number-specific parameters
3. Generate transformed samples: `z = x + 2.0 × sin(0.3 × x)`

### Step 2: GAN Training
1. Normalize transformed data using StandardScaler
2. Initialize Generator and Discriminator networks
3. Train adversarially:
   - Discriminator learns to distinguish real vs fake samples
   - Generator learns to produce realistic transformed samples
4. Monitor loss convergence

### Step 3: PDF Estimation
1. Generate large number of synthetic samples from trained Generator
2. Estimate probability density function using:
   - Histogram density estimation
   - Kernel Density Estimation (KDE)
3. Compare generated distribution with real transformed data

---

## 💻 Tools and Libraries
- **Python 3.x**
- **PyTorch** - Deep learning framework for GAN implementation
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical plotting
- **Scikit-learn** - Data preprocessing (StandardScaler)

---

## 📝 Conclusion
- A **nonlinear transformation** was successfully applied to NO₂ concentration data using roll-number-based parameters (a_r = 2.0, b_r = 0.3)
- A **Generative Adversarial Network** was trained to learn the unknown probability distribution without assuming any parametric form
- Generated samples **closely matched** the real data distribution, verified using histogram and KDE plots
- This experiment demonstrates the **effectiveness of GANs** in learning complex probability distributions directly from data
- The approach successfully learned an implicit representation of the transformed PDF using only data samples

---

## 👤 Author
**Akshat Kakkar**  
Roll Number: 102303730  



