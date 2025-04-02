
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Kōra – Global Timeline", layout="wide")
st.title("🌍 Kōra: Peace & Wellbeing Index – Global Timeline")

@st.cache_data
def load_data():
    df = pd.read_csv("data/global_timeline.csv")
    df["VI"] = df["Conflicts_per_century"] * df["Deaths_per_conflict"]
    df["SEWI"] = (df["BHW"] + df["EF"] + df["ES"]) / 3
    df["PWI"] = df["SEWI"] / df["VI"]
    df["PWI_scaled"] = df["PWI"] * 1000
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filters")

# Year range filtering
year_min, year_max = int(df["Year_From"].min()), int(df["Year_To"].max())
year_range = st.sidebar.slider("Select Year Range", min_value=year_min, max_value=year_max, value=(2025, 2075))
start_year, end_year = year_range
filtered_df = df[(df["Year_From"] <= end_year) & (df["Year_To"] >= start_year)]

# Period filter
periods = st.sidebar.multiselect("Period", options=df["Period"].unique(), default=df["Period"].unique())
filtered_df = filtered_df[filtered_df["Period"].isin(periods)]

# Optional advanced filters
with st.sidebar.expander("⚙️ Advanced Filters"):
    if "Economic_System" in df.columns:
        econ = st.multiselect("💰 Economic System", df["Economic_System"].unique(), default=df["Economic_System"].unique())
        filtered_df = filtered_df[filtered_df["Economic_System"].isin(econ)]
    if "Governance_Model" in df.columns:
        gov = st.multiselect("🏛 Governance Model", df["Governance_Model"].unique(), default=df["Governance_Model"].unique())
        filtered_df = filtered_df[filtered_df["Governance_Model"].isin(gov)]

# Display Data Table
st.subheader(f"📋 Civilizations active between {start_year} and {end_year}")
st.dataframe(filtered_df[["Civilization", "Period", "PWI_scaled", "SEWI", "VI", "Region"]], use_container_width=True)

# PWI Bar Chart
st.subheader("📈 Peace & Wellbeing Index (scaled)")
df_sorted = filtered_df.sort_values("PWI_scaled", ascending=False)
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.barh(df_sorted["Civilization"], df_sorted["PWI_scaled"], color="skyblue")
ax1.set_xlabel("PWI (scaled x1000)")
ax1.set_title("PWI by Civilization")
ax1.invert_yaxis()
st.pyplot(fig1)

# SEWI vs VI Scatter Plot
st.subheader("⚖️ SEWI vs Violence Index")
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.scatter(filtered_df["VI"], filtered_df["SEWI"], s=100, color="green")
for i in range(len(filtered_df)):
    ax2.text(filtered_df["VI"].iloc[i] + 100, filtered_df["SEWI"].iloc[i], filtered_df["Civilization"].iloc[i], fontsize=8)
ax2.set_xlabel("Violence Index (VI)")
ax2.set_ylabel("Sustainable & Equitable Wellbeing Index (SEWI)")
ax2.set_title("SEWI vs VI Scatter")
st.pyplot(fig2)

# Reminder
if end_year > 2025:
    st.info("🧭 You're exploring future trajectories. Results are scenario-based forecasts.")
elif end_year < 1500:
    st.warning("🏺 This range includes ancient or medieval estimates. Values are interpretative models.")
