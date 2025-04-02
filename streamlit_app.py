
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Kōra PWI Dashboard", layout="wide")

st.title("🌿 Kōra Peace & Wellbeing Index (PWI)")
st.markdown("A global open-source tool for exploring peace, justice, wellbeing, and sustainability across civilizations.")

# Load default dataset
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df["VI"] = df["Conflicts_per_century"] * df["Deaths_per_conflict"]
    df["SEWI"] = (df["BHW"] + df["EF"] + df["ES"]) / 3
    df["PWI"] = df["SEWI"] / df["VI"]
    df["PWI_scaled"] = df["PWI"] * 1000
    return df

# Load the ancient dataset by default
df = load_data("data/ancient.csv")

# Sidebar filters
st.sidebar.header("🔍 Filter Civilizations")

# Filter: Economic System
econ_filter = st.sidebar.multiselect("💰 Economic System", options=sorted(df["Economic_System"].unique()), default=df["Economic_System"].unique())

# Apply filters
filtered_df = df[df["Economic_System"].isin(econ_filter)]

# Sort by PWI
df_sorted = filtered_df.sort_values(by="PWI_scaled", ascending=False)

# Display Data
st.subheader("📊 Peace & Wellbeing Index (PWI) Table")
st.dataframe(df_sorted[["Civilization", "PWI_scaled", "SEWI", "VI", "Economic_System"]], use_container_width=True)

# Reflection link
st.info(
    "🪞 Struggling to make sense of the rankings?\n\n"
    "You're not alone. [Here's why these results feel wrong — and why that matters.](https://github.com/Kora-Restore/kora-restorative-toolkit/blob/main/docs/why-it-feels-wrong.md)"
)

# Bar Chart
st.subheader("📈 PWI by Civilization")
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.barh(df_sorted["Civilization"], df_sorted["PWI_scaled"], color="skyblue")
ax1.set_xlabel("PWI (scaled x1000)")
ax1.set_title("Peace & Wellbeing Index Ranking")
ax1.invert_yaxis()
st.pyplot(fig1)

# Scatter Plot
st.subheader("⚖️ SEWI vs Violence Index (VI)")
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.scatter(df_sorted["VI"], df_sorted["SEWI"], s=100, color="green")
for i in range(len(df_sorted)):
    ax2.text(df_sorted["VI"].iloc[i] + 100, df_sorted["SEWI"].iloc[i], df_sorted["Civilization"].iloc[i], fontsize=8)
ax2.set_xlabel("Violence Index (VI)")
ax2.set_ylabel("Sustainable & Equitable Wellbeing Index (SEWI)")
ax2.set_title("SEWI vs VI by Civilization")
st.pyplot(fig2)
