#-----------------------------------------------ENJOY GUYS---------------------------------------------------
#add 1.ico icon image in directory than run this program - icon of Tkinter file
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None   # Assigning None to a variable is a way of explicitly stating that it currently does not have a valid value or reference
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])  #here defaultextension and filetypes are keyword arguments not variables
    if file == "":
        file = None   # Assigning None to a variable is a way of explicitly stating that it currently does not have a valid value or reference
        #by use of os function name of file fetch directly and attached default extension 
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close() #good practice to close the file after use


def saveFile():
    global file
    if file == None: #in this case reference(name and it's data)  # Assigning None to a variable is a way of explicitly stating that it currently does not have a valid value or reference
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None     

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            #write write content in file than askforname
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:#in this case only data file not none so name is there
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def Select():
    TextArea.tag_add("sel", "1.0","end") # all text selected
    TextArea.tag_config("sel",background="green",foreground="red")

#we can also use "<cut>", "<copy", "<paste>" alternate option for (cut paste and copy)

def cut():
    global data 
    if TextArea.selection_get():  #otherwise nothing it will do
        data=TextArea.selection_get() # copy selected text to clipboard 
        TextArea.delete('sel.first','sel.last') # delete selected text 

def copy():
    global data 
    if TextArea.selection_get():
        data=TextArea.selection_get() # copy selected text to clipboard 

def paste():
    global data
    # data = root.clipboard_get()  #this statement can Fetch data from the clipboard
    TextArea.insert("insert", data)  # Paste data from clipboard

def about():
    showinfo("Notepad", "Notepad by _Shinu_Aman_")

if __name__ == '__main__':   #Code within this block will only execute if the script is run directly, not when it is imported as a module. 
    #use for security purpose can't able to use from another file
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("C:/Users/Seenu/OneDrive/Desktop/PYTHON/tkinter/hello.ico")#hello.ico icon in local system and inside brackets it's address is there

    root.geometry("644x788")

    #Add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    # To save the current file

    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)     #add in menu bar sequence create after designing it's inner command
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Select all", command=Select)
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)    #add in menu bar sequence create after designing it's inner command

    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)   #add in menu bar sequence create after designing it's inner command

    # Help Menu Ends

    root.config(menu=MenuBar)  #configured using config like use to establish the design

    #Adding Scrollbar on textarea and for now complete is textarea
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
