import streamlit as st
import pandas as pd

st.title("📊 Manufacturing Data Overview")

@st.cache_data
def load_data():
    return pd.read_csv("../data/processed/manufacturing_processed.csv")

df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head(20))

st.subheader("Key Statistics")
st.write(df.describe())

st.subheader("Machine Failure Distribution")
failure_counts = df["Machine failure"].value_counts()
st.bar_chart(failure_counts)
