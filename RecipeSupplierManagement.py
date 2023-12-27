#Main Menu
def mainMenu(): 
	print(Menu)
	print('[1] Recipe Menu')
	print('[2] Supply Menu')
	print('[3] Supplier Menu')
	print('[4] Save State')
	print('[5] Load State')
	print('[6] Exit')
	choice = input('Enter a number: ')
	return choice


#Recipe Book
def recipeMenu():  
	print(Recipe)
	print('[1] Add Recipe')
	print('[2] Delete Recipe')
	print('[3] Delete All Recipes')
	print('[4] View Recipes')
	print('[5] Execute Recipe')
	print('[6] Back to Main Menu')
	choice = input('Enter your choice: ')
	return choice

def addRecipe(dictionx, dictiony): #Function for adding a recipe in the inventory using the supplies.
	ItemList = [] #list for the the items of the recipe containing description and dictionary.
	dictionb = {} #The dictionary containing the item name as a key, and item number as a value.
	RecipeName = '' #Initialization of Recipe Name.
	RecipeName = input('Please Enter your Recipe Name: ') 
	RecipeDescription = input('Please Enter your Recipe Description: ')
	ItemList.append(RecipeDescription)
	while True: #A loop for adding items and will get terminate when 0 was entered.
		ItemName =  input('Please Enter Item Name (Enter 0 to End): ')
		if ItemName == '0':
			if dictionb == {}:
				break
			else:
				ItemList.append(dictionb)
				dictionx[RecipeName] = ItemList 
				break
		

		else: #The computer will ask for item value if 0 is not entered.
			if ItemName in dictiony:
				ItemAmount = int(input('Please Enter the Amount of Items: '))
				dictionb[ItemName] = ItemAmount	
			else:
				print('Item name not found. Please enter it first in supply record.') #This will print if the item name is not in the dictionary of supplies.
				break	#breaks the loop
	
	return dictionx

def deleteRecipe(dictiona): #Function that will delete an entered recipe.
	RecipeName = input('Please Enter Recipe Name to delete: ')
	if RecipeName in dictiona: #Checks if the recipe name is in the recipe dictionary.
		del dictiona[RecipeName]
		print(RecipeName, 'is successfully deleted!')
	else:
		print('Error: The Recipe Name', RecipeName, 'does not exist.') #Prints if the recipe name is not in the dictionary.
	return dictiona

def deleteAll(dictiona): #Fucntion for deleting all the recipes.
	dictiona.clear()
	print('All recipes are deleted.')
	return dictiona

def viewRecipe(dictiona, dictionb, dictionc): #Function for viewing the recipe lists.
	print(recipeRec)
	for k,v  in dictiona.items(): #Nested loop was used since there are dictionaries and lists inside the ditionaries.
		print('Recipe Name: ', k)
		print('Description:', v[0])
		print('')
		for i,j in v[1].items():
			print('Item Name: ', i)
			print('Item Amount: ', j)
			for a,b in dictionb.items(): #This part checks if the item entered is in the supply dictionary.
				if i == a:
					for c,d in dictionc.items(): #This checks it corresponding supplier name and contact to be added in the record.
						if c == b[2]:
							print('Supplier Name: ', c)
							print('Supplier Contact: ', d)
			

			print('')


def executeRecipe(dictiona, dictionb): #Function for executing recipe to subtract the item values from the supplies number.
	print(execute)
	for k,v  in dictiona.items():
		print('Recipe Name: ', k)
		print('Description:', v[0])
		print('')
		for i,j in v[1].items():
			print('Item Name: ', i)
			print('Item Amount: ', j)
			print('')
		print('='*30)
	print('[1] Done   [2] Cancel')
	choice = input('Enter Number: ')
	if choice == '1': 
		for a, b in list(dictionb.items()): #These blocks of code will work if 1 is pressed.
			for c,d in list(dictiona.items()): #Nested loop is used to check until the keys are equal to subtract their values.
				for e,f in list(d[1].items()):
					if a == e:
						b[0] = int(b[0]) - int(f)
						if int(b[0]) < 0:
							print('The recipe is successfully executed except for ' + a + ' since the amount of ingredients is not enough.') #This will prohibit from executing a recipe with not enough of amount of ingredients.
							#del d[1][e]
							b[0] = int(b[0]) + int(f) 
						if int(b[0]) <= 0:
							del dictionb[a] #Deletes a dictionary if its value reaches 0.
							#del d[1][e]
		return dictionb 
	elif choice == '2':
		
		return dictionb 

#For Supply Records Section ===================
def supplyMenu(): #Menu for supply
	print(Supply)
	print('[1] Add Supply')
	print('[2] Delete Supply')
	print('[3] Delete all Supply')
	print('[4] View Supply Record')
	print('[5] back to main menu')
	choice = input('Enter a number: ')
	return choice

def addRecord(dictionb, dictionc): #Function for adding a supply.
	itemlist = [] #Initialization of empty item list.
	checker = False #The checker will start as false.
	itemname = input('Please enter the item name: ')
	stock = int(input('Please enter item stock: '))
	itemlist.append (stock)
	price = float(input('Please enter item price:'))
	itemlist.append (price)
	suppliername = input('Please enter supplier name: ')
	for k,v in dictionc.items(): #This loop checks to make sure that the supplier name entered is in the supplier record.
		if suppliername == k:
			itemlist.append(suppliername)
			dictionb[itemname] = itemlist
			checker = True
			break
	if checker == False: #If the supplier is not in the record.
		print('Invalid Supplier')

	else:
		print('Supply Added!')
	return dictionb

def deleteRecord(dictionb): #Function for deleting a supply.
	itemname = input('Please enter item name: ')
	if itemname in dictionb: #Checks if the item is in the dictionary.
		del dictionb[itemname]
		print(itemname, 'is successfully deleted!')
	else:
		print('Error:', itemname, 'is not found.') #If item is not in the dictionary.

	return dictionb


def deleteallRecord(dictionb): #Deletes all the supplies in the record.
	dictionb.clear()
	print('All supply records are deleted.')
	return dictionb

def viewRecord(dictionb): #Function for viewing the supply record.
	if dictionb == {}: 
		print('There are no supply available.') #prints if the dictionary is empty.
	else:
		print(supplyRec)
		for k, v in dictionb.items():
			print('Item Name: ', k)
			print('Item Stock:', str(v[0]))
			print('Item Price:', str(v[1]))
			print('Associated Supplier:', v[2])
			print('')

#For Supplier Records ==============================
def supplierMenu():  #Menu for supplier.
	print(Supplier)
	print('[1] Add Supplier')
	print('[2] Delete Supplier')
	print('[3] Delete all Suppliers')
	print('[4] View Suppliers Record')
	print('[5] Back to main menu')
	print('')
	choice = input('Enter a number: ')
	return choice

def addSupplierRecord(dictionc): #Function for adding supplier to record.
	name = input('Please enter supplier name: ')
	contact = input('Please enter supplier contact: ')
	dictionc[name] = contact
	print('Supplier Added!')
	return dictionc

def deletesupplierRecord(dictionc): #Function for deleting supplier in the record.
	name = input('Please enter supplier name: ')
	if name in dictionc: #Checks if the name is in the record.
		del dictionc[name]
		print(name, 'is succesfully deleted!')
	else:
		print('Error:', name, 'is not found') #Prints if the name is not found in the record.
	return dictionc

def deleteallsupplierRecord(dictionc): #Function for deleting all the supplier record.
	dictionc.clear()
	print('All suppliers are deleted.')
	return dictionc

def viewsupplierRecord(dictionc): #Function for viewing the supplier record
	if dictionc == {}:
		print('There are no suppliers available.') #Prints if the dictionary is empty.
	else:
		print(supplierRec)
		for k,v in dictionc.items():
			print('Supplier Name:', k)
			print('Supplier Contact: ', v)
			print('')

def saveState(dictiona, dictionb, dictionc): #Function for saving all the information of recipe, supply and supplir.
	recipe = open('recipe.txt', 'w')
	supply = open('supply.txt', 'w')
	supplier = open('supplier.txt', 'w')

	#for recipe savestate
	lengthRecipe = 0 #Initialize
	lengthRecipeb = 0
	for k in dictiona: #Counts the length of the dictionary of recipe
		lengthRecipe += 1
	recipe.write(str(lengthRecipe) + '\n') #Writes the recipe length.
	lengthRecipe = 0
	for k,v in dictiona.items(): #Nested loop for writing all the information regarding recipes.
		recipe.write(k + '\n')
		recipe.write(v[0] + '\n')
		for c in v[1]:
			lengthRecipeb += 1
		recipe.write(str(lengthRecipeb) + '\n')
		lengthRecipeb = 0
		for i,j in v[1].items():
			recipe.write(i + '\n')
			recipe.write(str(j) + '\n')

	#for supply savestate
	lengthSupply = 0 #Initialize
	for z in dictionb:  #Counts the length of the dictionary of supplies.
		lengthSupply += 1
	supply.write(str(lengthSupply) + '\n') #Writes the length.
	for a,b in dictionb.items(): #Loop for writing the information of supply record.
		supply.write(a + '\n')
		supply.write(str(b[0]) + '\n')
		supply.write(str(b[1]) + '\n')
		supply.write(b[2]+ '\n')

	#for supplier savestate
	lengthSupplier = 0 #Initialize
	for y in dictionc: #Counts the length of supplier dictionary.
		lengthSupplier += 1
	supplier.write(str(lengthSupplier) + '\n') #Writes the length of the dictionary.
	for c,d in dictionc.items(): #loop for writing the keys and values of dictionary.
		supplier.write(c + '\n')
		supplier.write(d + '\n')
	print('Saved Successfuly!') #Prints once the saving process is complete.
	recipe.close()
	supply.close()
	supplier.close()


def loadState(): #Function for loading the information saved.
	recipe = open('recipe.txt', 'r')
	supply = open('supply.txt', 'r')
	supplier = open('supplier.txt', 'r')
	listx = []

	#load state for recipe
	lista = []     #Initialization of lists and dictionaries
	dictionarya = {}
	dictionaryb = {}
	lengthRecipe = recipe.readline()[:-1]
	for i in range(int(lengthRecipe)): #Nested loop for storing the information from the files in the dictionary.
		key = recipe.readline()[:-1]
		recipedesc = recipe.readline()[:-1]
		lista.append(recipedesc)
		recipeLength = recipe.readline()[:-1]
		for j in range(int(recipeLength)):
			item = recipe.readline()[:-1]
			amount = recipe.readline()[:-1]
			dictionaryb[item] = amount
		lista.append(dictionaryb)
		dictionarya[key] = lista 
		lista = [] #The list and dictionary will go back to empty one.
		dictionaryb = {}
	listx.append(dictionarya)

	#load state for supply
	cnta = 0 #Increment
	dictionaryaa = {} #Initialization of dictionary and list
	listaa = []
	lengthSupply = supply.readline()[:-1] #Reads the first line as the length of supply record.
	for i in range(int(lengthSupply)):#Nested loop for storing infos from files to dictionary of supplies.
		name = supply.readline()[:-1]
		for line in supply:
			if cnta < 2: #If else condition for storing supplies.
				info = (line[:-1])
				listaa.append(info)
				cnta += 1
			elif cnta == 2:
				info = (line[:-1])
				listaa.append(info)
				break
		cnta = 0
		dictionaryaa[name] = listaa #The list and dictionary will go back to empty one.
		listaa = []
	listx.append(dictionaryaa)

	#for supplier load state
	dictionaryaaa = {} #Initialization of dictionary and list.
	listaaa = []
	lengthsupplier = supplier.readline()[:-1] #Reads the first line as the length of supplier record.
	for i in range(int(lengthsupplier)): #Loop for  storing value from file to dictionary.
		suppliername = supplier.readline()[:-1]
		contact = supplier.readline()[:-1]
		dictionaryaaa[suppliername] = contact

	listx.append(dictionaryaaa)


	recipe.close()
	supply.close()
	supplier.close()
	print('Successfully Loaded!')  #Prints if all of the process of loading is completed.
	return listx


diction = {} #Initialization of main dictionaries and list.
dictionb = {}
dictionc = {}
listx = []

#ASCII art of texts
Menu = ("""
█▀▄▀█ ▄▀█ █ █▄░█   █▀▄▀█ █▀▀ █▄░█ █░█
█░▀░█ █▀█ █ █░▀█   █░▀░█ ██▄ █░▀█ █▄█                                                                      
""")

Recipe = ("""
█▀█ █▀▀ █▀▀ █ █▀█ █▀▀
█▀▄ ██▄ █▄▄ █ █▀▀ ██▄
""")

Supply = ("""
█▀ █░█ █▀█ █▀█ █░░ █▄█
▄█ █▄█ █▀▀ █▀▀ █▄▄ ░█░
""")

Supplier = ("""
█▀ █░█ █▀█ █▀█ █░░ █ █▀▀ █▀█
▄█ █▄█ █▀▀ █▀▀ █▄▄ █ ██▄ █▀▄
""")

recipeRec = ("""
█▀█ █▀▀ █▀▀ █ █▀█ █▀▀   █▀█ █▀▀ █▀▀ █▀█ █▀█ █▀▄
█▀▄ ██▄ █▄▄ █ █▀▀ ██▄   █▀▄ ██▄ █▄▄ █▄█ █▀▄ █▄▀
""")

supplyRec = ("""

█▀ █░█ █▀█ █▀█ █░░ █▄█   █▀█ █▀▀ █▀▀ █▀█ █▀█ █▀▄
▄█ █▄█ █▀▀ █▀▀ █▄▄ ░█░   █▀▄ ██▄ █▄▄ █▄█ █▀▄ █▄▀
""")

supplierRec = ("""
█▀ █░█ █▀█ █▀█ █░░ █ █▀▀ █▀█   █▀█ █▀▀ █▀▀ █▀█ █▀█ █▀▄
▄█ █▄█ █▀▀ █▀▀ █▄▄ █ ██▄ █▀▄   █▀▄ ██▄ █▄▄ █▄█ █▀▄ █▄▀
""")

execute = ("""
█▀▀ ▀▄▀ █▀▀ █▀▀ █░█ ▀█▀ █▀▀   █▀█ █▀▀ █▀▀ █ █▀█ █▀▀
██▄ █░█ ██▄ █▄▄ █▄█ ░█░ ██▄   █▀▄ ██▄ █▄▄ █ █▀▀ ██▄
""")


title = ("""

	░█████╗░███╗░░██╗███████╗░██████╗██╗  ███████╗░█████╗░░█████╗░██████╗░
	██╔══██╗████╗░██║██╔════╝██╔════╝██║  ██╔════╝██╔══██╗██╔══██╗██╔══██╗
	██║░░██║██╔██╗██║█████╗░░╚█████╗░██║  █████╗░░██║░░██║██║░░██║██║░░██║
	██║░░██║██║╚████║██╔══╝░░░╚═══██╗██║  ██╔══╝░░██║░░██║██║░░██║██║░░██║
	╚█████╔╝██║░╚███║███████╗██████╔╝██║  ██║░░░░░╚█████╔╝╚█████╔╝██████╔╝
	░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░╚═╝  ╚═╝░░░░░░╚════╝░░╚════╝░╚═════╝░

░█████╗░░█████╗░██████╗░██████╗░░█████╗░██████╗░░█████╗░████████╗██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
██║░░╚═╝██║░░██║██████╔╝██████╔╝██║░░██║██████╔╝███████║░░░██║░░░██║██║░░██║██╔██╗██║
██║░░██╗██║░░██║██╔══██╗██╔═══╝░██║░░██║██╔══██╗██╔══██║░░░██║░░░██║██║░░██║██║╚████║
╚█████╔╝╚█████╔╝██║░░██║██║░░░░░╚█████╔╝██║░░██║██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
""")








print(title) 
enter = input('                             Press ENTER To Continue.')
while True: #While it is true, the loop will goes on.
	choicea = mainMenu() #The variable will get the value of a function.
	if choicea == '1': #These will work if the choicea variable is 1
		while True:
			choice = recipeMenu() #This variable will get the value of recipeMenu() function.
			if choice == '1': #Calls addRecipe() function if 1 is pressed.
				diction = addRecipe(diction,dictionb)
			elif choice == '2': #Calls deleteRecipe() function if 2 is pressed.
				diction = deleteRecipe(diction)
			elif choice == '3': #Calls deleteAll() function if 3 is pressed.
				diction = deleteAll(diction)
			elif choice == '4': #Calls viewRecipe() function if 4 is pressed.
				if diction == {}:
					print('There are no Recipes.') #Prints if the dictionary is empty.
				else:
					viewRecipe(diction, dictionb, dictionc)
				press = input('Press ENTER to stop viewing. ')
			elif choice == '5': #Calls executeRecipe() function if 5 is pressed.
				if diction == {}:
					print("Please add recipe first")
				else:
					dictionb = executeRecipe(diction, dictionb)
			else:
				break #Stops the loop
	if choicea == '2':#These will work if 2 is entered.
		while True:
			choiceb = supplyMenu() #This variable will get the value of supplyMenu() function.
			if choiceb == '1': #Calls addRecord() function if 1 is pressed.
				dictionb = addRecord(dictionb, dictionc)
			elif choiceb == '2': #Calls deleteRecord() function if 2 is pressed.
				dictionb = deleteRecord(dictionb)
			elif choiceb == '3': #Calls deleteAllRecord() function if 3 is pressed.
				dictionb = deleteallRecord(dictionb)
			elif choiceb == '4': #Calls viewRecord() function if 5 is pressed.
				viewRecord(dictionb)
				press = input('Press ENTER to stop viewing. ')	
			else:
				break #stops the loop
	if choicea == '3': #These will work if 3 is entered.
		while True:
			choicec = supplierMenu() #This variable will get the value of supplierMenu() function.
			if choicec == '1': #Calls addSupplierRecord() function if 1 is pressed.
				dictionc = addSupplierRecord(dictionc)
			elif choicec == '2': #Calls deletesupplierRecord() function if 2 is pressed.
				dictionc = deletesupplierRecord(dictionc)
			elif choicec == '3': #Calls deleteallsupplierRecord() function if 3 is pressed.
				dictionc = deleteallsupplierRecord(dictionc)
			elif choicec == '4': #Calls viewsupplierRecord() function if 4 is pressed.
				viewsupplierRecord(dictionc)
				press = input('Press ENTER to stop viewing. ')
			else: 
				break #Stops the loop
	elif choicea == '4':  #The save state function will work if 4 is entered.
		saveState(diction, dictionb, dictionc) 

	elif choicea == '6': #The loop will stop if 6 is entered. Then the program wil stop.
		break  
	elif choicea == '5': 
		listx = loadState() #The listx variable will  get the returned value from loadState() function
		diction = listx[0] #The values inside the list will be distributed to the dictionaries using indexes.
		dictionb = listx[1]
		dictionc = listx[2]