import streamlit as st

st.set_page_config(page_title="Pilotage Charges Calculator", page_icon="🚢")

# Fixed Conversion Rate
USD_TO_INR = 90.73

st.title("🚢 Pilotage Charges Calculator")
st.markdown("Calculate Pilotage Charges with Currency Conversion")

# -----------------------------
# DROPDOWNS
# -----------------------------

vessel_category = st.selectbox(
    "Select Vessel Category",
    ["Container Vessel", "Other Than Container Vessel"]
)

run_type = st.selectbox(
    "Select Run Type",
    ["Foreign Run", "Coastal Run"]
)

gt = st.number_input("Enter Gross Tonnage (GT)", min_value=0.0)

currency = st.selectbox("Select Currency for Base Calculation", ["USD", "INR"])

# -----------------------------
# RATE LOGIC
# -----------------------------

rate = 0
minimum = 0
fuel_surcharge = 0

# =============================
# CONTAINER VESSEL (Sample Slabs – Adjust if needed)
# =============================
if vessel_category == "Container Vessel":

    if run_type == "Foreign Run":

        if gt <= 3000:
            rate = 0.50
            minimum = 3000
        elif gt <= 10000:
            rate = 0.55
        elif gt <= 30000:
            rate = 0.70
        else:
            rate = 0.85

    else:  # Coastal Run

        if gt <= 3000:
            rate = 40
            minimum = 200000
        elif gt <= 10000:
            rate = 45
        elif gt <= 30000:
            rate = 60
        else:
            rate = 75

# =============================
# OTHER THAN CONTAINER (FROM YOUR IMAGE)
# =============================
else:

    if run_type == "Foreign Run":

        if gt <= 3000:
            rate = 0
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

    else:  # Coastal Run

        if gt <= 3000:
            rate = 0
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
# CALCULATION
# -----------------------------

if gt > 0:

    if rate == 0:
        base_total = minimum
    else:
        calculated = gt * rate
        if minimum > 0:
            base_total = max(calculated, minimum)
        else:
            base_total = calculated

    # Fuel Surcharge (0.1 per GT)
    fuel_surcharge = gt * 0.1

    total = base_total + fuel_surcharge

    st.success(f"Base Charge: {round(base_total,2)} {currency}")
    st.info(f"Fuel Surcharge (0.1 per GT): {round(fuel_surcharge,2)} {currency}")
    st.success(f"Total Charge: {round(total,2)} {currency}")

    # -----------------------------
    # CURRENCY CONVERSION
    # -----------------------------

    if currency == "USD":
        total_inr = total * USD_TO_INR
        st.markdown("### 💰 Converted Amount")
        st.write(f"Equivalent in INR: ₹ {round(total_inr,2)}")

    else:
        total_usd = total / USD_TO_INR
        st.markdown("### 💰 Converted Amount")
        st.write(f"Equivalent in USD: $ {round(total_usd,2)}")


   
