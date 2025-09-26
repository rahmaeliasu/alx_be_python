def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def items(item):
    print("Enter the item: ")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f'Added "{item}" to the shopping list.')

        elif choice == '2':
            item = input("Enter the item remove: ")
            shopping_list.remove(item)
            print(f'Removed "{item}" from the shoppong list.')
        elif choice == '3':
            item = input("Enter the item view: ")
            if item in shopping_list:
                print(f'"{item}" in shopping list.')
            else:
                print(f'"{item}" not in shoping list.')
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
