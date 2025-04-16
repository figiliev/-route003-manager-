# ROUTE #003 Manager App - Phase 1
# Author: Levi Bundi
# Purpose: Help couriers manage routes, customers, deliveries, fuel, and maintenance logs

import datetime

# ----------------------
# Customer Data Section to be updated based on the driver's route 
# ----------------------
customers = {
    "FENTON NISSAN": {
        "town": "McAlester",
        "parts": 7,
        "payment": "COD",
        "dropoff_notes": "Check required before dropoff",
        "delivered": False
    },
    "NIX CHEVROLET": {
        "town": "Seminole",
        "parts": 2,
        "payment": "PAID",
        "dropoff_notes": "Leave at front desk",
        "delivered": False
    }
}

# ----------------------
# Fuel & Maintenance Logs
# ----------------------
fuel_log = []  # List of dictionaries
maintenance_log = {
    "Vehicle_type":"Dodge Sprinter Van",
    "VIN": "WDYPD744565968040",
    "last_oil_change": 98000,
    "last_checkup": "2024-12-01",
    "issues": []
}

# ----------------------
# Core Functions
# ----------------------
def lookup_customer(name):
    name = name.upper()
    if name in customers:
        data = customers[name]
        print(f"\nCustomer: {name}")
        print(f"Town: {data['town']}")
        print(f"Parts Ordered: {data['parts']}")
        print(f"Payment Type: {data['payment']}")
        print(f"Dropoff Notes: {data['dropoff_notes']}")
        print(f"Delivered: {'Yes' if data['delivered'] else 'No'}\n")
    else:
        print("Customer not found.\n")

def mark_delivered(name):
    name = name.upper()
    if name in customers:
        customers[name]['delivered'] = True
        print(f"Marked {name} as delivered.\n")
    else:
        print("Customer not found.\n")

def log_fuel(date, price, location, miles):
    entry = {
        "date": date,
        "price": price,
        "location": location,
        "miles": miles
    }
    fuel_log.append(entry)
    print("Fuel log updated.\n")

def check_maintenance(current_miles):
    due = maintenance_log['last_oil_change'] + 10000
    print("\nMaintenance Check:")
    print(f"Last oil change at: {maintenance_log['last_oil_change']} miles")
    print(f"Current miles: {current_miles}")
    if current_miles >= due:
        print("Oil change is due!")
    else:
        print("No maintenance needed at this time.")
    print("")

# ----------------------
# Basic Menu Loop (for testing)
# ----------------------
if __name__ == "__main__":
    while True:
        print("--- ROUTE #003 MANAGER ---")
        print("1. Lookup Customer")
        print("2. Mark Delivery")
        print("3. Log Fuel")
        print("4. Check Maintenance")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            lookup_customer(name)

        elif choice == "2":
            name = input("Enter customer name to mark as delivered: ")
            mark_delivered(name)

        elif choice == "3":
            date = input("Date (YYYY-MM-DD): ")
            price = float(input("Fuel Price ($): "))
            location = input("Location: ")
            miles = int(input("Miles driven: "))
            log_fuel(date, price, location, miles)

        elif choice == "4":
            current_miles = int(input("Enter current mileage: "))
            check_maintenance(current_miles)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.\n")