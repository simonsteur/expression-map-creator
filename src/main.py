#!/usr/bin/env python3
"""main module"""
from args import args
from files import readArticulationsFromFile, readArticulationsFromDir
from exprmap import createExpressionMap, createExpressionMaps

def main():
    """main function"""
    if args.file != "":
        print("Using file to create expression maps")
        f = readArticulationsFromFile(args.file)
        createExpressionMap(f, args.dest)
    elif args.dir != "":
        print("Reading files from directory to create expression maps")
        files = readArticulationsFromDir(args.dir)
        createExpressionMaps(files, args.dest)
    else:
        #start gui
        from gui import root
        root.mainloop()

if __name__ == "__main__":
    main()
