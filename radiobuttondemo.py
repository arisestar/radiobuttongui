"""
program : radiobuttondemo.py
author :audrey 10/19/2020
chapter pg 283-284
simple GUI-based application that highlights the use of check boxes.
"""

from breezypythongui import EasyFrame
import tkinter.filedialog

class RadiobuttonDemo(EasyFrame):
	"""Allows the user to place a resturant order from a set of radio button options."""

	def __init__(self):
		"""Sets up the window and wedgets."""
		EasyFrame.__init__(self,title = "radio button demo", width = 300, height = 100)
		# add the label,button group, and buttons for meats
		self.addLabel(text = "Meat", row = 0, column = 0  )
		self .meatGroup = self.addRadiobuttonGroup(row = 1, column = 0, rowspan = 2 )

		defaultRB = self.meatGroup.addRadiobutton(text =" chicken")
		self.meatGroup.setSelectbutton(defaultRB)
		self.meatGroup.addRadiobutton(text = "Beef")

		# Add the label, button group, and buttons for potatoes
		self.addLabel(text ="potatoes", row =0 , column = 1,)
		self.taterGroup = self. addRadiobutton(row = 1, column = 1, rowspan = 2)
		defaultRB = self. taterGroup.addRadiobutton(text = "French fries")
		self.taterGroup.addRadiobutton( text = "Baked potato")

	#  add the label, button group, and buttons for veggies
	self.addLabel(text = "Vegetable", row = 0 , column = 2)
	self.vegGroup = self.addRadiobutton(row = 1, column = 2, rowspan = 2)
	defaultRB = self.vegGroup.addRadiobutton(text = "Applesauce")
	self.vegGroup.setSelectbutton(defaultRB)
	self.vegGroup.addRadiobutton(text = "Green Beans")

	self.addRadiobutton(text = "Place order", row = 3, column = 0,columnspan = 3, command = self.placeOrder)

# event handler method.
		""" display a message box with the order information."""
		message = ""
		message += self.meatGroup.getSelectedButton()["text"]+ "\n\n"
		message += self.taterGroup.getSelectedButton()["text"] + "\n\n"
		message += self.vegGroup.getSelectedButton()["text"] 
		self.messageBox(title = "Customer order", message = message)


	# definintion of the main function 
	def main():
		radiobuttomDemo().mainloop()
	
#global call to the main() function
main()
  