
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Kōra PWI Timeline", layout="wide")
st.title("🌍 Kōra Peace & Wellbeing Index (PWI)")
st.markdown("Explore the Peace & Wellbeing Index across time — from ancient civilizations to future visions.")

# Map of available datasets
dataset_options = {
    "Ancient (Pre-500 CE)": "data/ancient.csv",
    "Medieval (500–1500 CE)": "data/medieval.csv",
    "Modern (1500–2000 CE)": "data/modern.csv",
    "Contemporary (2000–2025)": "data/contemporary.csv",
    "Forecast – Current Trajectory (2025–2075)": "data/forecast_realistic.csv",
    "Forecast – Long Term (Next 500 yrs)": "data/forecast_longterm.csv",
    "Forecast – Kōra Vision (2075+)": "data/kora_vision.csv"
}

# Dataset selector
dataset_name = st.sidebar.selectbox("📂 Select Dataset", list(dataset_options.keys()))
file_path = dataset_options[dataset_name]

@st.cache_data
def load_and_process(file_path):
    df = pd.read_csv(file_path, comment="#")
    df["VI"] = df["Conflicts_per_century"] * df["Deaths_per_conflict"]
    df["SEWI"] = (df["BHW"] + df["EF"] + df["ES"]) / 3
    df["PWI"] = df["SEWI"] / df["VI"]
    df["PWI_scaled"] = df["PWI"] * 1000
    return df

df = load_and_process(file_path)

# Optional filters
with st.sidebar.expander("🔍 Optional Filters"):
    if "Economic_System" in df.columns:
        econ = st.multiselect("💰 Economic System", df["Economic_System"].unique(), default=df["Economic_System"].unique())
        df = df[df["Economic_System"].isin(econ)]

# Display Table
st.subheader(f"📊 PWI Table – {dataset_name}")
st.dataframe(df[["Civilization", "PWI_scaled", "SEWI", "VI", "Economic_System"]], use_container_width=True)

# Info link for reflection
if "ancient" in file_path or "forecast" in file_path:
    st.info(
        "🪞 Struggling with what you see? [Read why this might feel wrong.](https://github.com/Kora-Restore/kora-restorative-toolkit/blob/main/docs/why-it-feels-wrong.md)"
    )

# Bar Chart
st.subheader("📈 PWI (scaled) by Civilization")
df_sorted = df.sort_values("PWI_scaled", ascending=False)
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.barh(df_sorted["Civilization"], df_sorted["PWI_scaled"], color="skyblue")
ax1.set_xlabel("PWI (scaled x1000)")
ax1.set_title("Peace & Wellbeing Index Ranking")
ax1.invert_yaxis()
st.pyplot(fig1)

# Scatter Plot
st.subheader("⚖️ SEWI vs Violence Index (VI)")
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.scatter(df["VI"], df["SEWI"], s=100, color="green")
for i in range(len(df)):
    ax2.text(df["VI"].iloc[i] + 100, df["SEWI"].iloc[i], df["Civilization"].iloc[i], fontsize=8)
ax2.set_xlabel("Violence Index (VI)")
ax2.set_ylabel("Sustainable & Equitable Wellbeing Index (SEWI)")
ax2.set_title("SEWI vs VI")
st.pyplot(fig2)
