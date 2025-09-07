import re
def add_contact():
	name=input("Enter name:").strip()
	if name in contact:
		print("Already existed")
	else:
		phone=get_valid_phone_number()
		email=get_valid_email()
		contact[name]={"phone":phone,"email":email}
		print(f"{name} added successfully")
def del_contact():
	name=input("Enter the name to delete:").strip()
	if name in contact:
		del contact[name]
		print(f"{name} deleted successfully")
	else:
		print("No contact found")
def update_contact():
	name=input("Enter the name to update:")
	if name in contact:
		phone=get_valid_phone_number(blank=True)
		email=get_valid_email(blank=True)
		if phone:
			contact[name]["phone"]=phone
		if email:
			contact[name]["email"]=email
		print(f"{name} updated successfully")
	else:
		print("No contact found")
def view_contact():
	name=input("Enter the name to view in the contact book:")
	if name in contact:
		print(f"Name:{name}")
		print(f"Phone:{contact[name]["phone"]}")
		print(f"Email:{contact[name]["email"]}")
	else:
		print("No search found")
def view_all_contact():
    if contact:
        print("All Contacts")
        print("-"*40)
        for name,details in contact.items():
            print(f"Name:{name}")
            print(f"Phone:{details["phone"]}")
            print(f"Email:{details["email"]}")
            print("-"*40)
def get_valid_phone_number(blank=False):
	while True:
		phone=input("Enter phone number:")
		if blank and phone=="":
			return None
		if phone.isdigit() and len(phone)==10:
			return phone
		print("Invalid phone number.Please enter a valid 10 digit phone number")	
def get_valid_email(blank=False):
	pattern= r'^[\w\.-]+@[\w\.-]+\.\w+$'
	while True:
		email=input("Enter email:").strip()
		if blank and email=="":
			return None
		if re.match(pattern,email):
			return email
		print("Invalid email.Please enter a valid email")	
contact={}
while True:
	print("Contact Book")
	print("-"*40)
	print("\n1.Add new contact\n2.Delete the contact\n3.Update the contact\n4.View the contact\n5.Exit\n")
	try:
		choice = int(input("Enter your option (1-6): "))
		if choice==1:
			add_contact()
		elif choice==2:
			del_contact()
		elif choice==3:
			update_contact() 
		elif choice==4:
			view_contact()
		elif choice==5:
			view_all_contact()
		elif choice==6:
			print("GoodBye")
			break
		else:
			print("Invalid choice")
	except ValueError:
		print("Please enter a number between 1 and 5.")
  


		 