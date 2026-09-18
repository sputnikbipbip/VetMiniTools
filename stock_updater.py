from decimal import Decimal, InvalidOperation, ROUND_UP


CENT = Decimal("0.01")


def round_up(value):
    return value.quantize(CENT, rounding=ROUND_UP)


def main():
    print("="*45)
    print("   STOCK PRICE UPDATER")
    print("   (Type 'q' or 'quit' at any prompt to exit)")
    print("="*45)

    while True:
        # 1. Accept the base value
        print("\n--- New Calculation ---")
        val_input = input("Enter the base stock price: ").strip()
        
        # Check for exit command
        if val_input.lower() in ['q', 'quit', 'exit']:
            print("Exiting program. Goodbye!")
            break
            
        # Replace comma with dot to handle European decimal formats (e.g., 1,06 -> 1.06)
        val_input = val_input.replace(',', '.')
        
        try:
            base_value = Decimal(val_input)
        except InvalidOperation:
            print("Error: Please enter a valid numerical value.")
            continue

        if not base_value.is_finite() or base_value < 0:
            print("Error: Please enter a non-negative numerical value.")
            continue

        # 2. Ask user to select the multiplier
        print("Select multiplier:")
        print("  [1] for 1.06")
        print("  [2] for 1.23")
        choice = input("Enter 1 or 2: ").strip()
        
        if choice.lower() in ['q', 'quit', 'exit']:
            print("Exiting program. Goodbye!")
            break

        if choice == '1':
            multiplier = Decimal("1.06")
            iva = "6%"
        elif choice == '2':
            multiplier = Decimal("1.23")
            iva = "23%"
        else:
            print("Error: Invalid selection. Please choose 1 or 2.")
            continue

        # 3. Perform calculations
        # First, multiply by the selected multiplier (1.06 or 1.23)
        productBuyPrice = round_up(base_value * multiplier)
        
        # Then, multiply that result by 1.4 (profit margin)
        final_value = round_up(productBuyPrice * Decimal("1.4"))

        # Check if we need to divide by number of units (if applicable)
        units_input = input("Enter the number of units (or press Enter to skip): ").strip()
        if units_input:
            try:
                units = int(units_input)
                if units <= 0:
                    print("Error: Please enter a positive integer for the number of units.")
                    continue
                final_saleprice__per_unit = round_up(final_value /units)
                final_purchase_per_unit = round_up(productBuyPrice / units)
            except ValueError:
                print("Error: Please enter a valid integer for the number of units.")
                continue

        # 4. Print the results formatted to 2 decimal places
        print("\n--- Results ---")
        print(f"Supplier price: {base_value:.2f}")
        print(f"IVA: {iva}")
        print(f"Purchase Price: {productBuyPrice:.2f}")
        print(f"Sale Price: {final_value:.2f}")
        if units_input:
            print(f"[Purchase Price p/Unit: {final_purchase_per_unit:.2f}]")
            print(f"[Sale Price p/Unit: {final_saleprice__per_unit:.2f}]")
        print("-" * 25)

if __name__ == "__main__":
    main()