# 📊 Comparative Performance Analysis of Pretrained Text Summarization Models using TOPSIS

## 🚀 Project Overview

This project presents a comparative performance analysis of multiple pretrained text summarization models from Hugging Face using the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) multi-criteria decision-making method.

The objective is to identify the most suitable summarization model across different text domains by evaluating multiple performance metrics simultaneously.

---

## 🎯 Motivation

Text summarization models perform differently across domains such as Politics, Sports, and Finance. Instead of relying on a single evaluation metric (like ROUGE), this project:

- Evaluates models using multiple quality and efficiency metrics
- Applies TOPSIS to rank models based on overall performance
- Identifies domain-specific best-performing models

This approach provides a balanced and structured model selection strategy.

---

## 🗂️ Domains Considered

The dataset was filtered into three domains:

- 🏛 Politics  
- ⚽ Sports  
- 💰 Finance  

---

## 🤖 Models Evaluated

The following pretrained models from Hugging Face were used:

- `facebook/bart-base`
- `google/pegasus-cnn_dailymail`
- `t5-base`
- `t5-small`

All models were evaluated under identical experimental conditions.

---

## 📚 Dataset

- **CNN/DailyMail Dataset**
- Loaded using Hugging Face `datasets` library
- Articles filtered into domains using keyword-based classification
- Equal number of samples per domain used for fairness

---

## 📏 Evaluation Metrics

Each generated summary was evaluated using the following criteria:

### Maximization Criteria:
- ROUGE-1
- ROUGE-2
- ROUGE-L
- BERTScore

### Minimization Criteria:
- Compression Ratio
- Inference Time

These metrics capture both quality and computational efficiency.

---

## 🧮 TOPSIS Methodology

TOPSIS was implemented manually using NumPy to ensure transparency and reproducibility.

Steps followed:

1. Construct decision matrix
2. Normalize the matrix
3. Apply weights to criteria
4. Identify ideal and negative ideal solutions
5. Compute Euclidean distances
6. Calculate relative closeness scores
7. Rank models per domain

Equal weights were used in the base experiment.

---

## 📊 Results

Below is the TOPSIS score comparison across domains:

<br>



<br>

---

## 🏆 Key Findings

- Model performance varies across domains.
- Some models show strong consistency across multiple domains.
- Efficiency metrics (inference time, compression ratio) significantly influence final ranking.
- Multi-criteria decision-making provides more balanced evaluation than single-metric comparison.

---

## 🛠️ Tech Stack

- Python
- Google Colab
- Hugging Face Transformers
- Hugging Face Datasets
- Evaluate (ROUGE, BERTScore)
- NumPy
- Pandas
- Seaborn / Matplotlib

---

## 📂 Project Structure

```
├── dataset_loading.ipynb
├── summarization_pipeline.ipynb
├── evaluation_metrics.ipynb
├── topsis_implementation.ipynb
├── results_visualization.ipynb
└── README.md
```

---

## 🔬 Future Improvements

- Use entropy-based weighting instead of equal weights
- Add more domains (Medical, Technology, Legal)
- Compare extractive vs abstractive models
- Perform statistical significance testing
- Evaluate large-scale models (BART-large, FLAN-T5-large)

---

## 📌 Conclusion

This project demonstrates how multi-criteria decision-making techniques like TOPSIS can be effectively applied to model evaluation in NLP.

Rather than selecting a model based solely on ROUGE scores, this approach provides a structured, domain-aware, and performance-balanced framework for model selection.

---
