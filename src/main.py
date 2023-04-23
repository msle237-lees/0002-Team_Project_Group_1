import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from file_operations import FileOperations


class Lab7GroupProject(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the title of the main window and the size of the window.
        self.title("Lab 7 Group Project")
        self.geometry("360x240")

        # Add a menu item for "File".  
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu)

        # Under "File", add a "Close" choice, separator, and "Force close" choice to close the program.  
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Close", command=self.close_program)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Force close", command=self.force_close_program)

        # Obtain a filename of a text file from an input box 
        # and then open the file and read it into a string.
        self.file_name = tk.StringVar()
        self.file_name_entry = ttk.Entry(self, textvariable=self.file_name)
        self.file_name_entry.grid(row=0, column=0, padx=15, pady=15, columnspan=6, sticky="ew")
        self.file_name_entry.insert(0, "File name goes here")
        self.file_name_entry.bind("<FocusIn>", lambda event: self.file_name_entry.delete(0, tk.END))
        self.file_name_entry.bind("<Return>", lambda event: self.file_name_entry.focus())
        
        # Obtain a search string from an input box.
        self.search_string = tk.StringVar()
        self.search_string_entry = ttk.Entry(self,  textvariable=self.search_string)
        self.search_string_entry.grid(row=2, column=0, padx=15, pady=15, columnspan=6, sticky="ew")
        self.search_string_entry.insert(0, "Search string goes here")
        self.search_string_entry.bind("<FocusIn>", lambda event: self.search_string_entry.delete(0, tk.END))
        self.search_string_entry.bind("<Return>", lambda event: self.search_string_entry.focus())

        #Spinbox Num Entry
        self.nth=tk.IntVar()
        self.spin_label = ttk.Label(self, text="Nth word: ")
        self.spin=tk.Spinbox(self, from_=0, to=9, width=5, state='readonly')
        self.spin_label.grid(row=3, column=0, sticky="ew")
        self.spin.grid(row=3, column=1, sticky="ew")

        # and then search the text file for a string.  Create a button to accept all input and begin processing. 
        self.search_button = ttk.Button(self, text="Search", command=self.search_file)
        self.search_button.grid(row=4, column=0, sticky="ew")
        
        # Create a checkbox for case sensitivity on searching.
        self.case_sensitive = tk.BooleanVar()
        self.case_sensitive_checkbox = ttk.Checkbutton(self, text="Case sensitive", variable=self.case_sensitive)
        self.case_sensitive_checkbox.grid(row=4, column=1, padx=15, pady=15, columnspan=1, sticky="ew")

        # Show the total number of times the search matched in a box.  Show the total number of words in the file.
        self.total_matches_label = ttk.Label(self, text="Total matches:")
        self.total_matches_label.grid(row=5, column=0, padx=15, pady=15, columnspan=1, sticky="ew")
        
        self.total_matches = tk.StringVar()
        self.total_matches.set("0")
        self.total_matches_label = ttk.Label(self, textvariable=self.total_matches)
        self.total_matches_label.grid(row=5, column=3, padx=15, pady=15, columnspan=1, sticky="ew")

        # Trap the X close button event from the window and pop up a yes/no message box "Really quit?".
        # If the user clicks "Yes", close the program.  If the user clicks "No", do nothing.
        self.protocol("WM_DELETE_WINDOW", self.close_program)

        # Create a button to optionally save the results to a file with a filename specified in a box on a pop up window.
        self.save_button = ttk.Button(self, text="Save", command=self.save_file)
        self.save_button.grid(row=4, column=3, sticky="ew")

        # Trap the enter key to move the cursor to next box
        self.file_name_entry.bind('<Return>', self.focusDown)

        # For example, assume the source file has "the Senate has 100 members" in it; if the search term entered is 
        # "the" and n is 0, add "the" to your internal list; if the search term entered is "the" and n is 1, add "Senate" 
        # to your internal list; if the search term entered is "the" and n is 2, add "has" to your internal list, etcetera.

    # For "Close", pop up the yes/no message box confirmation for "Really quit?".  
    def close_program(self):
        if messagebox.askyesno("Really quit?", "Are you sure you want to quit?"):
            self.destroy()
    
    # For "Force close", immediately close the program without confirmation.
    def force_close_program(self):
        self.destroy()

    def search_file(self):
        file_operations = FileOperations()
        status = file_operations.open_file(self.file_name.get())
        if status:
            data = file_operations.search_file(self.search_string.get(), self.case_sensitive.get())
            self.total_matches.set(len(data))
        else:
            self.total_matches.set("File open failure")

    def save_file(self):
        file_name = filedialog.asksaveasfilename()
        file_operations = FileOperations()
        file_operations.save_data_to_file(file_name, self.total_matches.get())
    # For enter key bind, will move focus to second textbox if first textbox is focused when enter key is pressed
    def focusDown(self, *args):
        self.search_string_entry.focus()
if __name__ == "__main__":
    app = Lab7GroupProject()
    app.mainloop()
