"""GUI module providing the .. GUI"""
from tkinter import Tk, filedialog, StringVar, Label, Button, Text, Scrollbar
from exprmap import createExpressionMaps

class gui():
    def __init__(self, master):
        """GUI class"""
        self.master = master
        master.title("Expression-Map-Creator")

        self.selectedFilesList = list()
        self.text = str()
        self.selectedFilesLabelText = StringVar()
        self.selectedFilesLabelText.set("0 files selected")
        self.selectedFilesLabel = Label(textvariable=self.selectedFilesLabelText)
        self.selectedFilesLabel.grid(row=4, sticky='W')

        self.textField = Text(borderwidth=0)
        yScrollbar = Scrollbar(master)
        yScrollbar.grid(row=3, column=1, sticky='N'+'S')
        self.textField.config(state='disabled', yscrollcommand=yScrollbar.set)
        self.textField.grid(row=3, sticky='W')
        yScrollbar.config(command=self.textField.yview)

        self.browse_button = Button(text="Select Files", borderwidth="0", activebackground="gray80", command=self.selectFiles)
        self.browse_button.grid(row=0, sticky='W')

        self.createExprMapButton = Button(text="Create Expression Maps", borderwidth="0", activebackground="gray80", command=self.createExpMap)
        self.createExprMapButton.config(state='disabled')
        self.createExprMapButton.grid(row=0, column=0, sticky='E')

        self.outputLabelText = StringVar()
        self.outputLabel = Label(textvariable=self.outputLabelText)
        self.outputLabel.grid(row=4, sticky='E')

    def selectFiles(self):
        """selectFiles handles selection of files to turn into expression maps"""
        self.textField.config(state='normal')
        self.textField.delete('1.0', 'end')
        filenames = filedialog.askopenfilenames()
        for f in filenames:
            self.selectedFilesList.append(f)
            self.textField.insert('end', "Selected: " + f + "\n")
        self.selectedFilesLabelText.set(str(len(filenames)) + " file(s) selected")
        self.textField.config(state='disabled')
        self.createExprMapButton.config(state='normal')
        self.textField.see('end')

    def createExpMap(self):
        """createExpMap allows a user to select the output directory and will then create the expression maps from the loaded yaml files"""
        dest = filedialog.askdirectory()
        self.outputLabelText.set("Location:" + dest)
        self.textField.config(state='normal')
        self.textField.insert('end', "\nCreating expression maps from selected files..")
        results = createExpressionMaps(self.selectedFilesList)
        for result in results:
            self.textField.insert('end', "\nCreated " + str(result))
        self.textField.config(state='disabled')
        self.textField.see('end')

root = Tk()
gui = gui(root)
root.resizable(width=False, height=False)
