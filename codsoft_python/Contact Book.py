class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        if name not in self.contacts:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print(f"Contact '{name}' added successfully.")
        else:
            print(f"Contact '{name}' already exists. Use a different name.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n")

    def search_contact(self, query):
        results = []
        for name, details in self.contacts.items():
            if query.lower() in name.lower() or query in details['phone']:
                results.append((name, details))

        if results:
            print("\nSearch Results:")
            for result in results:
                print(f"Name: {result[0]}\nPhone: {result[1]['phone']}\nEmail: {result[1]['email']}\nAddress: {result[1]['address']}\n")
        else:
            print("No matching contacts found.")

    def update_contact(self, name, field, new_value):
        if name in self.contacts:
            if field in self.contacts[name]:
                self.contacts[name][field] = new_value
                print(f"Contact '{name}' updated successfully.")
            else:
                print(f"Invalid field '{field}'. Choose from 'phone', 'email', or 'address'.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

def main():
    contact_book = ContactBook()

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
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            query = input("Enter contact name or phone number to search: ")
            contact_book.search_contact(query)

        elif choice == '4':
            name = input("Enter contact name to update: ")
            field = input("Enter field to update (phone/email/address): ")
            new_value = input(f"Enter new value for {field}: ")
            contact_book.update_contact(name, field, new_value)

        elif choice == '5':
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    main()
