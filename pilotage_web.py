import streamlit as st

st.set_page_config(page_title="Pilotage Charges Calculator", page_icon="🚢")

USD_TO_INR = 90.73  # Fixed conversion rate

st.title("🚢 Pilotage Charges Calculator")
st.markdown("Includes one Berthing and one Un-berthing")

# -----------------------------
# INPUT SECTION
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

# -----------------------------
# RATE CALCULATION
# -----------------------------

rate = 0
minimum = 0
currency = "USD"

# ==============================
# CONTAINER VESSELS
# ==============================

if vessel_category == "Container Vessel":

    if run_type == "Foreign Run":
        currency = "USD"

        if gt <= 3000:
            rate = 0
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

    else:  # Coastal Run
        currency = "INR"

        if gt <= 3000:
            rate = 0
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
        currency = "INR"

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
# CALCULATE TOTAL
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

    # Fuel surcharge
    fuel_surcharge = gt * 0.1
    total = base_total + fuel_surcharge

    st.subheader("💰 Charges Breakdown")
    st.write(f"Base Charge: {round(base_total,2)} {currency}")
    st.write(f"Fuel Surcharge (0.1 per GT): {round(fuel_surcharge,2)} {currency}")
    st.success(f"Total Charge: {round(total,2)} {currency}")

    # -----------------------------
    # CURRENCY CONVERSION
    # -----------------------------

    st.subheader("🔄 Currency Conversion")

    if currency == "USD":
        total_inr = total * USD_TO_INR
        st.write(f"Equivalent in INR: ₹ {round(total_inr,2)}")

    else:
        total_usd = total / USD_TO_INR
        st.write(f"Equivalent in USD: $ {round(total_usd,2)}")
