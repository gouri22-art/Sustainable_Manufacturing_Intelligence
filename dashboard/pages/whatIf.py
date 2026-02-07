import streamlit as st
import joblib
import pandas as pd

st.title("🔮 What-If Simulation")

model = joblib.load("../models/rf_model.pkl")

st.subheader("Adjust Machine Parameters")

air_temp = st.slider("Air temperature [K]", 295, 305, 300)
process_temp = st.slider("Process temperature [K]", 305, 315, 310)
rpm = st.slider("Rotational speed [rpm]", 1100, 3000, 1500)
torque = st.slider("Torque [Nm]", 3, 80, 40)
tool_wear = st.slider("Tool wear [min]", 0, 250, 50)
machine_type = st.selectbox("Machine Type", [0, 1, 2])

input_df = pd.DataFrame([[
    machine_type,
    air_temp,
    process_temp,
    rpm,
    torque,
    tool_wear
]], columns=[
    "Type",
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
])

if st.button("Predict Machine Failure"):
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("⚠️ High risk of Machine Failure")
    else:
        st.success("✅ Machine operating normally")
