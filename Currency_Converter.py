import requests
from tkinter import *
from tkinter import messagebox

# Get exchange rates
def get_rates():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    if response.status_code != 200:
        messagebox.showerror("Error", "Unable to fetch exchange rates!")
        return None
    return response.json()["rates"]

# Convert currency
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        if from_currency == to_currency:
            messagebox.showinfo("Result", f"{amount} {from_currency} is {amount} {to_currency}")
            status_label.config(text=f"Converted {amount} {from_currency} to {amount} {to_currency}", fg='green')
            return
        
        rates = get_rates()
        if rates is None:
            return
        
        from_rate = rates[from_currency]
        to_rate = rates[to_currency]

        converted_amount = amount * (to_rate / from_rate)
        messagebox.showinfo("Result", f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}")
        status_label.config(text=f"Converted {amount} {from_currency} to {converted_amount:.2f} {to_currency}", fg='green')
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the amount!")
        status_label.config(text="Invalid input. Please enter a number.", fg='red')

# Main window
root = Tk()
root.title("Currency Converter")
root.geometry("400x400")
root.config(bg='#282C34')

# Title label
title_label = Label(root, text="Currency Converter", font=("Arial", 18, "bold"), bg='#61AFEF', fg='white', padx=10, pady=10)
title_label.pack(pady=10, fill=X)

# Amount entry
amount_label = Label(root, text="Amount:", font=("Arial", 12), bg='#282C34', fg='white')
amount_label.pack(pady=10)
amount_entry = Entry(root, font=("Arial", 14), justify='center', borderwidth=2, relief='groove', width=20)
amount_entry.pack(pady=10)

# Currency options
currency_options = ["USD", "EUR", "INR", "JPY", "GBP", "CAD"]

# From currency
from_currency_var = StringVar(root)
from_currency_var.set("USD")
from_label = Label(root, text="From Currency:", font=("Arial", 12), bg='#282C34', fg='white')
from_label.pack()
from_menu = OptionMenu(root, from_currency_var, *currency_options)
from_menu.config(font=("Arial", 10), bg='#61AFEF', fg='white', padx=10, pady=5, borderwidth=2)
from_menu.pack(pady=5)

# To currency
to_currency_var = StringVar(root)
to_currency_var.set("INR")
to_label = Label(root, text="To Currency:", font=("Arial", 12), bg='#282C34', fg='white')
to_label.pack()
to_menu = OptionMenu(root, to_currency_var, *currency_options)
to_menu.config(font=("Arial", 10), bg='#61AFEF', fg='white', padx=10, pady=5, borderwidth=2)
to_menu.pack(pady=5)

# Convert button with hover effect
def on_enter(e):
    convert_button.config(bg='#4CAF50')

def on_leave(e):
    convert_button.config(bg='#61AFEF')

convert_button = Button(root, text="Convert", font=("Arial", 12, "bold"), bg='#61AFEF', fg='white', command=convert_currency)
convert_button.pack(pady=20)
convert_button.bind("<Enter>", on_enter)
convert_button.bind("<Leave>", on_leave)

# Status bar
status_label = Label(root, text="", font=("Arial", 10), bg='#282C34', fg='white')
status_label.pack(side=BOTTOM, fill=X)

# Run the application
root.mainloop()