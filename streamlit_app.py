import requests
import pandas as pd
import streamlit as st
from PIL import Image
from pathlib import Path

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic_path = current_dir / "assets" / "urbanicola.png"
profile_pic = Image.open(profile_pic_path)
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

PAGE_TITLE = "Urbanícola"
PAGE_ICON = ":shark:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


url = "http://64.23.131.192:6868/v1/spent"

col1, col2, col3 = st.columns(3)
with col1:
    date = st.date_input("Fecha", value=None)
with col2:
    mount = st.number_input("Agrega el monto", min_value=0.1)
with col3:
    type = st.selectbox('Tipo de gasto',("Fijo", "Variable"))
description = st.text_input(
    "Por favor agrega la descripción de gasto",
    placeholder="descripción",
)
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
            json=make_spent(date, mount, type, concept, subtype, area, 1, provider, factura, payment_type, bank_count, description),
            headers=headers)
            )


st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
