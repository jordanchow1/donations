# 🧾 Donations Analytics Dashboard

A donation data analytics project that combines data cleaning, exploratory data analysis, interactive dashboards, donor segmentation, and predictive modeling using Python, Pandas, Streamlit, and Scikit-learn.

## 📊 Overview

This project analyzes a fictional dataset of donation transactions. It was designed to simulate real-world nonprofit analytics tasks such as:

- Identifying top-performing campaigns
- Understanding donor behaviour
- Visualizing donation trends over time
- Segmenting donors using clustering

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
- **Donor Behaviour**: Donors vary widely in behaviour—some give small frequent donations, while others contribute large one-time amounts.
- **Monthly Trends**: Donation volume peaked in November and December, indicating strong seasonal giving behaviour near the end of the year.
- **Clustering**: K-Means segmentation revealed three donor types:
  - **Cluster 0**: Infrequent, low-value donors
  - **Cluster 1**: Consistent mid-range donors
  - **Cluster 2**: High-value, highly engaged donors
 
## 📌 Recommendations

Based on the findings, the following strategies are suggested:

- Focus on High-Value Donors: Prioritize marketing and stewardship efforts for Cluster 2 to increase giving.
- Re-engage Low-Activity Donors: Target Cluster 0 with personalized campaigns or incentives.
- Optimize Campaign Portfolio: Scale high-performing campaigns and revise or sunset underperformers.
- Leverage Seasonal Trends: Plan fundraising drives in Q4 to align with peak giving periods.
- Use Predictive Insights: Apply the donation model to forecast and nurture high-potential donors.
