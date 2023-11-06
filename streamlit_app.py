import requests
import json
import pandas as pd
import streamlit as st


conn = requests.get("http://104.248.109.197:6868/v1/gastos")
gastos = pd.DataFrame.from_dict(json.loads(conn.json()))

st.write(gastos)

st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
