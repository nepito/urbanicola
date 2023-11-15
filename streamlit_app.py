import requests
import json
import pandas as pd
import streamlit as st
import datetime


name = st.text_input(
    "Por favor agrega un nombre",
    placeholder="Nombre",
)
age = st.number_input("Agrega una edad por favor", min_value=18, max_value=65)
client = st.checkbox("Cliente")
url = "http://104.248.109.197:6868/v1/item"

date = st.date_input("Fecha", value=None)
mount = st.number_input("Agrega el monto", min_value=0.1)
type = st.selectbox('Tipo de gasto',("Fijo", "Variable"))
concept = st.selectbox('Concepto',("Administrativos", "Costos", "Otros"))
subtype = st.selectbox("Subtipo", ("Gasolina hilux", "comida", "Personal", "riego"))
area = st.selectbox("Área", ("Obra", "Proyectos", "Dirección", "Inversiones"))
how_many = st.number_input("Cantidad", min_value=0.1)
provider = st.selectbox("Proveedor", ("Arco", "Oxxo", "Toyota", "Otros"))
factura = st.checkbox("Factura")
type_pay = st.selectbox("Forma de pago", ("Transferencia", "Efectivo"))
bank_count = st.selectbox("Cuenta", ("Santander", "Efectivo"))
description = st.text_input(
    "Por favor la descripción de gasto",
    placeholder="descripción",
)


def make_spent(fecha, monto, tipo, concepto, subtipo, area, cantidad, proveedor, factura, tipo_pago, cuenta, descripcion):
    return {
        "date": [fecha],
        "mount": [monto],
        "type": [tipo],
        "concept": [concepto],
        "subtype": [subtipo],
        "area": [area],
        "how_many": [cantidad],
        "provider": [proveedor],
        "factura": [factura],
        "pay_type": [tipo_pago],
        "bank_count": [cuenta],
        "descrption": [descripcion],
    }


def make_user(nombre, edad, es_cliente):
    return {"name": [nombre], "age": [edad], "client": [es_cliente]}


headers = {"Content-type": "application/json"}

if st.button("Make post request"):
#    st.write(requests.post(url, json=make_user(name, age, client), headers=headers))
    st.write(date, mount, type, concept, subtype, area, how_many, provider, factura, type_pay, bank_count, description)

conn = requests.get("http://104.248.109.197:6868/v1/gastos")
gastos = pd.DataFrame.from_dict(json.loads(conn.json()))

st.write(gastos)

st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
