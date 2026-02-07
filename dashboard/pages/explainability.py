import streamlit as st
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt

st.title("🧠 Explainable AI – Feature Importance")

model = joblib.load("../models/rf_model.pkl")
df = pd.read_csv("../data/processed/manufacturing_processed.csv")

X = df.drop("Machine failure", axis=1)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

st.subheader("Global Feature Importance")

fig, ax = plt.subplots()
shap.summary_plot(shap_values[1], X, show=False)
st.pyplot(fig)
