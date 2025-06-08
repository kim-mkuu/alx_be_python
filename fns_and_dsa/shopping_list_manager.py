def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"Added: {item}")
            else:
                print("Error: Cannot add empty item")
                
        elif choice == '2':
            if not shopping_list:
                print("The shopping list is empty.")
                continue
                
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed: {item}")
            else:
                print(f"Item not found: {item}")
                
        elif choice == '3':
            if shopping_list:
                print("Current Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Your shopping list is empty.")
                
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1-4.")

if __name__ == "__main__":
    main()