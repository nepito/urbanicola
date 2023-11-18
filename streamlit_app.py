import requests
import json
import pandas as pd
import streamlit as st
import datetime


url = "http://104.248.109.197:6868/v1/spent"

col1, col2, col3 = st.columns(3)
with col1:
    date = st.date_input("Fecha", value=None)
with col2:
    mount = st.number_input("Agrega el monto", min_value=0.1)
    how_many = st.number_input("Cantidad", min_value=0.1)
with col3:
    type = st.selectbox('Tipo de gasto',("Fijo", "Variable"))
colA, colB, colC = st.columns(3)
with colA:
    concept = st.selectbox('Concepto',("Administrativos", "Costos", "Otros"))
with colB:
    subtype = st.selectbox("Subtipo", ("Gasolina hilux", "comida", "Personal", "riego"))
with colC:
    area = st.selectbox("Área", ("Obra", "Proyectos", "Dirección", "Inversiones"))
colI, colII = st.columns(2)
with colI:
    provider = st.selectbox("Proveedor", ("Arco", "Oxxo", "Toyota", "Otros"))
with colII:
    factura = st.checkbox("Factura")
cola, colb = st.columns(2)
with cola:
    payment_type = st.selectbox("Forma de pago", ("Transferencia", "Efectivo"))
with colb:
    bank_count = st.selectbox("Cuenta", ("Santander", "Efectivo"))
description = st.text_input(
    "Por favor la descripción de gasto",
    placeholder="descripción",
)


def make_spent(fecha, monto, tipo, concepto, subtipo, area, cantidad, proveedor, factura, tipo_pago, cuenta, descripcion):
    return {
        "date": [str(fecha)],
        "mount": [monto],
        "type": [tipo],
        "concept": [concepto],
        "subtype": [subtipo],
        "area": [area],
        "how_many": [cantidad],
        "provider": [proveedor],
        "factura": [factura],
        "payment_type": [tipo_pago],
        "bank_count": [cuenta],
        "description": [descripcion]
    }


headers = {"Content-type": "application/json"}

if st.button("Registrar gasto"):
    st.write(str(date), mount, type, concept, subtype, area, how_many, provider, factura, payment_type, bank_count, description)
    st.write(
        requests.post(
            url,
            json=make_spent(date, mount, type, concept, subtype, area, how_many, provider, factura, payment_type, bank_count, description),
            headers=headers)
            )


st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
