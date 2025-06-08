def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            # Add Item
            item = input("Enter item to add: ").strip()
            if item:  # Check for non-empty input
                shopping_list.append(item)
                print(f"'{item}' added to the shopping list.")
            else:
                print("Invalid input! Item cannot be empty.")
                
        elif choice == '2':
            # Remove Item
            if not shopping_list:
                print("Your shopping list is empty!")
                continue
                
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
                
        elif choice == '3':
            # View List
            if not shopping_list:
                print("Your shopping list is empty!")
            else:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                    
        elif choice == '4':
            # Exit
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1-4.")

if __name__ == "__main__":
    main()