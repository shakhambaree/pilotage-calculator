import streamlit as st
from datetime import date

st.set_page_config(page_title="Pilotage Charges Calculator", page_icon="🚢")

st.title("🚢 Pilotage Charges Calculator")
st.markdown("Includes one Berthing and one Un-berthing")

# -----------------------------
# INVOICE DETAILS
# -----------------------------

st.subheader("Invoice Details")

colA, colB = st.columns(2)

with colA:
    vessel_name = st.text_input("Vessel Name")
    invoice_no = st.text_input("Invoice Number")
    port = st.text_input("Port Name", value="Chennai")

with colB:
    agent_name = st.text_input("Shipping Agent")
    voyage_no = st.text_input("Voyage Number")
    invoice_date = st.date_input("Invoice Date", value=date.today())

# -----------------------------
# INPUT SECTION
# -----------------------------

st.subheader("Calculation Inputs")

col1, col2 = st.columns(2)

with col1:
    USD_TO_INR = st.number_input(
        "Enter Today's USD to INR Exchange Rate",
        min_value=0.0,
        value=90.73000,
        step=0.00001,
        format="%.5f"
    )

with col2:
    fuel_rate = st.number_input(
        "Enter Fuel Surcharge per GT",
        min_value=0.0,
        value=0.10000,
        step=0.00001,
        format="%.5f"
    )

# Vessel Selection
vessel_type = st.selectbox(
    "Select Vessel Type",
    [
        "Container",
        "Non-Container",
        "Bulk",
        "Break Bulk",
        "Liquid",
        "LTSB",
        "MFF",
        "Others"
    ]
)

if vessel_type == "Container":
    vessel_category = "Container"
else:
    vessel_category = "Non-Container"

run_type = st.selectbox(
    "Select Run Type", ["Foreign Run", "Coastal Run"]
)

gt = st.number_input(
    "Enter Gross Tonnage (GT)",
    min_value=0,
    step=1,
    format="%d"
)

calculate = st.button("Calculate Charges")

# -----------------------------
# CALCULATION
# -----------------------------

if calculate and gt > 0:

    rate = 0
    minimum = 0
    currency = "USD"

    if vessel_category == "Container":

        if run_type == "Foreign Run":
            currency = "USD"

            if gt <= 3000:
                minimum = 2095
            elif gt <= 10000:
                rate = 0.376
                minimum = 3492
            elif gt <= 15000:
                rate = 0.433
            elif gt <= 30000:
                rate = 0.502
            elif gt <= 60000:
                rate = 0.712
            else:
                rate = 0.824

        else:
            currency = "INR"

            if gt <= 3000:
                minimum = 41889
            elif gt <= 10000:
                rate = 9.78
                minimum = 41889
            elif gt <= 15000:
                rate = 11.17
            elif gt <= 30000:
                rate = 13.96
            elif gt <= 60000:
                rate = 19.54
            else:
                rate = 22.35

    else:

        if run_type == "Foreign Run":
            currency = "USD"

            if gt <= 3000:
                minimum = 2431
            elif gt <= 10000:
                rate = 0.428
                minimum = 3861
            elif gt <= 15000:
                rate = 0.558
            elif gt <= 30000:
                rate = 0.703
            elif gt <= 60000:
                rate = 0.858
            else:
                rate = 0.929

        else:
            currency = "INR"

            if gt <= 3000:
                minimum = 42887
            elif gt <= 10000:
                rate = 10.01
                minimum = 42887
            elif gt <= 15000:
                rate = 11.43
            elif gt <= 30000:
                rate = 14.30
            elif gt <= 60000:
                rate = 20.01
            else:
                rate = 22.87

    # Base calculation
    if rate == 0:
        base_total = minimum
    else:
        calculated = gt * rate
        base_total = max(calculated, minimum) if minimum > 0 else calculated

    fuel_surcharge = gt * fuel_rate
    total = base_total + fuel_surcharge

    # GST (18% example)
    gst = total * 0.18
    grand_total = total + gst

    # -----------------------------
    # TABS FOR OUTPUT
    # -----------------------------

    tab1, tab2, tab3 = st.tabs(
        ["Charges Breakdown", "Tax Invoice", "Performance Invoice"]
    )

    # -----------------------------
    # TAB 1 : BREAKDOWN
    # -----------------------------

    with tab1:

        st.subheader("💰 Charges Breakdown")

        st.write(f"Vessel Type: {vessel_type}")
        st.write(f"Rate Category: {vessel_category}")

        st.write(f"Base Charge: {round(base_total,2)} {currency}")
        st.write(f"Fuel Surcharge: {round(fuel_surcharge,5)} {currency}")

        st.success(f"Total Charge: {round(total,5)} {currency}")

    # -----------------------------
    # TAB 2 : TAX INVOICE
    # -----------------------------

    with tab2:

        st.subheader("🧾 TAX INVOICE")

        st.markdown(f"""
        **Invoice Number:** {invoice_no}  
        **Invoice Date:** {invoice_date}  
        **Port:** {port}

        **Vessel Name:** {vessel_name}  
        **Voyage No:** {voyage_no}  
        **Agent:** {agent_name}

        ---
        **Service:** Pilotage Charges  
        **Gross Tonnage:** {gt}

        Base Charge: {round(base_total,2)} {currency}  
        Fuel Surcharge: {round(fuel_surcharge,2)} {currency}

        **Subtotal:** {round(total,2)} {currency}  
        **GST (18%):** {round(gst,2)} {currency}

        ### Grand Total: {round(grand_total,2)} {currency}
        """)

    # -----------------------------
    # TAB 3 : PERFORMANCE INVOICE
    # -----------------------------

    with tab3:

        st.subheader("📄 PERFORMANCE INVOICE")

        st.markdown(f"""
        **Vessel:** {vessel_name}  
        **Voyage:** {voyage_no}  
        **Port:** {port}

        **Service Performed:**  
        Pilotage – One Berthing & One Un-berthing

        **Gross Tonnage:** {gt}

        Base Charge: {round(base_total,2)} {currency}  
        Fuel Surcharge: {round(fuel_surcharge,2)} {currency}

        **Total Performance Charge:**  
        {round(total,2)} {currency}

        Date of Service: {invoice_date}
        """)

elif calculate and gt == 0:
    st.warning("Please enter a valid GT value.")
