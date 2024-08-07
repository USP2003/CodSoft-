#Contact Information: Store name, phone number, email, and address for each contact.

#Add Contact: Allow users to add new contacts with their details.

#View Contact List: Display a list of all saved contacts with names and phone numbers.
#Search Contact: Implement a search function to find contacts by name or phone number.

#Update Contact: Enable users to update contact details.
#Delete Contact: Provide an option to delete a contact.

#User Interface: Design a user-friendly interface for easy interaction.

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"\nContact '{contact.name}' added successfully!")

    def view_contact_list(self):
        print("\n=== Contact List ===")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        matching_contacts = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        return matching_contacts

    def update_contact(self, index, updated_contact):
        self.contacts[index] = updated_contact
        print(f"\nContact '{updated_contact.name}' updated successfully!")

    def delete_contact(self, index):
        deleted_contact = self.contacts.pop(index)
        print(f"\nContact '{deleted_contact.name}' deleted successfully!")

def get_user_input(prompt):
    return input(prompt + ": ").strip()

def main():
    contact_manager = ContactManager()

    while True:
        print("\n=== Contact Management System ===")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = get_user_input("Enter your choice")

        if choice == "1":
            name = get_user_input("Enter the name")
            phone = get_user_input("Enter the phone number")
            email = get_user_input("Enter the email")
            address = get_user_input("Enter the address")

            new_contact = Contact(name, phone, email, address)
            contact_manager.add_contact(new_contact)

        elif choice == "2":
            contact_manager.view_contact_list()

        elif choice == "3":
            query = get_user_input("Enter the name or phone number to search")
            matching_contacts = contact_manager.search_contact(query)

            if matching_contacts:
                print("\n=== Matching Contacts ===")
                for contact in matching_contacts:
                    print(f"{contact.name} - {contact.phone}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            index = int(get_user_input("Enter the index of the contact to update"))
            if 0 <= index < len(contact_manager.contacts):
                updated_name = get_user_input("Enter the updated name")
                updated_phone = get_user_input("Enter the updated phone number")
                updated_email = get_user_input("Enter the updated email")
                updated_address = get_user_input("Enter the updated address")

                updated_contact = Contact(updated_name, updated_phone, updated_email, updated_address)
                contact_manager.update_contact(index, updated_contact)
            else:
                print("Invalid index. Please enter a valid index.")

        elif choice == "5":
            index = int(get_user_input("Enter the index of the contact to delete"))
            if 0 <= index < len(contact_manager.contacts):
                contact_manager.delete_contact(index)
            else:
                print("Invalid index. Please enter a valid index.")

        elif choice == "6":
            print("Exiting the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
