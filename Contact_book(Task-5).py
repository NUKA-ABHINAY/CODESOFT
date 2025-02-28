class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f"Contact for {name} added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\nContact List:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts 
                          if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if found_contacts:
            print("\nSearch Results:")
            for contact in found_contacts:
                self.display_contact(contact)
        else:
            print("No contacts found.")

    def update_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                print("\nUpdating Contact:")
                self.display_contact(contact)
                name = input("Enter new name (leave blank to keep current): ") or contact.name
                phone = input("Enter new phone (leave blank to keep current): ") or contact.phone
                email = input("Enter new email (leave blank to keep current): ") or contact.email
                address = input("Enter new address (leave blank to keep current): ") or contact.address
                contact.name, contact.phone, contact.email, contact.address = name, phone, email, address
                print("Contact updated.")
                return
        print("No contact found to update.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                self.contacts.remove(contact)
                print(f"Contact for {contact.name} deleted.")
                return
        print("No contact found to delete.")

    def display_contact(self, contact):
        print(f"\nName: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Address: {contact.address}")

def main():
    manager = ContactManager()

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)
        elif choice == '4':
            search_term = input("Enter name or phone number to update: ")
            manager.update_contact(search_term)
        elif choice == '5':
            search_term = input("Enter name or phone number to delete: ")
            manager.delete_contact(search_term)
        elif choice == '6':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
