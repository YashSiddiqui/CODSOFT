# Initialize an empty contact list as a dictionary
contacts = {}


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"{name} added to contacts.")


def view_contact_list():
    if contacts:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("-" * 20)
    else:
        print("No contacts found.")


def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = []
    for name, info in contacts.items():
        if search_term.lower() in name.lower() or search_term in info['phone']:
            found_contacts.append((name, info))

    if found_contacts:
        print("\nSearch Results:")
        for name, info in found_contacts:
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("-" * 20)
    else:
        print("No matching contacts found.")


def update_contact():
    name_to_update = input("Enter the name of the contact to update: ")
    if name_to_update in contacts:
        print(f"Current details for {name_to_update}:")
        print(f"Phone: {contacts[name_to_update]['phone']}")
        print(f"Email: {contacts[name_to_update]['email']}")
        print(f"Address: {contacts[name_to_update]['address']}")
        new_phone = input("Enter new phone number (press Enter to keep current): ")
        new_email = input("Enter new email address (press Enter to keep current): ")
        new_address = input("Enter new address (press Enter to keep current): ")
        if new_phone:
            contacts[name_to_update]['phone'] = new_phone
        if new_email:
            contacts[name_to_update]['email'] = new_email
        if new_address:
            contacts[name_to_update]['address'] = new_address
        print(f"Contact details for {name_to_update} updated.")
    else:
        print(f"{name_to_update} not found in contacts.")


def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ")
    if name_to_delete in contacts:
        del contacts[name_to_delete]
        print(f"{name_to_delete} deleted from contacts.")
    else:
        print(f"{name_to_delete} not found in contacts.")


# Main loop for the user interface
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
