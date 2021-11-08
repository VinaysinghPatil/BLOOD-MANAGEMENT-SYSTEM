from tkinter import *
from tkinter import messagebox
import functions
#import blood_bank
#db=blood_bank.connect("localhost","asus","123","blood_bank")
#cursor=db.cursor()

class App(Tk):
	def __init__(self):
		Tk.__init__(self)
		self._frame = None
		self.title(" PATIENT FORM ")
		self.switch(Menu)
		self.geometry('700x700')
		self.config(bg = "light blue")

	def switch(self, frame_class):
		"""Destroys current frame and replaces it with a chosen by the user"""
		new_frame = frame_class(self)
		if self._frame is not None:
			self._frame.destroy()
		self._frame = new_frame
		self._frame.pack()

class Menu(Frame):
	"""Main menu"""
	def __init__(self, master):
		Frame.__init__(self, master)
		functions.file_open()
		self.config(bg = "light yellow")
		"""Frame widgets"""
		label = Label(self, font = ('elephant',(30)),text = "PATIENT FORM !\n Choose an option.", bg = "white", fg = "blue")
		label.pack()
		button = Button(self, text = "View details",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Details))
		button.pack(padx = 10, pady = 10)
		button2 = Button(self, text = "New Patient",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(File_Write))
		button2.pack(padx = 10, pady = 10)
		
		button6 = Button(self, text = "Modify",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Modify) )
		button6.pack(padx = 10, pady = 10)
		
		button7 = Button(self, text = "Delete",font = ('Times new roman',(30)),bg = "red", width = 20, command = lambda: master.switch(Delete) )
		button7.pack(padx = 10, pady = 10)
		
		button4 = Button(self, text = "View Blood_group wise ",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(View_Blood_group) )
		button4.pack(padx = 10, pady = 10)
		button5 = Button(self, text = "Total Registered",font = ('Times new roman',(30)),bg = "white", width = 20, command = lambda: master.switch(Total) )
		button5.pack(padx = 10, pady = 10)
		
		button3 = Button(self, text = "Exit",font = ('Times new roman',(30)),bg = "white", width = 20, command = self.close)
		button3.pack(padx = 10, pady = 10)

	def close(self):
		"""Close the app"""
		self.destroy()
		exit()

class Delete(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.config(bg = "light yellow")
		
		def on_click():
			"""Checking data and writing the results"""
			Adhar_number = entry_Adhar_number.get()
			Error = False
			# Condtions remained to be added 
			if Adhar_number.isdecimal() :
				pass
			else:
				Error = True
			if Error == True:
				messagebox.showerror("Error", "Please enter correct data!")
			else:
				functions.Delete(Adhar_number)
				messagebox.showinfo( "Status" , " Information Deleted Successfully !")
				entry_Adhar_number.get().delete(0,END)

				
		"""Frame widgets"""
		label = Label(self, text ="Enter the Adhar_number of patient ",font = ('Elephant',(30)), bg = "yellow", fg = "black")
		label.pack()
		# user input, product
		label2 = Label(self, text = "Adhar_number : ",font = ('times new roman',(25)), width= 20, bg = "pink", fg = "black")
		label2.pack()
		entry_Adhar_number = Entry(self, width = 35,font = ('times new roman',(20)), bg = "white")
		entry_Adhar_number.pack()
		
		submit = Button(self, text = "Submit",font = ('times new roman',(25)), bg = "red" , width = 8, command = on_click)
		submit.pack(padx = 10, pady = 10)
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = lambda: master.switch(Menu))
		self.button.pack(padx = 10, pady = 10)
class Modify(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		attribute_list = [ "Name" , "Blood_group" , "Email" , "Phone" , "Pincode" ]
		
		def on_click():
			"""Checking data and writing the results"""
			Adhar_number = entry_Adhar_number.get()
			value = value_inside.get()
			modified = entryModify.get()
	
			Error = False
			# Condtions remained to be added 
			if Adhar_number.isdecimal() :
				pass
			else:
				Error = True
			if Error == True:
				messagebox.showerror("Error", "Please enter correct data!")
			else:
				functions.Modify( Adhar_number,value,modified)
				messagebox.showinfo( "Status" , " Information modified Successfully !")
				entry_Adhar_number.delete(0,END)
				
				entryModify.delete(0,END)
				
		"""Frame widgets"""
		label = Label(self, text ="Enter the Adhar number of patient ",font = ('Elephant',(30)), bg = "light blue", fg = "red")
		label.pack()
		# user input, product
		label2 = Label(self, text = "Adhar number : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label2.pack()
		entry_Adhar_number = Entry(self, width = 35,font = ('times new roman',(20)), bg = "white")
		entry_Adhar_number.pack(padx = 20, pady = 20)
		
		value_inside = StringVar(self)
		value_inside.set("Select the Attribute")
		question_menu = OptionMenu(self,value_inside,*attribute_list ).pack()
		
		label3 = Label(self, text = "Modified value : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label3.pack()
		entryModify = Entry(self, width = 35,font = ('times new roman',(20)), bg = "white")
		entryModify.pack(padx = 20, pady = 20)
		
		submit = Button(self, text = "Submit",font = ('times new roman',(25)), bg = "light yellow" ,width = 8, command = on_click)
		submit.pack(padx = 20, pady = 20)
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = lambda: master.switch(Menu))
		self.button.pack(padx = 20, pady = 20)


class Details(Frame):
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.config(bg = "light blue")

		def on_click():
			"""Checking data and writing the results"""
			Adhar_number =  entry_Adhar_number.get()
			output.delete(0.0, END)

			Error = False
            
			# Condtions remained to be added 
			if Adhar_number.isdecimal() :
				pass
			else:
				Error = True
			if Error == True:
				messagebox.showerror("Error", "Please enter correct data!")
			else:
				
				output.insert(END, functions.view(Adhar_number))
				
		"""Frame widgets"""
		label = Label(self, text ="Enter the  Adhar_number of patient",font = ('Elephant',(30)), bg = "light blue", fg = "black")
		label.pack()
		# user input, product
		label2 = Label(self, text = " Adhar_number: ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label2.pack()
		entry_Adhar_number = Entry(self, width = 35,font = ('times new roman',(20)), bg = "white")
		entry_Adhar_number.pack()
		    
		submit = Button(self, text = "Submit",font = ('times new roman',(25)), width = 8, bg = "light yellow" , command = on_click)
		submit.pack(padx = 10, pady = 10)

		output = Text(self, width = 40,font = ('times new roman',(25)), height = 6, wrap = WORD, bg = "white")
		output.pack()
		    
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = lambda: master.switch(Menu))
		self.button.pack(padx = 10, pady = 10)


class Total(Frame):
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.config(bg = "light blue")
		
		label = Label(self, text ="Total Patients Registered",font = ('Elephant',(30)), bg = "light blue", fg = "red")
		label.pack()
		

		output = Text(self, width = 40,font = ('times new roman',(25)), height = 20, wrap = WORD, bg = "white")
		output.pack()
		
		output.delete(0.0, END)
		message = functions.view_total()
		
		output.insert(END, message)
				
		"""Frame widgets"""
		
		    
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = lambda: master.switch(Menu))
		self.button.pack(padx = 10, pady = 10)
		

class View_Blood_group(Frame):
	
	def __init__(self, master):
		Frame.__init__(self, master)
		self.config(bg = "light blue")

		def on_click():
			"""Checking data and writing the results"""
			Blood_group = entryBlood_group.get()
			Pincode = Diventry.get()
			output.delete(0.0, END)

			Error = False
            
			#Condtions remained to be added 
			if Pincode.isdecimal() :
				pass
			else:
				Error = True
			if Error == True:
				messagebox.showerror("Error", "Please enter Pincode in Numeric form !")
			else:
				message = functions.view_Blood_group(Blood_group,Pincode)
				if message == 5:
					message = "\n \t There is no such Blood_group\n\t\tor there is no such Pincode "
				output.insert(END, message)
				
		"""Frame widgets"""
		label = Label(self, text ="Enter the Blood_group of Patient",font = ('Elephant',(30)), bg = "light blue", fg = "red")
		label.pack()
		# user input, product
		label2 = Label(self, text = "Blood_group : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label2.pack()
		
		entryBlood_group = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		entryBlood_group.pack()
		
		label3 = Label(self, text = "Pincode : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label3.pack()
		
		Diventry = Entry(self, width = 20,font = ('times new roman',(20)), bg = "white")
		Diventry.pack()
		    
		submit = Button(self, text = "View Patients",font = ('times new roman',(25)), width = 20, bg = "light yellow", command = on_click)
		submit.pack(padx = 10, pady = 10)

		output = Text(self, width = 40,font = ('times new roman',(25)), height = 10, wrap = WORD, bg = "white")
		output.pack()
		    
		self.button = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = lambda: master.switch(Menu))
		self.button.pack(padx = 10, pady = 10)
		

class File_Write(Frame):

	def __init__(self, master):
		Frame.__init__(self, master)
		self.config(bg = "light blue")

		def validate():
			"""Checks is the user inputs correct data"""
			error = False
			Adhar_ID = Adhar_numberEntry.get()
			Name = NameEntry.get()
			Blood_group = Blood_groupEntry.get()
			Pincode = PincodeEntry.get()
			Email = EmailEntry.get()
			Phone = PhoneEntry.get()
			message = ""
			if Adhar_ID.isdecimal() and Phone.isdecimal():
				pass
			else:
				error = True
				message += " \"Adhar_ID/ Phone \" cannot include alphabet ! \n\n"
				
			if Pincode.isdecimal():
				pass
			else:
				error = True
				message += "Pls Enter Pincode in Numeric form ( 1, 2, 3, ... )! \n\n"
			if "@" not in Email :
				error = True
				message += "Pls Enter proper Email address !"
		
			if error == True:
				messagebox.showerror("Error",message)
			else:
				#writing to a file
				success = functions.write(Adhar_ID , Name , Blood_group , Pincode , Email ,Phone)
				if success == -1:
					messagebox.showerror("Error", "That Adhar_ID is already registered !")
				#Emptying inputs
				NameEntry.delete(0, END)
				Adhar_numberEntry.delete(0, END)
				Blood_groupEntry.delete(0, END)
				PincodeEntry.delete(0, END)
				EmailEntry.delete(0, END)
				PhoneEntry.delete(0, END)

		"""Frame widgets"""
		label = Label(self,font = ('Elephant',(30)), bg = "light blue", fg = "black", text ="Enter the details ")
		label.pack()
		
		label2 = Label(self, text = "Adhar_ID : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label2.pack()
		Adhar_numberEntry= Entry(self,font = ('times new roman',(20)), width = 35, bg = "white")
		Adhar_numberEntry.pack()
		
		label1 = Label(self, text = "Name : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label1.pack()
		NameEntry = Entry(self, width = 35,font = ('times new roman',(20)), bg = "white")
		NameEntry.pack()

		

		label3 = Label(self, text = "Blood_group : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label3.pack()
		Blood_groupEntry = Entry(self,font = ('times new roman',(20)), width = 15, bg = "white")
		Blood_groupEntry.pack()

		label4 = Label(self, text = "Pincode : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label4.pack()
		PincodeEntry = Entry(self, width = 25,font = ('times new roman',(20)), bg = "white")
		PincodeEntry.pack()

		label5 = Label(self, text = "Email : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label5.pack()
		EmailEntry = Entry(self, width = 35,font = ('times new roman',(20)), bg = "white")
		EmailEntry.pack()

		label6 = Label(self, text = "Phone : ",font = ('times new roman',(25)), bg = "light blue", fg = "black")
		label6.pack()
		PhoneEntry = Entry(self, width = 35,font = ('times new roman',(20)), bg = "white")
		PhoneEntry.pack()

		submit = Button(self, text = "Submit",font = ('times new roman',(25)), width = 8, bg= "light yellow", command = validate)
		submit.pack(padx = 10, pady = 10)

		button3 = Button(self, text = "Back",font = ('times new roman',(25)), width = 8, command = lambda: master.switch(Menu))
		button3.pack(padx = 10, pady = 10)


if __name__ == "__main__":
    app = App()
    app.mainloop()

