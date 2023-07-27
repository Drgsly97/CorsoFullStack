from tkinter import *
from tkinter import ttk
from calendar import month_name

master=Tk()
master.title("Combobox")
master.geometry("400x600")

mese_selezionato=StringVar()
mesi_combobox = ttk.Combobox(master,textvariable=mese_selezionato)
mesi_combobox['values']=[month_name[m] for m in range(1,13)]

mesi_combobox.pack(fill=X, pady=5,padx=5)

mainloop()