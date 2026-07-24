# E-Commerce-Customer-Churn-Analysis-and-Behavioral-Insights-Extraction
## Overview
End-to-end data analytics project analyzing customer churn behavior for an e-commerce platform. The goal was to identify key churn drivers, segment customers by behavior and build a predictive model to flag at-risk accounts — enabling targeted retention strategies.
## Tools and Technologies
Excel Power Query - Data Cleaning and ETL
MySQL - Exploratory queries and business insights
Python - EDA, RFM Segmentation and ML modelling
Power BI - Interactive dashboard and visualisation
## Project Flow
Raw Data → Excel Power Query (ETL) → SQL (EDA & Analysis) → Python (RFM + ML) → Power BI (Dashboard)
## Dataset
- Source: E-Commerce Dataset by Anagha Paul — Kaggle
- Records: 5,000+ customer records
- Features: 20 columns including tenure, satisfaction score, complaint history, city tier, payment mode and churn status
## What I Did
### Phase 1 — Excel Power Query (ETL)
- Handled null values using median imputation for 7 columns
- Removed duplicates and standardized text formatting
- Engineered ChurnFlag column (Churned/Retained) 
- Documented all 15+ transformation steps in Applied Steps panel
### Phase 2 — SQL (MySQL)
- Wrote 20+ queries using GROUP BY, CASE WHEN, subqueries
- Used window functions — DENSE_RANK(), PARTITION BY
- Built CTEs for churn rate analysis by city tier
- Created stored procedure GetChurnByCityTier(tier)
- Created views for reusable churned customer segments
### Phase 3 — Python
- Performed full EDA with 10+ visualizations using Seaborn and Matplotlib
- Built RFM segmentation classifying customers into 4 segments: Champion, Loyal, At Risk and Lost
- Trained Logistic Regression (baseline) and Random Forest classifier
- Achieved 99.9%+ ROC-AUC score with Random Forest
- Identified top 3 churn drivers: Tenure, CashbackAmount, WarehouseToHome via feature importance
### Phase 4 — Power BI
- Built 3-page interactive dashboard using custom DAX measures
- Page 1: Overview — KPI cards, churn distribution, churn by city tier, complaint and payment mode
- Page 2: Segment Analysis — RFM segment breakdown, churn rate by segment, avg tenure and cashback by segment
- Page 3: Churn Drivers — feature importance chart, satisfaction distribution, drill-through by segment
- Added slicers for CityTier, ChurnFlag, PaymentMode and Segment
## Model Performance & Business Interpretation
### Random Forest Classifier Results
- **ROC-AUC Score: 99.9%**
- **5-Fold Cross-Validation Score: 0.9996** (confirms score is not a fluke)
- **Test Set Size: 1,126 customers**
### Why a 99.9% Score is Legitimate Here
A score this high is normally a red flag for data leakage — so I stress-tested it:
- Plotted feature importances to ensure no single "cheat" column was doing all the work — distribution was healthy, with Tenure and Complaint History leading logically
- Ran 5-fold Cross-Validation — score held steady at 0.9996 across all folds
- Benchmarked against a shallow Decision Tree (max depth 3) which still achieved 87.8% accuracy — confirming the dataset is naturally separable
**Conclusion:** Short-tenure customers who file complaints are highly predictable churn risks, making this a cleanly separable classification problem.
### Confusion Matrix Breakdown
| | Predicted: Stay | Predicted: Leave |
| **Actual: Stay** | ✅ True Negative | ❌ False Positive (3) |
| **Actual: Leave** | ❌ False Negative (15) | ✅ True Positive |
**Out of 1,126 test customers, the model only made 18 mistakes total.**
### Business Cost of Each Error Type
| Error | Count | Business Impact |
| False Positives | 3 | Minor — loyal customers incorrectly flagged as churners, may waste small retention budget sending unnecessary discount vouchers |
| False Negatives | 15 | Critical — actual churners missed entirely, these customers walk out the door without any retention attempt, losing their full lifetime revenue |
### Business Recommendation
Since False Negatives are far more costly than False Positives, the model should be tuned to minimize missed churners even if it means flagging slightly more loyal customers for retention outreach. The cost of a discount voucher is always lower than the cost of losing a customer permanently.
## Key Insights
- Tenure is the single strongest churn predictor (importance: 0.226) — customers in their first 0-2 months show nearly 100% churn rate, dropping sharply after 5 months
- Cashback Amount is the 2nd strongest predictor (0.103) — Champion customers receive avg ₹228 cashback vs Lost customers at ₹135, suggesting cashback directly drives retention
- At Risk segment has the highest churn rate (~18%) among all RFM segments despite representing 24.56% of the customer base — making it the highest priority for retention campaigns
- Delivery distance (WarehouseToHome) ranked 3rd in feature importance (0.073) — a silent but significant churn driver often overlooked by businesses
- Debit Card users have the highest customer volume but also show notable churn — UPI and E-wallet users show comparatively lower churn rates
- Complaints ranked 6th in feature importance — they are a symptom of poor delivery experience and low cashback rather than the root cause of churn
- 60.64% of customers fall in the Loyal segment — the customer base is fundamentally healthy, making At Risk intervention highly cost-effective
