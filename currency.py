from tkinter import *
from tkinter import ttk

from tbc_parser import TBC_parser
from gb_parser import GB_parser
from eb_parser import EB_parser



def convert(event):

	currency_values = None
	currency_type = None
	c_val = None

	label_error.place_forget()


	if bank_var.get() == 1:
		currency_values = EB_parser()
		
	elif bank_var.get() == 2:
		currency_values = TBC_parser()

	elif bank_var.get() == 3:
		currency_values = GB_parser()


	if currency_entry.get():
		c_val = currency_entry.get()

		for i in c_val:
			if i == ",":
				c_val = c_val.replace(f"{i}", ".")

		try:
			c_val = float(c_val)

		except:
			label_error.place(x = 40, y = 120, height = 50)


	else:
		gel_converted_buy.configure(text='0.00')
		gel_converted_sell.configure(text='0.00')

		d_converted_buy.configure(text='0.00')
		d_converted_sell.configure(text='0.00')

		e_converted_buy.configure(text='0.00')
		e_converted_sell.configure(text='0.00')



	if c_val and currency_var.get() and bank_var.get():
		if currency_var.get() == 1:
			gel_converted_buy.configure(text=f'{round(c_val*1, 4)}')
			gel_converted_sell.configure(text=f'{round(c_val*1, 4)}')

			d_converted_buy.configure(text=f'{round(c_val/currency_values[0][0], 4)}')
			d_converted_sell.configure(text=f'{round(c_val/currency_values[0][1], 4)}')

			e_converted_buy.configure(text=f'{round(c_val/currency_values[1][0], 4)}')
			e_converted_sell.configure(text=f'{round(c_val/currency_values[1][1], 4)}')


		elif currency_var.get() == 2:
			gel_converted_buy.configure(text=f'{round(c_val*currency_values[0][0], 4)}')
			gel_converted_sell.configure(text=f'{round(c_val*currency_values[0][1], 4)}')

			d_converted_buy.configure(text=f'{round(c_val*1, 4)}')
			d_converted_sell.configure(text=f'{round(c_val*1, 4)}')

			e_converted_buy.configure(text=f'{round((c_val*currency_values[0][0]) / currency_values[1][0], 4)}')
			e_converted_sell.configure(text=f'{round((c_val*currency_values[0][0]) / currency_values[1][1], 4)}')


		elif currency_var.get() == 3:
			gel_converted_buy.configure(text=f'{round(c_val*currency_values[1][0], 4)}')
			gel_converted_sell.configure(text=f'{round(c_val*currency_values[1][1], 4)}')

			d_converted_buy.configure(text=f'{round((c_val*currency_values[1][0]) / currency_values[0][0], 4)}')
			d_converted_sell.configure(text=f'{round((c_val*currency_values[1][0]) / currency_values[0][1], 4)}')

			e_converted_buy.configure(text=f'{round(c_val*1, 4)}')
			e_converted_sell.configure(text=f'{round(c_val*1, 4)}')



def change():
	convert(None)



window = Tk()

window.geometry('540x400+600+90')
window.resizable(False, False)  
window.title("Currency Calculator")


label_error = Label(window, text = "გთხოვთ, შეიყვანეთ რიცხვი!", font = ("Arial", 11))

title_label = ttk.Label(window, text = "Currency Calculator", font = ("Arial", 20))
title_label.place(x = 160, y = 5, height = 50)


# entry
entry_label = Label(window, text = "შეიყვანეთ თანხა: ", font = ("Arial", 11))
entry_label.place(x = 40, y = 160, height = 30)

currency_entry = ttk.Entry(window, width = 27)
currency_entry.place(x = 180, y = 160, height = 30)
currency_entry.bind("<KeyRelease>", convert)



bank_var = IntVar()
currency_var = IntVar()

# bank radiobuttons
e_bank = ttk.Radiobutton(window, text="ეროვნული ბანკი", variable=bank_var, value=1, command = change)
e_bank.place(x = 60, y = 50, height = 40)

tbc_bank = ttk.Radiobutton(window, text="თიბისი ბანკი", variable=bank_var, value=2, command = change)
tbc_bank.place(x = 200, y = 50, height = 40)

g_bank = ttk.Radiobutton(window, text="საქართველოს ბანკი", variable=bank_var, value=3, command = change)
g_bank.place(x = 330, y = 50, height = 40)



# currency type radiobuttons
GEL = ttk.Radiobutton(window, text="ლარი", variable=currency_var, value=1, command = change)
GEL.place(x = 150, y = 80, height = 40)

USD = ttk.Radiobutton(window, text="აშშ დოლარი", variable=currency_var, value=2, command = change)
USD.place(x = 220, y = 80, height = 40)

EURO = ttk.Radiobutton(window, text="ევრო", variable=currency_var, value=3, command = change)
EURO.place(x = 340, y = 80, height = 40)



# converted currency type titles
gel_converted_title = ttk.Label(window, text = "ლარი:", font = ("Arial", 12))
gel_converted_title.place(x = 30, y = 240, height = 30)
gel_converted_title.configure(state='disabled')

dollar_converted_title = ttk.Label(window, text = "აშშ დოლარი:", font = ("Arial", 12))
dollar_converted_title.place(x = 30, y = 270, height = 30)
dollar_converted_title.configure(state='disabled')

euro_converted_title = ttk.Label(window, text = "ევრო:", font = ("Arial", 12))
euro_converted_title.place(x = 30, y = 300, height = 30)
euro_converted_title.configure(state='disabled')


# buy / sell titles
buy_label = ttk.Label(window, text = "ყიდვა", font = ("Arial", 12))
buy_label.place(x = 200, y = 200, height = 30)

sell_label = ttk.Label(window, text = "გაყიდვა", font = ("Arial", 12))
sell_label.place(x = 350, y = 200, height = 30)


# cconverted currency amount labels 
# GEL buy/sell
gel_converted_buy = ttk.Label(window, text = "0.00", font = ("Arial", 12))
gel_converted_buy.place(x = 200, y = 240, height = 30)
gel_converted_buy.configure(state='disabled')

gel_converted_sell = ttk.Label(window, text = "0.00", font = ("Arial", 12))
gel_converted_sell.place(x = 350, y = 240, height = 30)
gel_converted_sell.configure(state='disabled')


# DOLLAR buy/sell
d_converted_buy = ttk.Label(window, text = "0.00", font = ("Arial", 12))
d_converted_buy.place(x = 200, y = 270, height = 30)
d_converted_buy.configure(state='disabled')

d_converted_sell = ttk.Label(window, text = "0.00", font = ("Arial", 12))
d_converted_sell.place(x = 350, y = 270, height = 30)
d_converted_sell.configure(state='disabled')


# EURO buy/sell
e_converted_buy = ttk.Label(window, text = "0.00", font = ("Arial", 12))
e_converted_buy.place(x = 200, y = 300, height = 30)
e_converted_buy.configure(state='disabled')

e_converted_sell = ttk.Label(window, text = "0.00", font = ("Arial", 12))
e_converted_sell.place(x = 350, y = 300, height = 30)
e_converted_sell.configure(state='disabled')


window.mainloop()  