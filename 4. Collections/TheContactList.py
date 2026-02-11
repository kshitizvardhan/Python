Contacts = {
    "Kshitiz":{
        "phone": "123-456-7890",
        "email": "kshitiz@example.com",
        "birthday": "2005-12-11"
    },
    "Shagun":{
        "phone": "234-456-7890",
        "email": "shagun@example.com",
        "birthday": "2006-01-16"
    }
}

print("--- Contact List ---")

while True:
    name = input("Enter the contact name (or 'exit' to quit): ")
    if name.lower() == 'exit':
        break
    if name in Contacts:
        print(f"Contact details for {name}:")
        print(f"Phone: {Contacts[name]['phone']}")
        print(f"Email: {Contacts[name]['email']}")
        print(f"Birthday: {Contacts[name]['birthday']}")
    else:
        print(f"No contact found for {name}.")

