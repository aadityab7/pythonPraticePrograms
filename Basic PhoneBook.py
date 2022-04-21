print("\nProgram to Impliment a PhoneBook: \n")

class Contact:
	def __init__ (Self, contacts_details):
		Self.contacts_details = contacts_details
	
	#Show All Data : 
	def getData(Self):
		rfile = open("contacts.txt", "r")
		Contacts = rfile.read()
		print(Contacts)
		rfile.close()

	#Add Data : 
	def putData(Self):
		wfile = open("contacts.txt", "a")

		for i in Self.contacts_details:
			wfile.write(i)
			wfile.write("\n")
		
		wfile.close()

	#search
	#delete 
	#update 


def readContacts():
		rfile = open("contacts.txt", "r")
		Contacts = rfile.read()
		print(Contacts)
		rfile.close()

def table():
	sno = 1
	x = 1
	tfile = open("contacts.txt", "r")
	Contacts_data = tfile.read().split("\n")

	print("Sno.\t|\tName\t|\tL_Name\t|\tphone no\t|\tMail\t|\n")

	for i in Contacts_data:
		if(x == 1):
			print(sno, end = '\t|\t')
		print(i, end = '\t|\t')

		x = x + 1
		if(x == 5):
			print("\n")
			x = 1
			sno = sno + 1
		
	tfile.close()


t = int(input("Number of contacts to be entered : "))
while(t > 0):

	f_name1 = input("Enter First Name : ")
	l_name1 = input("Enter Last name : ")
	address = input("Enter Address : ")
	number1 = input("Enter  Phone number 1 : ")
	number2 = input("Enter Phone number 2 : ")
	email = input("Enter E-mail : ")
	catagory = input("Enter catagory : ")

	Contacts_details = [f_name1, l_name1, address, number1, number2, email, catagory]

	c1 = Contact(Contacts_details)
	c1.putData()

	t = t - 1

readContacts()