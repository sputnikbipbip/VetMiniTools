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
            base_value = float(val_input)
        except ValueError:
            print("Error: Please enter a valid numerical value.")
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
            multiplier = 1.06
        elif choice == '2':
            multiplier = 1.23
        else:
            print("Error: Invalid selection. Please choose 1 or 2.")
            continue

        # 3. Perform calculations
        # First, multiply by the selected multiplier (1.06 or 1.23)
        productBuyPrice = base_value * multiplier
        
        # Then, multiply that result by 1.4 (profit margin)
        final_value = productBuyPrice * 1.4

        # 4. Print the results formatted to 2 decimal places
        print("\n--- Results ---")
        print(f"Supplier price:           {base_value:.2f}")
        print(f"IVA: {multiplier} Product Buy price {productBuyPrice:.2f}  <-- (Before multiplying by 1.4)")
        print(f"Product Sell Price:   {final_value:.2f}  <-- (After multiplying by 1.4)")
        print("-" * 25)

if __name__ == "__main__":
    main()