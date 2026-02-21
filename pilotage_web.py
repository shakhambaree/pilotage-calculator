import streamlit as st

st.set_page_config(page_title="Pilotage Charges Calculator", page_icon="🚢")

st.title("🚢 Pilotage Charges Calculator")
st.markdown("Calculate pilotage charges easily.")

vessel_type = st.selectbox(
    "Select Vessel Type",
    ["Container Vessel", "Other Than Container"]
)

run_type = st.selectbox(
    "Select Run Type",
    ["Coastal Run", "Foreign Run"]
)

gt = st.text_input("Enter Vessel Size (GT)")

if st.button("Calculate Charges"):

    try:
        gt = int(gt.replace(",", ""))
        rate = ""
        minimum_charge = ""

        if vessel_type == "Container Vessel":
            if run_type == "Foreign Run":
                if gt <= 3000:
                    rate, minimum_charge = "Lump Sum", "USD 2,095"
                elif gt <= 10000:
                    rate, minimum_charge = "USD 0.376 per GT", "USD 3,492"
                elif gt <= 15000:
                    rate, minimum_charge = "USD 0.433 per GT", "As Applicable"
                elif gt <= 30000:
                    rate, minimum_charge = "USD 0.502 per GT", "As Applicable"
                elif gt <= 60000:
                    rate, minimum_charge = "USD 0.712 per GT", "As Applicable"
                else:
                    rate, minimum_charge = "USD 0.824 per GT", "As Applicable"
            else:
                if gt <= 3000:
                    rate, minimum_charge = "Lump Sum", "INR 41,889"
                elif gt <= 10000:
                    rate, minimum_charge = "INR 9.78 per GT", "INR 41,889"
                elif gt <= 15000:
                    rate, minimum_charge = "INR 11.17 per GT", "As Applicable"
                elif gt <= 30000:
                    rate, minimum_charge = "INR 13.96 per GT", "As Applicable"
                elif gt <= 60000:
                    rate, minimum_charge = "INR 19.54 per GT", "As Applicable"
                else:
                    rate, minimum_charge = "INR 22.35 per GT", "As Applicable"
        else:
            if run_type == "Foreign Run":
                if gt <= 3000:
                    rate, minimum_charge = "Lump Sum", "USD 2,431"
                elif gt <= 10000:
                    rate, minimum_charge = "USD 0.428 per GT", "USD 3,861"
                elif gt <= 15000:
                    rate, minimum_charge = "USD 0.558 per GT", "As Applicable"
                elif gt <= 30000:
                    rate, minimum_charge = "USD 0.703 per GT", "As Applicable"
                elif gt <= 60000:
                    rate, minimum_charge = "USD 0.858 per GT", "As Applicable"
                else:
                    rate, minimum_charge = "USD 0.929 per GT", "As Applicable"
            else:
                if gt <= 3000:
                    rate, minimum_charge = "Lump Sum", "INR 42,887"
                elif gt <= 10000:
                    rate, minimum_charge = "INR 10.01 per GT", "INR 42,887"
                elif gt <= 15000:
                    rate, minimum_charge = "INR 11.43 per GT", "As Applicable"
                elif gt <= 30000:
                    rate, minimum_charge = "INR 14.30 per GT", "As Applicable"
                elif gt <= 60000:
                    rate, minimum_charge = "INR 20.01 per GT", "As Applicable"
                else:
                    rate, minimum_charge = "INR 22.87 per GT", "As Applicable"

        st.success(f"Rate per GT: {rate}")
        st.info(f"Minimum Charges: {minimum_charge}")

    except:
        st.error("Please enter valid GT value.")

st.markdown("---")
st.markdown("Developed for Pilotage Charge Calculation System")
