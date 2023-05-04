from tkinter import *
 
class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
 
        self.title("Twitch Downloader")
        
        self.minsize(500,400)
        self.maxsize(500,400)
        self.download_button = Button(self, text="Download")
        
        # Configure the button widget to be bigger, longer, and purple
        self.download_button.config(font=("Arial Bold", 16), fg="white", bg="purple", width=15, height=1)
        
        # Pack the button widget onto the root window
        #self.download_button.place(x=250, y=300)
        self.download_button.pack(side=BOTTOM, anchor=S, padx=10, pady=10)


          # Create a label widget for the file name
        self.filename_label = Label(self, text="Enter a file name:")

        # Create an entry widget for the file name
        self.filename_entry = Entry(self)

        # Create a label widget for the first dropdown menu
        self.dropdown1_label = Label(self, text="Select an Game section:")

        # Create a list of options for the first dropdown menu
        options1 = ["Option 1", "Option 2", "Option 3"]

        # Create a variable to store the selected option from the first dropdown menu
        self.selected_option1 = StringVar()

        # Set the default value of the variable to the first option in the list
        self.selected_option1.set(options1[0])

        # Create a dropdown menu for the first option
        self.dropdown1 = OptionMenu(self, self.selected_option1, *options1)

        # Create a label widget for the second dropdown menu
        self.dropdown2_label = Label(self, text="Select another option:")

        # Create a list of options for the second dropdown menu
        options2 = ["Option A", "Option B", "Option C"]

        # Create a variable to store the selected option from the second dropdown menu
        self.selected_option2 = StringVar()

        # Set the default value of the variable to the first option in the list
        self.selected_option2.set(options2[0])

        # Create a dropdown menu for the second option
        self.dropdown2 = OptionMenu(self, self.selected_option2, *options2)

        # Pack the widgets onto the root window
        self.filename_label.pack(pady=10)
        self.filename_entry.pack(pady=5)
        self.dropdown1_label.pack(pady=10)
        self.dropdown1.pack(pady=5)
        self.dropdown2_label.pack(pady=10)
        self.dropdown2.pack(pady=5)

root = Root()
root.mainloop()