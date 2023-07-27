import tkinter as tk
r = tk.Tk()
r.title('Corso Talent')
button = tk.Button(r, text='ole', width=25, command=r.destroy)
button.pack()
r.mainloop()