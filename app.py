
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Oilfield Simulator 2.0",
    page_icon="🛢️",
    layout="wide"
)

st.title("🛢️ Oilfield Simulator 2.0")
st.subheader("Integrated Reservoir, Drilling & Production Simulator")

st.sidebar.header("Simulation Controls")

porosity = st.sidebar.slider(
    "Reservoir Porosity (%)", 5, 35, 20
)

permeability = st.sidebar.slider(
    "Permeability (mD)", 1, 2000, 150
)

reservoir_pressure = st.sidebar.slider(
    "Initial Reservoir Pressure (psi)", 500, 10000, 3500
)

oil_rate = st.sidebar.number_input(
    "Initial Oil Production (bbl/day)", 100, 50000, 5000
)

decline_rate = st.sidebar.slider(
    "Annual Decline Rate (%)", 1, 50, 12
)

drilling_cost = st.sidebar.number_input(
    "Drilling Cost ($)", 100000, 20000000, 5000000
)

st.header("1. Reservoir Simulation")

st.metric("Porosity", f"{porosity}%")
st.metric("Permeability", f"{permeability} mD")
st.metric("Initial Pressure", f"{reservoir_pressure:,} psi")

st.header("2. Drilling Simulation")

st.metric("Estimated Drilling Cost", f"${drilling_cost:,.0f}")

days = np.arange(0, 3651, 30)

st.header("3. Production Forecast")

daily_rate = oil_rate * np.exp(
    -(decline_rate / 100) * days / 365
)

production = pd.DataFrame({
    "Day": days,
    "Oil Production (bbl/day)": daily_rate
})

st.line_chart(
    production.set_index("Day")
)

total_oil = np.trapezoid(daily_rate, days)

st.metric(
    "Estimated 10-Year Oil Recovery",
    f"{total_oil:,.0f} barrels"
)

st.header("4. Production Data")

st.dataframe(production, use_container_width=True)

st.success("Simulation completed successfully!")

st.caption(
    "Educational engineering model. "
    "Not validated for operational drilling or reservoir decisions."
)
