import streamlit as st
import pandas as pd

st.set_page_config(page_title="Traffic Violations Dashboard", layout="wide")

st.title("🚦 Traffic Violations Insight System")
st.write("Dashboard loading… please wait ⏳")

@st.cache_data
def load_data():
    return pd.read_csv("traffic_violations_cleaned.csv", nrows=200000)

df = load_data()

st.success("Data loaded successfully")

# Sidebar filter
st.sidebar.header("Filters")
gender = st.sidebar.selectbox(
    "Select Gender",
    ["All"] + sorted(df["Gender"].dropna().unique().tolist())
)

if gender != "All":
    df = df[df["Gender"] == gender]

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Violations (sample)", len(df))
col2.metric("Accidents", df["Accident"].sum() if "Accident" in df.columns else 0)
col3.metric("Fatal Cases", df["Fatal"].sum() if "Fatal" in df.columns else 0)

# Charts
st.subheader("Top Violation Types")
st.bar_chart(df["Violation Type"].value_counts().head(10))

st.subheader("Violations by Hour")
df["Stop_Timestamp"] = pd.to_datetime(df["Stop_Timestamp"])
df["Hour"] = df["Stop_Timestamp"].dt.hour
st.line_chart(df["Hour"].value_counts().sort_index())
