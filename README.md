# 🧾 Donations Analytics Dashboard

A donation data analytics project that combines data cleaning, exploratory data analysis, interactive dashboards, donor segmentation, and predictive modeling using Python, Pandas, Streamlit, and Scikit-learn.

## 📊 Overview

This project analyzes a fictional dataset of donation transactions. It was designed to simulate real-world nonprofit analytics tasks such as:

- Identifying top-performing campaigns
- Understanding donor behavior
- Visualizing donation trends over time
- Segmenting donors using clustering
- Predicting future donation potential

The app is built with **Streamlit** and provides interactive visualizations and exportable insights for campaign managers and analysts.

---

## 🗂️ Features

### 📈 Streamlit Dashboard
- Missing value inspection  
- Campaign performance tracking  
- Monthly donation trends  
- Distribution of average donation per donor  
- Stacked area chart for donations over time

### 🤖 Machine Learning
- **K-Means clustering** for donor segmentation (RFM-based)  
- **Random Forest regression** to predict total donation potential

## 🧠 Findings

Key insights from the donation dataset include:

- **Campaign Effectiveness**: A small number of campaigns generated the majority of donations, suggesting focused fundraising drives were most successful.
- **Donor Behavior**: Donors vary widely in behavior—some give small frequent donations, while others contribute large one-time amounts.
- **Monthly Trends**: Donation volume peaked in November and December, indicating strong seasonal giving behavior near the end of the year.
- **Clustering**: K-Means segmentation revealed three donor types:
  - **Cluster 0**: Infrequent, low-value donors
  - **Cluster 1**: Consistent mid-range donors
  - **Cluster 2**: High-value, highly engaged donors
 
## 📌 Recommendations

Based on the findings, the following strategies are suggested:

- **Prioritize High-Value Donors**: Focus marketing and stewardship efforts on Cluster 2 donors (high-value and loyal) to encourage continued and increased giving.
- **Reactivate Low-Engagement Donors**: Create re-engagement campaigns for Cluster 0 with personalized messages or small incentives.
- **Campaign Optimization**: Invest more in the top-performing campaigns identified in the analysis and consider discontinuing or revising underperforming ones.
- **Leverage Seasonality**: Plan major fundraising pushes in Q4 (October–December) to capitalize on donor generosity during the holiday season.
- **Predictive Targeting**: Use the donation prediction model to forecast high-potential donors and proactively allocate resources to cultivate them.
