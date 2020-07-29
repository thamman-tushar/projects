user = {}
status = ""

def displaymenu():
	status = input("\n\nAre you registered user? \"Y/N\" ?...'q for quit ' : ")
	if status.upper()=="Y":
		oldUser()
	elif status.upper()=="N":
		newUser()
	elif status.upper()=="Q":
		print("Thanks! For Using ;)")

def newUser():
	createlogin = input("Enter Login name : ")

	if createlogin in user:
		print("\n User already registered!\n")
		newUser()

	else:
		createPassw = input("Create Password : ")
		user[createlogin] = createPassw
		quer=input("\n User Created!\n Login? \"Y/N\"? : ")
		if quer.upper()=="Y":
			oldUser()
		elif quer.upper()=="Q":
			print("Thanks! For Using ;)")

def oldUser():
	login = input("Enter Login Id : ")
	passw = input("Enter Password : ")

	if login in user and user[login] == passw:
			print("Login Successfull! ")

	else :
		if login in user and user[login] != passw:
			print("\nPassword Not Matched try again \n")
			oldUser()

		else :
			ver=input("Enter Correct Details OR Create new login \"Y/N\"? : ")
			if ver.upper()=="Y":
				newUser()
			elif ver.upper()=="N":
		 		oldUser()
#		 	elif ver.upper()=="Q":
#		 		print("Thanks! For Using ;) ")
