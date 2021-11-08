dict = {}
Attr = [ "Name : " , "Blood_group : " , "Pincode : " , "Email : " , "Phone : "]

Index = {"Name" : 0 , "Blood_group" : 1 , "Email" : 3 , "Phone" : 4, "Pincode" :2}
def file_open():
	file = open("DATA.txt", "r")
	for line in file:
		line = line[:-1]
		line = line.split(":")
		key = line[0]
		value = line[1].split(",")
		
		dict[key] = value
	file.close()
	
def write(Adhar_ID , Name , Blood_group , Pincode , Email ,Phone):
	if Adhar_ID in dict :
		return -1 
	file = open("DATA.txt", "a")
	Value = f"{Adhar_ID}:{Name},{Blood_group},{Pincode},{Email},{Phone}\n"
	file.write(Value)
	file.close()
	return 1
	
def Delete(Adhar_number):
	with open("DATA.txt","r") as f:
		lines = f.readlines()
	with open("DATA.txt", "w") as f:
		for line in lines:
			list = line.split(":")
			if list[0] == Adhar_number :
				pass
			else:
				f.write(line)
	global dict
	dict = {}
	
def Modify(Adhar_number, Attribute , Modified ):
	with open("DATA.txt","r") as f:
		lines = f.readlines()
	with open("DATA.txt", "w") as f:
		for line in lines:
			list = line.split(":")
			if list[0] == Adhar_number :
				value = list[1]
				value = value[:-1]
				value = value.split(",")
				value[Index[Attribute]] = Modified
				line = f"{list[0]}:{value[0]},{value[1]},{value[2]},{value[3]},{value[4]}\n"
			f.write(line)

def Clear():
	with open("DATA.txt","w") as f:
		pass
	global dict 
	dict = {}
	
	
def view_Blood_group( Blood_group , Pincode):
	output = ""
	for key in dict:
		value = dict[key] 
		if value[1] == Blood_group and value[2] == Pincode :
			output += f"{key} : {value[0]}\n"
		
	if output == "" :
		return 5
		
	return output 
	
	
	
def view_total():
	output = ""
	count = 0
	for key in dict:
		value = dict[key] 
		output += f"{key} : {value[0]}\n"
		count += 1
	output = f"Total Patients : {count} \n" + output
	return output 
	
	
def view(Adhar_number):
	output = ""
	value = dict.get(Adhar_number,[]) 
	if value == []:
		output = "\nThere is no such Patient in the data .\n\n Pls Ensure that Adhar_number is correct ."
		return output
	for i in range(5):
		output += Attr[i] + value[i] + "\n"
		
	return output
	

