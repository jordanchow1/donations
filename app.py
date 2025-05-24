import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Setup
st.set_page_config(page_title="Donation Analysis", layout="wide")
st.title("📊 Donation Data Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("sample_donations.csv")
    df['donation_date'] = pd.to_datetime(df['donation_date'])
    df_cleaned = df.dropna(subset=['donor_id', 'donation_amount'])
    df_cleaned['month'] = df_cleaned['donation_date'].dt.to_period('M')
    return df, df_cleaned

df, df_cleaned = load_data()

# Sidebar
st.sidebar.header("Filters")
selected_campaign = st.sidebar.multiselect("Campaign(s):", options=df_cleaned['campaign'].unique(),
                                           default=df_cleaned['campaign'].unique())

filtered_df = df_cleaned[df_cleaned['campaign'].isin(selected_campaign)]

# Row 1: Missing Values
st.subheader("Missing Values Summary")
missing_values = df[['donor_id', 'donation_amount']].isnull().sum()
st.dataframe(missing_values.to_frame(name="Missing Count"))

# Row 2: Campaign Totals
st.subheader("Top Campaigns by Total Donations")
campaign_totals = filtered_df.groupby("campaign")["donation_amount"].sum().sort_values(ascending=False)

fig1, ax1 = plt.subplots()
sns.barplot(x=campaign_totals.values, y=campaign_totals.index, ax=ax1, palette="viridis")
ax1.set_title("Total Donation Amount per Campaign")
ax1.set_xlabel("Total Amount")
st.pyplot(fig1)

# Row 3: Average Donation Distribution
st.subheader("Average Donation per Donor (Histogram)")
avg_donation = filtered_df.groupby("donor_id")["donation_amount"].mean()

fig2, ax2 = plt.subplots()
sns.histplot(avg_donation, kde=True, bins=20, ax=ax2)
ax2.set_title("Distribution of Average Donations")
ax2.set_xlabel("Avg Donation Amount")
st.pyplot(fig2)

# Row 4: Monthly Volume
st.subheader("Monthly Donation Volume")
monthly_counts = filtered_df.groupby('month').size()

fig3, ax3 = plt.subplots()
monthly_counts.plot(kind='line', marker='o', ax=ax3, color='teal')
ax3.set_title("Number of Donations per Month")
ax3.set_xlabel("Month")
ax3.set_ylabel("Donation Count")
st.pyplot(fig3)

# Row 5: Campaigns Over Time
st.subheader("Campaign Donations Over Time (Stacked Area)")
monthly_campaigns = filtered_df.groupby(['month', 'campaign']).size().unstack(fill_value=0)

fig4, ax4 = plt.subplots(figsize=(10, 6))
monthly_campaigns.plot.area(ax=ax4, colormap='tab20')
ax4.set_title("Donations by Campaign Over Time")
ax4.set_xlabel("Month")
ax4.set_ylabel("Donations")
st.pyplot(fig4)