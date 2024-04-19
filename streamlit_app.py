import requests
import pandas as pd
import streamlit as st
from PIL import Image
from pathlib import Path

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
profile_pic_path = current_dir / "assets" / "urbanicola.png"
profile_pic = Image.open(profile_pic_path)
PAGE_TITLE = "Urbanícola"
PAGE_ICON = "🦈"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


def make_spent(
    fecha,
    monto,
    tipo,
    concepto,
    subtipo,
    area,
    cantidad,
    proveedor,
    factura,
    tipo_pago,
    cuenta,
    descripcion,
):
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
        "description": [descripcion],
    }


def make_selling(
    concept,
    sales_date,
    expiration,
    status,
    sales_credit,
    customer,
    prod_serv,
    amount,
    paid,
    unit_price,
    bank_account,
    way_pay,
    sector,
    invoice_folio,
    date_issue,
    final_price,
    discount,
    income,
    product_cost,
    delivery_type,
    shipping_cost,
    shipping_date,
    place_delivery,
    delivery_date,
    billig,
    profit,
    margin_gain,
    payment_status,
    sales_number,
    pending_amount,
    registration_date,
    check,
):
    return {
        "concept": [concept],
        "sales_date": [sales_date],
        "expiration": [expiration],
        "status": [status],
        "sales_credit": [sales_credit],
        "customer": [customer],
        "prod_serv": [prod_serv],
        "amount": [amount],
        "paid": [paid],
        "unit_price": [unit_price],
        "bank_account": [bank_account],
        "way_pay": [way_pay],
        "sector": [sector],
        "invoice_folio": [invoice_folio],
        "date_issue": [date_issue],
        "final_price": [final_price],
        "discount": [discount],
        "income": [income],
        "product_cost": [product_cost],
        "delivery_type": [delivery_type],
        "shipping_cost": [shipping_cost],
        "shipping_date": [shipping_date],
        "place_delivery": [place_delivery],
        "delivery_date": [delivery_date],
        "billig": [billig],
        "profit": [profit],
        "margin_gain": [margin_gain],
        "payment_status": [payment_status],
        "sales_number": [sales_number],
        "pending_amount": [pending_amount],
        "registration_date": [registration_date],
        "check": [check],
    }


headers = {"Content-type": "application/json"}
url = "http://64.23.131.192:6868/v1/spent"
gastos, ventas = st.tabs(["Gastos", "Ventas"])

with gastos:
    col1, _ = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)
    col1, col2, col3 = st.columns(3)
    with col1:
        date = st.date_input("Fecha", value=None)
    with col2:
        mount = st.number_input("Agrega el monto", min_value=0.1)
        how_many = st.number_input("Cantidad", min_value=0.1)
    with col3:
        type = st.selectbox("Tipo de gasto", ("Fijo", "Variable"))
    colA, colB, colC = st.columns(3)
    with colA:
        concept = st.selectbox("Concepto", ("Administrativos", "Costos", "Otros"))
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

    if st.button("Registrar gasto"):
        st.write(
            str(date),
            mount,
            type,
            concept,
            subtype,
            area,
            how_many,
            provider,
            factura,
            payment_type,
            bank_count,
            description,
        )
        st.write(
            requests.post(
                url,
                json=make_spent(
                    date,
                    mount,
                    type,
                    concept,
                    subtype,
                    area,
                    how_many,
                    provider,
                    factura,
                    payment_type,
                    bank_count,
                    description,
                ),
                headers=headers,
            )
        )


# Ventas
with ventas:
    col1, _ = st.columns(2, gap="small")
    col1, col2, col3 = st.columns(3)
    with col1:
        concept = st.selectbox("Concepto", ("Venta", "Ingreso"))
    with col2:
        sales_date = st.date_input("Fecha de venta", value=None)
    with col3:
        expiration = st.date_input("Vencimiento", value=None)
    col1, col2, col3 = st.columns(3)
    with col1:
        customer = st.text_input(
            "Por favor agrega al cliente",
            placeholder="cliente",
        )
    with col2:
        status = st.selectbox("Estatus", ("Pagada", "Inversión", "Préstamo"))
    with col3:
        prod_serv = st.text_input(
            "Producto/servicio",
            placeholder="servicio",
        )
    col1, col2, col3 = st.columns(3)
    with col1:
        amount = st.number_input("Cantidad venta", min_value=0.1)
    with col2:
        paid = st.number_input("Pagado", min_value=0.1)
    with col3:
        unit_price = st.number_input("Precio unitario", min_value=0.1)
    col1, col2, col3 = st.columns(3)
    with col1:
        bank_acount = st.selectbox("Cuenta", ("Efectivo", "Bajío", "Santander"))
    with col2:
        way_pay = st.selectbox("Cuenta", ("Efectivo", "Transferencia"))
    with col3:
        sector = st.selectbox("Área", ("Obra", "Mantenimiento", "Proyecto", "Inversión"))
    col1, col2, col3 = st.columns(3)
    with col1:
        invoice_folio = st.text_input(
            "Folio factura",
            placeholder="folio",
        )
    with col2:
        date_issue = st.date_input("Emisión", value=None)
    with col3:
        final_price = st.number_input("Precio final", min_value=0.1)
    col1, col2, col3 = st.columns(3)
    with col1:
        discount = st.number_input("Descuento", min_value=0.1)
    with col2:
        income = st.number_input("Ingreso", min_value=0.1)
    with col3:
        product_cost = st.number_input("Costo Prod", min_value=0.1)
    col1, col2, col3 = st.columns(3)
    with col1:
        delivery_type = st.selectbox("Tipo de entrega", ("En persona", "Desde lejitos"))
    with col2:
        shipping_cost = st.number_input("Costo de envío", min_value=0.1)
    with col3:
        shipping_date = st.date_input("Fecha de envío", value=None)
    col1, col2, col3 = st.columns(3)
    with col1:
        place_delivery = st.selectbox("Lugar de entrega", ("En persona", "Desde lejitos"))
    with col2:
        delivery_date = st.date_input("Fecha de entrega", value=None)
    with col3:
        billig = st.checkbox("Facturación")
    col1, col2, col3 = st.columns(3)
    with col1:
        profit = st.number_input("Ganancia", min_value=0.1)
    with col2:
        margin_gain = st.number_input("Margen", min_value=0.1)
    with col3:
        payment_status = st.selectbox("Status pago", ("Pagada", "Espera"))
    col1, col2, col3 = st.columns(3)
    with col1:
        sales_number = st.number_input("Número de venta", min_value=0.1)
    with col2:
        pending_amount = st.number_input("Mont pendiente", min_value=0.1)
    with col3:
        registration_date = st.date_input("Fecha de registro", value=None)
    sales_credit = True
    bank_account = "Santander"
    check = True

    if st.button("Registrar venta"):
        st.write(
                    concept,
                    sales_date,
                    expiration,
                    status,
                    sales_credit,
                    customer,
                    prod_serv,
                    amount,
                    paid,
                    unit_price,
                    bank_account,
                    way_pay,
                    sector,
                    invoice_folio,
                    date_issue,
                    final_price,
                    discount,
                    income,
                    product_cost,
                    delivery_type,
                    shipping_cost,
                    shipping_date,
                    place_delivery,
                    delivery_date,
                    billig,
                    profit,
                    margin_gain,
                    payment_status,
                    sales_number,
                    pending_amount,
                    registration_date,
                    check,
        )
        st.write(
            requests.post(
                url,
                json=make_selling(
                    concept,
                    sales_date,
                    expiration,
                    status,
                    sales_credit,
                    customer,
                    prod_serv,
                    amount,
                    paid,
                    unit_price,
                    bank_account,
                    way_pay,
                    sector,
                    invoice_folio,
                    date_issue,
                    final_price,
                    discount,
                    income,
                    product_cost,
                    delivery_type,
                    shipping_cost,
                    shipping_date,
                    place_delivery,
                    delivery_date,
                    billig,
                    profit,
                    margin_gain,
                    payment_status,
                    sales_number,
                    pending_amount,
                    registration_date,
                    check,
                ),
                headers=headers,
            )
        )

st.markdown("Made with 💖 by [nies.futbol](https://nies.futbol)")
