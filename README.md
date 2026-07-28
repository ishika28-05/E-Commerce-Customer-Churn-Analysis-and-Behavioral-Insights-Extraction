# 🛒 E-Commerce Customer Churn Analysis & Behavioral Insights

End-to-end data analytics project analyzing customer churn behavior for an e-commerce platform — from raw data to a deployed ML app. The goal: identify key churn drivers, segment customers by behavior, and build a predictive model to flag at-risk accounts for targeted retention.

**🚀 [Try the live app](https://ishika28-05-e-commerce-customer-churn-analysis-pythonapp-uezw94.streamlit.app/)**

---

## 🔧 Tools & Technologies
| Stage | Tool |
|---|---|
| Data Cleaning / ETL | Excel Power Query |
| Exploratory Analysis | MySQL |
| EDA, Segmentation, ML | Python (Pandas, Seaborn, Scikit-learn) |
| Dashboard | Power BI |
| Deployment | Streamlit |

## 🔄 Project Flow
```
Raw Data → Excel Power Query (ETL) → SQL (EDA & Analysis) → Python (RFM + ML) → Power BI (Dashboard) → Streamlit (Deployment)
```

## 📊 Dataset
- **Source:** [E-Commerce Dataset by Anagha Paul](https://www.kaggle.com/) — Kaggle
- **Records:** 5,000+ customer records
- **Features:** 20 columns including tenure, satisfaction score, complaint history, city tier, payment mode, and churn status

---

## 🧹 Phase 1 — Excel Power Query (ETL)
- Handled null values using median imputation across 7 columns
- Removed duplicates and standardized text formatting
- Engineered a `ChurnFlag` column (Churned / Retained)
- Documented all 15+ transformation steps in the Applied Steps panel

## 🗄️ Phase 2 — SQL (MySQL)
- Wrote 20+ queries using `GROUP BY`, `CASE WHEN`, and subqueries
- Used window functions — `DENSE_RANK()`, `PARTITION BY`
- Built CTEs for churn rate analysis by city tier
- Created a stored procedure `GetChurnByCityTier(tier)`
- Created views for reusable churned-customer segments

## 🐍 Phase 3 — Python
- Performed full EDA with 10+ visualizations (Seaborn, Matplotlib)
- Built RFM segmentation classifying customers into 4 segments: **Champion, Loyal, At Risk, Lost**
- Trained Logistic Regression (baseline) and Random Forest classifier
- Achieved **99.9%+ ROC-AUC** with Random Forest
- Identified top 3 churn drivers via feature importance: **Tenure, CashbackAmount, WarehouseToHome**

## 📈 Phase 4 — Power BI
3-page interactive dashboard with custom DAX measures:
- **Page 1 — Overview:** KPI cards, churn distribution, churn by city tier, complaints & payment mode
- **Page 2 — Segment Analysis:** RFM segment breakdown, churn rate by segment, avg tenure & cashback by segment
- **Page 3 — Churn Drivers:** feature importance chart, satisfaction distribution, drill-through by segment
- Slicers for CityTier, ChurnFlag, PaymentMode, and Segment

## 🌐 Phase 5 — Deployment
- Built an interactive **Streamlit app** so anyone can input customer details and get a live churn prediction from the trained Random Forest model
- **[Live app →](https://ishika28-05-e-commerce-customer-churn-analysis-pythonapp-uezw94.streamlit.app/)**

---

## 🎯 Model Performance & Business Interpretation

### Random Forest Classifier Results
- **ROC-AUC Score:** 99.9%
- **5-Fold Cross-Validation Score:** 0.9996 (confirms the score isn't a fluke)
- **Test Set Size:** 1,126 customers

### Why a 99.9% Score Is Legitimate Here
A score this high is normally a red flag for data leakage — so I stress-tested it:
- Plotted feature importances to confirm no single "cheat" column was doing all the work — distribution was healthy, with Tenure and Complaint History leading logically
- Ran 5-fold cross-validation — score held steady at 0.9996 across all folds
- Benchmarked against a shallow Decision Tree (max depth 3), which still hit 87.8% accuracy — confirming the dataset is naturally separable

**Conclusion:** Short-tenure customers who file complaints are highly predictable churn risks, making this a cleanly separable classification problem.

### Confusion Matrix (Test Set: 1,126 customers)
| | Predicted: Stay | Predicted: Leave |
|---|---|---|
| **Actual: Stay** | ✅ True Negative | ❌ 3 False Positives |
| **Actual: Leave** | ❌ 15 False Negatives | ✅ True Positive |

Only **18 total mistakes** out of 1,126 predictions.

### Business Cost of Each Error Type
| Error | Count | Business Impact |
|---|---|---|
| False Positives | 3 | Minor — loyal customers flagged as churners; small wasted retention spend (unnecessary vouchers) |
| False Negatives | 15 | Critical — actual churners missed entirely; full customer lifetime value lost |

**Recommendation:** Since false negatives are far more costly than false positives, the model should be tuned to minimize missed churners — even at the cost of flagging more loyal customers for retention outreach. A discount voucher is always cheaper than losing a customer permanently.

---

## 💡 Key Insights
- **Tenure** is the strongest churn predictor (importance: 0.226) — customers in months 0–2 show near-100% churn, dropping sharply after month 5
- **Cashback Amount** is the 2nd strongest predictor (0.103) — Champions receive avg ₹228 cashback vs. Lost customers at ₹135
- **At Risk** segment has the highest churn rate (~18%) despite being 24.56% of the customer base — highest-priority retention target
- **WarehouseToHome** (delivery distance) ranks 3rd (0.073) — a silent but significant churn driver
- Debit Card users have the highest volume and notable churn; UPI/E-wallet users churn less
- **Complaints** rank 6th — a symptom of poor delivery/low cashback rather than a root cause
- 60.64% of customers are in the Loyal segment — the base is fundamentally healthy, making At Risk intervention highly cost-effective

---

## 📁 Repo Structure
```
├── data/          # Raw & cleaned datasets
├── sql/           # MySQL queries, stored procedures, views
├── python/         
│   ├── app.py             # Streamlit app
│   ├── churn_model.pkl    # Trained Random Forest model
│   └── requirements.txt
├── powerbi/       # Power BI dashboard file
└── README.md
```

## ▶️ Run Locally
```bash
git clone https://github.com/ishika28-05/E-Commerce-Customer-Churn-Analysis-and-Behavioral-Insights-Extraction.git
cd E-Commerce-Customer-Churn-Analysis-and-Behavioral-Insights-Extraction/python
pip install -r requirements.txt
streamlit run app.py
```

## 🔮 Future Improvements
- Add SHAP explainability so predictions come with a "why" for each customer
- Experiment with XGBoost / ensemble stacking to compare against Random Forest
- Add model monitoring for performance drift on new data

---
**Author:** Ishika | [LinkedIn](# 🛒 E-Commerce Customer Churn Analysis & Behavioral Insights

End-to-end data analytics project analyzing customer churn behavior for an e-commerce platform — from raw data to a deployed ML app. The goal: identify key churn drivers, segment customers by behavior, and build a predictive model to flag at-risk accounts for targeted retention.

**🚀 [Try the live app](https://ishika28-05-e-commerce-customer-churn-analysis-pythonapp-uezw94.streamlit.app/)**

![App Screenshot](screenshot.png)
<!-- Replace screenshot.png with your actual screenshot filename after uploading it -->

---

## 🔧 Tools & Technologies
| Stage | Tool |
|---|---|
| Data Cleaning / ETL | Excel Power Query |
| Exploratory Analysis | MySQL |
| EDA, Segmentation, ML | Python (Pandas, Seaborn, Scikit-learn) |
| Dashboard | Power BI |
| Deployment | Streamlit |

## 🔄 Project Flow
```
Raw Data → Excel Power Query (ETL) → SQL (EDA & Analysis) → Python (RFM + ML) → Power BI (Dashboard) → Streamlit (Deployment)
```

## 📊 Dataset
- **Source:** [E-Commerce Dataset by Anagha Paul](https://www.kaggle.com/) — Kaggle
- **Records:** 5,000+ customer records
- **Features:** 20 columns including tenure, satisfaction score, complaint history, city tier, payment mode, and churn status

---

## 🧹 Phase 1 — Excel Power Query (ETL)
- Handled null values using median imputation across 7 columns
- Removed duplicates and standardized text formatting
- Engineered a `ChurnFlag` column (Churned / Retained)
- Documented all 15+ transformation steps in the Applied Steps panel

## 🗄️ Phase 2 — SQL (MySQL)
- Wrote 20+ queries using `GROUP BY`, `CASE WHEN`, and subqueries
- Used window functions — `DENSE_RANK()`, `PARTITION BY`
- Built CTEs for churn rate analysis by city tier
- Created a stored procedure `GetChurnByCityTier(tier)`
- Created views for reusable churned-customer segments

## 🐍 Phase 3 — Python
- Performed full EDA with 10+ visualizations (Seaborn, Matplotlib)
- Built RFM segmentation classifying customers into 4 segments: **Champion, Loyal, At Risk, Lost**
- Trained Logistic Regression (baseline) and Random Forest classifier
- Achieved **99.9%+ ROC-AUC** with Random Forest
- Identified top 3 churn drivers via feature importance: **Tenure, CashbackAmount, WarehouseToHome**

## 📈 Phase 4 — Power BI
3-page interactive dashboard with custom DAX measures:
- **Page 1 — Overview:** KPI cards, churn distribution, churn by city tier, complaints & payment mode
- **Page 2 — Segment Analysis:** RFM segment breakdown, churn rate by segment, avg tenure & cashback by segment
- **Page 3 — Churn Drivers:** feature importance chart, satisfaction distribution, drill-through by segment
- Slicers for CityTier, ChurnFlag, PaymentMode, and Segment

## 🌐 Phase 5 — Deployment
- Built an interactive **Streamlit app** so anyone can input customer details and get a live churn prediction from the trained Random Forest model
- **[Live app →](https://ishika28-05-e-commerce-customer-churn-analysis-pythonapp-uezw94.streamlit.app/)**

---

## 🎯 Model Performance & Business Interpretation

### Random Forest Classifier Results
- **ROC-AUC Score:** 99.9%
- **5-Fold Cross-Validation Score:** 0.9996 (confirms the score isn't a fluke)
- **Test Set Size:** 1,126 customers

### Why a 99.9% Score Is Legitimate Here
A score this high is normally a red flag for data leakage — so I stress-tested it:
- Plotted feature importances to confirm no single "cheat" column was doing all the work — distribution was healthy, with Tenure and Complaint History leading logically
- Ran 5-fold cross-validation — score held steady at 0.9996 across all folds
- Benchmarked against a shallow Decision Tree (max depth 3), which still hit 87.8% accuracy — confirming the dataset is naturally separable

**Conclusion:** Short-tenure customers who file complaints are highly predictable churn risks, making this a cleanly separable classification problem.

### Confusion Matrix (Test Set: 1,126 customers)
| | Predicted: Stay | Predicted: Leave |
|---|---|---|
| **Actual: Stay** | ✅ True Negative | ❌ 3 False Positives |
| **Actual: Leave** | ❌ 15 False Negatives | ✅ True Positive |

Only **18 total mistakes** out of 1,126 predictions.

### Business Cost of Each Error Type
| Error | Count | Business Impact |
|---|---|---|
| False Positives | 3 | Minor — loyal customers flagged as churners; small wasted retention spend (unnecessary vouchers) |
| False Negatives | 15 | Critical — actual churners missed entirely; full customer lifetime value lost |

**Recommendation:** Since false negatives are far more costly than false positives, the model should be tuned to minimize missed churners — even at the cost of flagging more loyal customers for retention outreach. A discount voucher is always cheaper than losing a customer permanently.

---

## 💡 Key Insights
- **Tenure** is the strongest churn predictor (importance: 0.226) — customers in months 0–2 show near-100% churn, dropping sharply after month 5
- **Cashback Amount** is the 2nd strongest predictor (0.103) — Champions receive avg ₹228 cashback vs. Lost customers at ₹135
- **At Risk** segment has the highest churn rate (~18%) despite being 24.56% of the customer base — highest-priority retention target
- **WarehouseToHome** (delivery distance) ranks 3rd (0.073) — a silent but significant churn driver
- Debit Card users have the highest volume and notable churn; UPI/E-wallet users churn less
- **Complaints** rank 6th — a symptom of poor delivery/low cashback rather than a root cause
- 60.64% of customers are in the Loyal segment — the base is fundamentally healthy, making At Risk intervention highly cost-effective

---

## 📁 Repo Structure
```
├── data/          # Raw & cleaned datasets
├── sql/           # MySQL queries, stored procedures, views
├── python/         
│   ├── app.py             # Streamlit app
│   ├── churn_model.pkl    # Trained Random Forest model
│   └── requirements.txt
├── powerbi/       # Power BI dashboard file
└── README.md
```

## ▶️ Run Locally
```bash
git clone https://github.com/ishika28-05/E-Commerce-Customer-Churn-Analysis-and-Behavioral-Insights-Extraction.git
cd E-Commerce-Customer-Churn-Analysis-and-Behavioral-Insights-Extraction/python
pip install -r requirements.txt
streamlit run app.py
```

## 🔮 Future Improvements
- Add SHAP explainability so predictions come with a "why" for each customer
- Experiment with XGBoost / ensemble stacking to compare against Random Forest
- Add model monitoring for performance drift on new data

---
**Author:** Ishika | [LinkedIn](www.linkedin.com/in/ishika-mittal-100747363)
