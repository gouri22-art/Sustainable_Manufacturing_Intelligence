import streamlit as st
import pandas as pd

def machine_input_form():
    st.subheader("🔧 Machine Operating Parameters")

    col1, col2 = st.columns(2)

    with col1:
        machine_type = st.selectbox("Machine Type", [0, 1, 2])
        air_temp = st.slider("Air temperature [K]", 295, 305, 300)
        process_temp = st.slider("Process temperature [K]", 305, 315, 310)

    with col2:
        rpm = st.slider("Rotational speed [rpm]", 1100, 3000, 1500)
        torque = st.slider("Torque [Nm]", 3, 80, 40)
        tool_wear = st.slider("Tool wear [min]", 0, 250, 50)

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

    return input_df
