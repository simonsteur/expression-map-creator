#!/usr/bin/env python3
"""main module"""
from tkinter import Tk, filedialog, StringVar, Label, Button, ttk
from args import args
from files import readArticulationsFromFile, readArticulationsFromDir
from exprmap import createExpressionMap

def select_files():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global files
    filenames = filedialog.askopenfilenames()
    print(filenames)
    for f in filenames:
        print(f)
        files.append(f)

app = Tk()
app.title("Expression-Map-Creator")
app.geometry("1000x820")
app.configure(background='gray80')

files = list()


lbl1 = Label(master=app, textvariable=str(files), bg='gray75')
lbl1.place(x=10, y=50, width=800)

button1 = Button(text="Select Files", command=select_files, bg='gray70', bd='0')
button1.place(x=10, y=10, width=120, height=25)


app.mainloop()

def main():
    """main function"""
    if args.file != "":
        print("Using file to create expression maps")
        file = readArticulationsFromFile(args.file)
        createExpressionMap(file)
    elif args.dir != "":
        print("Reading files from directory to create expression maps")
        files = readArticulationsFromDir(args.dir)
        for file in files:
            file = readArticulationsFromFile(file)
            createExpressionMap(file)

if __name__ == "__main__":
    main()
