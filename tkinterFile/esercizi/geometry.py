width = 600 # Width
height = 300 # Height

screen_width = master.winfo_screenwidth()  # Width of the screen
screen_height = master.winfo_screenheight() # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

master.geometry('%dx%d+%d+%d' % (width, height, x, y))