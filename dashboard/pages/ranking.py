import streamlit as st
import pandas as pd

st.title("🏆 Machine Sustainability Ranking")

df = pd.read_csv("../data/processed/manufacturing_processed.csv")

# Rank machines
df["Sustainability Rank"] = df["sustainability_score"].rank(
    ascending=False, method="dense"
)

top_n = st.slider("Select number of top machines", 5, 50, 10)

st.subheader(f"Top {top_n} Sustainable Machines")
st.dataframe(
    df.sort_values("Sustainability Rank").head(top_n)
)

st.bar_chart(
    df.sort_values("Sustainability Rank")
      .head(top_n)
      .set_index("Sustainability Rank")["sustainability_score"]
)
