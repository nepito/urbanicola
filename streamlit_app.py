import requests
import json
import pandas as pd
import streamlit as st

name = st.text_input(
    "Por favor agrega un nombre",
    placeholder="Nombre",
)
age = st.number_input("Agrega una edad por favor", min_value=18, max_value=65)
client = st.checkbox("Cliente")
url = "http://104.248.109.197:6868/v1/item"


def make_user(nombre, edad, es_cliente):
    return {"name": [nombre], "age": [edad], "client": [es_cliente]}


headers = {"Content-type": "application/json"}

if st.button("Make post request"):
    st.write(requests.post(url, json=make_user(name, age, client), headers=headers))

conn = requests.get("http://104.248.109.197:6868/v1/gastos")
gastos = pd.DataFrame.from_dict(json.loads(conn.json()))

st.write(gastos)

st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
