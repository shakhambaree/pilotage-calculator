# Pilotage Charges Calculator (Dynamic USD Version)

print("🚢 Pilotage Charges Calculator")
print("Includes one Berthing and one Un-berthing\n")

while True:

    # -----------------------------
    # INPUT USD EXCHANGE RATE
    # -----------------------------

    USD_TO_INR = float(input("Enter Today's USD to INR Exchange Rate: "))

    print("\nSelect Vessel Type:")
    print("1. Container")
    print("2. Bulk")
    print("3. Break Bulk")
    print("4. Liquid")
    print("5. LTSB")
    print("6. MFF")
    print("7. Others")

    vessel_choice = int(input("Enter choice (1-7): "))

    if vessel_choice == 1:
        vessel_category = "Container Vessel"
    else:
        vessel_category = "Other Than Container Vessel"

    print("\nSelect Run Type:")
    print("1. Foreign Run")
    print("2. Coastal Run")

    run_choice = int(input("Enter choice (1-2): "))

    if run_choice == 1:
        run_type = "Foreign Run"
    else:
        run_type = "Coastal Run"

    # GT as whole number
    gt = int(input("\nEnter Gross Tonnage (GT) (Whole number only): "))

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

        else:  # Coastal Run
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
    # CALCULATE TOTAL
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

    print("\n💰 Charges Breakdown")
    print("Base Charge:", round(base_total, 2), currency)
    print("Fuel Surcharge (0.1 per GT):", round(fuel_surcharge, 2), currency)
    print("Total Charge:", round(total, 2), currency)

    print("\n🔄 Currency Conversion")

    if currency == "USD":
        total_inr = total * USD_TO_INR
        print("Equivalent in INR: ₹", round(total_inr, 2))
    else:
        total_usd = total / USD_TO_INR
        print("Equivalent in USD: $", round(total_usd, 2))

    # -----------------------------
    # REPEAT OPTION
    # -----------------------------

    repeat = input("\nDo you want to calculate again? (y/n): ")

    if repeat.lower() != 'y':
        print("\nThank you for using Pilotage Charges Calculator 🚢")
        break
