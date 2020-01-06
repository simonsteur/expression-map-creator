"""main module"""
from articulations import readArticulationsFile
from exprmap import createExpressionMap



def main():
    """main function"""
    articulations = readArticulationsFile()
    createExpressionMap(articulations)

if __name__ == "__main__":
    main()
