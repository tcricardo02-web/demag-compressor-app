import streamlit as st
import pandas as pd
import numpy as np

st.title("Demag Compressor Performance App")
unit_system = st.selectbox("Selecione o sistema de unidades", ["Métrico (SI)", "Imperial (Oil & Gas)"])

flow = st.number_input("Vazão", value=300.0)
pressure_in = st.number_input("Pressão de entrada", value=1.0)
pressure_out = st.number_input("Pressão de saída", value=5.0)

power_kw = (pressure_out - pressure_in) * flow * 0.05
if unit_system == "Imperial (Oil & Gas)":
    power_hp = power_kw * 1.34102
    st.write(f"Potência: {power_hp:.2f} HP")
else:
    st.write(f"Potência: {power_kw:.2f} kW")

# Exemplo de curva
df = pd.DataFrame({
    "Flow": np.linspace(100, 500, 5),
    "Power": np.linspace(200, 600, 5)
})
st.line_chart(df.set_index("Flow"))
