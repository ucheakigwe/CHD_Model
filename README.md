# Coronary Heart Disease Prediction Model

This repository contains the project for developing a machine learning-based prediction model for coronary heart disease (CHD). The study leverages data preprocessing, feature selection, and machine learning algorithms to enhance early detection, prevention, and personalized healthcare.

## Project Overview

Coronary heart disease (CHD) is a leading cause of death globally. This project employs machine learning to predict CHD risk based on demographic, clinical, and lifestyle factors. It emphasizes the importance of data quality, ethical considerations, and collaboration between data scientists and healthcare professionals.

### Key Features:
- Comprehensive data preprocessing and cleaning.
- Feature selection using Random Forest for dimensionality reduction.
- Implementation of machine learning models, including:
  - Decision Tree
  - K-Nearest Neighbors (KNN)
  - Random Forest
- Addressing class imbalance using SMOTE (Synthetic Minority Over-sampling Technique).
- Evaluation metrics such as accuracy, precision, recall, F1-score, and AUC-ROC.

---

## Table of Contents
- [Background](#background)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Results](#results)
- [Conclusion](#conclusion)
- [References](#references)

---

## Background

Coronary heart disease accounts for millions of deaths annually. While traditional risk assessment tools are limited, machine learning offers a broader and more precise approach by analyzing complex interactions among diverse factors.

### Benefits of Machine Learning:
- Higher accuracy than traditional tools.
- Comprehensive inclusion of non-traditional risk factors.
- Adaptability and personalization.

---

## Dataset

The dataset originates from the **Behavioral Risk Factor Surveillance System (BRFSS) 2021**, collected by the U.S. Centers for Disease Control and Prevention (CDC). It includes over **438,000 records** with **304 attributes**, reduced to 25 key features after preprocessing.

### Key Preprocessing Steps:
1. Handling missing values and imputation.
2. Normalization of numerical features.
3. Feature selection using Random Forest importance scores.

---

## Methodology

1. **Data Preprocessing**:
   - Addressed missing data and imbalanced classes.
   - Applied feature engineering techniques.
2. **Feature Selection**:
   - Top features identified using Random Forest.
3. **Machine Learning Models**:
   - Implemented and compared models using PyCaret.
   - Validated results using Scikit-learn implementations.

### Tools and Libraries:
- Python, Pandas, Scikit-learn, PyCaret

---

## Results

- **K-Nearest Neighbors (KNN)** achieved the best performance with:
  - Training Accuracy: **91%**
  - Test Accuracy: **87%**
  - Balanced precision, recall, and F1-scores.
- **Random Forest** and **Decision Tree** models also demonstrated strong performance but required careful hyperparameter tuning to mitigate overfitting.

---

## Conclusion

The **KNN algorithm** proved most effective for CHD prediction, balancing flexibility, adaptability, and simplicity. The model provides actionable insights for early prevention and personalized healthcare strategies.

---

## References

- [Behavioral Risk Factor Surveillance System (BRFSS)](https://www.cdc.gov/brfss/)
- [PyCaret Documentation](https://pycaret.org/)
- Research papers and relevant studies listed in the project document.

---
