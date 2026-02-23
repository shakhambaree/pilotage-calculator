import streamlit as st

st.set_page_config(page_title="Pilotage Charges Calculator", page_icon="🚢")

st.title("🚢 Pilotage Charges Calculator")
st.markdown("Includes one Berthing and one Un-berthing")

# -----------------------------
# INPUT SECTION
# -----------------------------

# Dynamic USD rate input
USD_TO_INR = st.number_input(
    "Enter Today's USD to INR Exchange Rate",
    min_value=0.0,
    value=90.73,
    step=0.01
)

# Vessel type selection
vessel_type = st.selectbox(
    "Select Vessel Type",
    ["Container", "Bulk", "Break Bulk", "Liquid", "LTSB", "MFF", "Others"]
)

# Auto mapping
if vessel_type == "Container":
    vessel_category = "Container Vessel"
else:
    vessel_category = "Other Than Container Vessel"

run_type = st.selectbox(
    "Select Run Type",
    ["Foreign Run", "Coastal Run"]
)

# Whole number GT
gt = st.number_input(
    "Enter Gross Tonnage (GT)",
    min_value=0,
    step=1,
    format="%d"
)

# Add Calculate Button (important for Streamlit)
calculate = st.button("Calculate Charges")

# -----------------------------
# CALCULATION
# -----------------------------

if calculate and gt > 0:

    rate = 0
    minimum = 0
    currency = "USD"

    # ==============================
    # CONTAINER
    # ==============================

    if vessel_category == "Container Vessel":

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

    # ==============================
    # OTHER THAN CONTAINER
    # ==============================

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

    # -----------------------------
    # TOTAL CALCULATION
    # -----------------------------

    if rate == 0:
        base_total = minimum
    else:
        calculated = gt * rate
        if minimum > 0:
            base_total = max(calculated, minimum)
        else:
            base_total = calculated

    fuel_surcharge = gt * 0.1
    total = base_total + fuel_surcharge

    # -----------------------------
    # OUTPUT
    # -----------------------------

    st.subheader("💰 Charges Breakdown")
    st.write(f"Base Charge: {round(base_total,2)} {currency}")
    st.write(f"Fuel Surcharge (0.1 per GT): {round(fuel_surcharge,2)} {currency}")
    st.success(f"Total Charge: {round(total,2)} {currency}")

    st.subheader("🔄 Currency Conversion")

    if currency == "USD":
        total_inr = total * USD_TO_INR
        st.write(f"Equivalent in INR: ₹ {round(total_inr,2)}")
    else:
        total_usd = total / USD_TO_INR
        st.write(f"Equivalent in USD: $ {round(total_usd,2)}")

elif calculate and gt == 0:
    st.warning("Please enter a valid GT value.")
