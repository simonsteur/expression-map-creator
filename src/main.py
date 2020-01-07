#!/usr/bin/env python3
"""main module"""
from args import args
from files import readArticulationsFromFile, readArticulationsFromDir
from exprmap import createExpressionMap

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
