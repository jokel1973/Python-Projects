##
##
##import tkinter as tk
##from tkinter import *
##
##
##class ParentWindow(Frame):
##    def __init__(self, master):
##        Frame.__init__(self, master)
##        # Sets title of GUI window
##        self.master.title("File Transfer")
##
##
##if __name__ == "__main__":
##    root = tk.Tk()  # Correcting the case of Tk()
##    App = ParentWindow(root)
##    root.mainloop()
##
##
##import datetime
##
##class ParentWindow(Frame):
##    # ... (rest of the code remains unchanged)
##
##    def transferFiles(self):
##        # Gets source directory
##        source = self.source_dir.get()
##        # Gets destination directory
##        destination = self.destination_dir.get()
##        # Gets the current time
##        current_time = datetime.datetime.now()
##
##        # Gets a list of files in the source directory
##        source_files = os.listdir(source)
##
##        # Runs through each file in the source directory
##        for i in source_files:
##            # Gets the full path of the file
##            file_path = os.path.join(source, i)
##
##            # Gets the modification time of the file
##            file_modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
##
##            # Calculates the time difference between current time and modification time
##            time_difference = current_time - file_modification_time
##
##            # Checks if the file has been modified within the last 24 hours
##            if time_difference.total_seconds() <= 24 * 3600:
##                # Moves the file from the source to the destination
##                shutil.move(file_path, destination)
##                print(f"{i} was successfully transferred.")
##            else:
##                print(f"{i} was not transferred as it is older than 24 hours.")
##
##
##
##
##def transferFiles(self):
##    # Gets source directory
##    source = self.source_dir.get()
##    # Gets destination directory
##    destination = self.destination_dir.get()
##    # Gets a list of files in the source directory
##    file_names = os.listdir(source)
##    # Runs through each file in the source directory
##    for file_name in file_names:
##        # Gets the full path of the file
##        file_path = os.path.join(source, file_name)
##
##        # Gets the modification time of the file
##        file_modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
##
##        # Calculates the time difference between current time and modification time
##        time_difference = datetime.datetime.now() - file_modification_time
##
##        # Checks if the file has been modified within the last 24 hours
##        if time_difference.total_seconds() <= 24 * 3600:
##            # moves each file from the source to the destination
##            shutil.move(file_path, destination)
##            print(f"{file_name} was successfully transferred.")
##
##
##    def transferFiles(self):
##        #Gets source directory
##        source = self.source_dir.get()
##        #Gets destination directory
##        destination = self.destination_dir.get()
##        #Gets a list of files in the source directory
##        file_path = os.listdir(source)
##        #Runs through each file in the source directory
##        for i in file_path:
##            # Gets the modification time of the file
##            file_modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
##
##            # Calculates the time difference between current time and modification time
##            time_difference = current_time - file_modification_time
##
##            # Checks if the file has been modified within the last 24 hours
##            if time_difference.total_seconds() <= 24 * 3600:
##                #moves each file from the source to the destination
##                shutil.move(source + '/' + i, destination)
##                print(i + ' was successfully transferred.')
##

##import tkinter as tk
##from tkinter import *
##import webbrowser
##
##class ParentWindow(Frame):
##    def __init__(self, master):
##        Frame.__init__(self, master)
##        self.master.title("Web Page Generator")
##
##        # Create the button and configure its properties
##        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
##        # Grid the button properly
##        self.btn.grid(padx=(10, 10), pady=(10, 10))
##
##    # Define the defaultHTML method as a method of the class
##    def defaultHTML(self):
##        htmlText = "Stay tuned for our amazing summer sale!"
##        htmlFile = open("index.html", "w")
##        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
##        htmlFile.write(htmlContent)
##        htmlFile.close()
##        webbrowser.open_new_tab("index.html")
##
##        
##
##if __name__ == "__main__":
##    root = tk.Tk()
##    App = ParentWindow(root)
##    root.mainloop()


import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # Entry widget for custom text input
        self.custom_text_entry = Entry(self.master, width=40)
        self.custom_text_entry.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0))

        # Create the button and configure its properties
        self.default_btn = Button(self.master, text="Default HTML Page", width=20, height=2, command=self.defaultHTML)
        self.default_btn.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

        # Create a button for custom HTML Page
        self.custom_btn = Button(self.master, text="Custom HTML Page", width=20, height=2, command=self.customHTML)
        self.custom_btn.grid(row=1, column=1, padx=(10, 10), pady=(10, 10))

    # Define the defaultHTML method as a method of the class
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        self.generateHTML(htmlText)

    # Define a method to handle custom HTML generation
    def customHTML(self):
        custom_text = self.custom_text_entry.get()
        # Use default text if custom text is empty
        htmlText = custom_text if custom_text else "Stay tuned for our amazing summer sale!"
        self.generateHTML(htmlText)

    # Define a method to generate HTML and open it in a new tab
    def generateHTML(self, htmlText):
        htmlFile = open("index.html", "w")
        htmlContent = f"<html>\n<body>\n<h1>{htmlText}</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        # Label providing instructions
        label_instructions = Label(self.master, text="Enter Custom text or click the Default HTML button")
        label_instructions.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0))

        # Entry widget for custom text input
        self.custom_text_entry = Entry(self.master, width=40)
        self.custom_text_entry.grid(row=1, column=0, columnspan=2, padx=(10, 10), pady=(0, 0))

        # Create the button and configure its properties
        self.default_btn = Button(self.master, text="Default HTML Page", width=20, height=2, command=self.defaultHTML)
        self.default_btn.grid(row=2, column=0, padx=(10, 10), pady=(10, 10))

        # Create a button for custom HTML Page
        self.custom_btn = Button(self.master, text="Custom HTML Page", width=20, height=2, command=self.customHTML)
        self.custom_btn.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))

    # Define the defaultHTML method as a method of the class
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        self.generateHTML(htmlText)

    # Define a method to handle custom HTML generation
    def customHTML(self):
        custom_text = self.custom_text_entry.get()
        # Use default text if custom text is empty
        htmlText = custom_text if custom_text else "Stay tuned for our amazing summer sale!"
        self.generateHTML(htmlText)

    # Define a method to generate HTML and open it in a new tab
    def generateHTML(self, htmlText):
        htmlFile = open("index.html", "w")
        htmlContent = f"<html>\n<body>\n<h1>{htmlText}</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()



