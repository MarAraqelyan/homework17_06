def add_contact():
	key = input("Enter name:")
	value = input("Enter phone number:")
	if key in phone_book:
		print("This contact already exsists")
	else:
		phone_book[key] = value
		print("Contact added succesfully!")

def search_contact():
	key = input("Enter name:")
	if key in phone_book:
		print("Phone number:", phone_book[key])
	else:
		print("No such contact")

def list_contacts():
	if len(phone_book) == 0:
		print("No contacts")
	else:
		print("Contacts:")
		for i in phone_book.keys():
			print(i, ':', phone_book[i])

phone_book = {}
ls = ['1. Add a new contact', '2. Search for a contact', '3. List all contacts', '4. Exit']

name = "Phone Book Program"
print(name)
for i in range(len(name)):
	print("-", end = "")
print()
for i in ls:
	print(i)

while True:
	while True:
		choices = [1, 2, 3, 4]	
	
		n = int(input("Enter your choice:"))	
		if n in	choices:
			break

	if n == 1:
		add_contact()
	if n == 2:
		search_contact()
	if n == 3:
		list_contacts()
	if n == 4:
		print("Goodbye!")
		break





