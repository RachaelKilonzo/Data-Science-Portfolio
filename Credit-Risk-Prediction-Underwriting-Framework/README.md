<<<<<<< HEAD

# Data-Science-Portfolio


A curated collection of data science projects focusing on Exploratory Data Analysis (EDA), Web Scraping, Sentiment Analysis, and Data Visualization. Includes diverse datasets ranging from Olympic sports and urban mobility to literary analysis and public health trends. Built with Python, R, and Jupyter Notebooks to showcase data storytelling.


### [Tokyo-Decathlon](https://github.com/RachaelKilonzo/Data-Science-Portfolio/tree/main/Tokyo-Decathlon)

### [Olympics-Marathon](https://github.com/RachaelKilonzo/Data-Science-Portfolio/tree/main/Olympics-Marathon)
![marathon times plot](https://github.com/RachaelKilonzo/Data-Science-Portfolio/blob/main/Olympics-Marathon/marathon.png)
=======
#  Default Prediction System using XGBoost

---

## Summary
Traditional credit scoring models (like FICO) often rely heavily on static history, potentially excluding "credit invisible" applicants who are financially stable, while approving prime borrowers who are actually over-leveraged.

This project analyzes over **2.2 million loan applications** (Lending Club, 2007–2018) to build a machine learning framework capable of predicting the **Probability of Default (PoD)**. By engineering features that measure borrower "capacity" and "intent" rather than just history, the final **XGBoost model achieved an ROC-AUC of 0.74**, offering a robust alternative to traditional underwriting.

---

## Key Results & Impact
*   **Model Performance:** 0.744 AUC (XGBoost), outperforming the Random Forest baseline.
*   **Precision (Non-Default):** 0.94 — The model is highly reliable when approving loans.
*   **Risk Identification:** Successfully flagged **70%** of actual defaults in the holdout test set.
*   **Business Insight:** Identified that borrowers with a **Payment-to-Income (PTI) ratio > 15%** carry significantly higher risk, regardless of income level.
  ![ROC](https://github.com/RachaelKilonzo/Credit-Risk-Prediction-Underwriting-Framework/blob/main/roc.png)

---

##  Feature Engineering 
To prevent data leakage and improve predictive power, I moved beyond raw bureau data and engineered synthesized financial metrics:

| Feature | Logic | Why it matters |
| :--- | :--- | :--- |
| **Payment-to-Income (PTI)** | `(Installment / Monthly Income)` | Measures monthly affordability stress. |
| **Credit Utilization Efficiency** | `(Revol Bal / Util Rate)` | Detects reliance on revolving credit for liquidity. |
| **Delinquency Flag** | Binary composite of liens/bankruptcies | Captures historical behavioral patterns. |
| **Employment Stability** | Boolean (`Emp Length > 2 years`) | Proxy for income continuity and job security. |

---

## Visual Analysis
### 1. Risk Drivers
*Exploratory analysis revealing the sharp divergence in PTI and Utilization between compliant borrowers and defaulters.*

![Risk Drivers Visualization](https://github.com/RachaelKilonzo/Credit-Risk-Prediction-Underwriting-Framework/blob/main/drivers.png)
*(Note: Defaulters use 55% of available credit on average, compared to 49% for good borrowers.)*

### 2. Feature Importance
*The top factors driving the XGBoost decision logic.*

![Feature Importance](https://github.com/RachaelKilonzo/Credit-Risk-Prediction-Underwriting-Framework/blob/main/risk%20factor.png)

---

## Model Architecture
*   **Algorithm:** XGBoost Classifier (Gradient Boosting).
*   **Handling Imbalance:** The dataset had an 11.9% default rate. I used `scale_pos_weight` and stratified splitting to manage class imbalance.
*   **Preprocessing Strategy:**
    *   **Temporal Split:** Features were filtered to include *only* data available at the moment of application to prevent data leakage.
    *   **Target Mapping:** 'Charged Off' and 'Default' mapped to `1`; 'Fully Paid' and 'Current' mapped to `0`.

---

>>>>>>> source_repo/main
