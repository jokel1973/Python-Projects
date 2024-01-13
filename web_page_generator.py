


import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

         # Label for instructions
        label_instructions = Label(self.master, text="Enter Custom text or click the Default HTML button")
        label_instructions.grid(row=0, column=0, columnspan=2, padx=(10, 10), pady=(10, 0))


        # Creates the Entry widget for custom text input field
        self.custom_text_entry = Entry(self.master, width=40)
        self.custom_text_entry.grid(row=1, column=0, columnspan=2, padx=(10, 10), pady=(10, 0))

        # Creates the button and sets size and location
        self.default_btn = Button(self.master, text="Default HTML Page", width=20, height=2, command=self.defaultHTML)
        self.default_btn.grid(row=3, column=0, padx=(10, 10), pady=(10, 10))

        # Creates a button for custom web page and sets the size and location of the button
        self.custom_btn = Button(self.master, text="Custom HTML Page", width=20, height=2, command=self.customHTML)
        self.custom_btn.grid(row=3, column=1, padx=(10, 10), pady=(10, 10))

    # Defines the defaultHTML method 
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        self.generateHTML(htmlText)

    # Definse a method to handle custom text
    def customHTML(self):
        custom_text = self.custom_text_entry.get()
        # Use default text if custom text is empty
        htmlText = custom_text if custom_text else "Stay tuned for our amazing summer sale!"
        self.generateHTML(htmlText)

    # Defines a method to generate HTML and open it in a new tab
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
